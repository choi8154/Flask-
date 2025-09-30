# Pytest(단위 테스트)
>공식문서 : https://docs.pytest.org/en/stable/contents.html

- 작성한 코드가 정상적으로 동작하는지 검증을 해줌
- 예상하지 못한 에러가 발생하지 않으면 "성공"
- 에러가 발생하면 "실패"
- 검증만 하는 것이기 때문에 테스트 함수는 반환값이 없어야함.

>## 설치 및 실행 방법
1. poetry add --group dev pytest : 설차
    - 설정 : ...
2. pytest --version : 설치 확인
3. test_이름 형식의 파일, 함수, 클래스 생성
4. pytest . : 현재 디렉터리의 모든 테스트 함수를 실행

>## 사용 방법
```py
def add(a:int, b: int) -> int:
    return a+b

def test_add() -> None:
    # Given : 무엇인가 주어졌을 때
    a, b = 1, 1

    # When : 테스트 대상이 되는 함수를 호출합니다.
    result = add(a, b)  # result의 타입은 int

    # Then :
    assert result == 2, "계산이 틀림." #밑의 예제와 같은 역할
    # if not result == 2: raise AssertionError
```
>입력 : pytest .  
>반환 : FAILED test_simple.py::test_add - AssertionError: 계산이 틀림
 

<br>
<br>

---

# Coverage
>공식문서 : https://github.com/nedbat/coveragepy?utm_source=chatgpt.com

- 커버리지 정의 : (테스트도중한번이라도실행된제품코드)/(전체제품코드)
- 커버리지를 통해 실행된 코드와 실행되지 않는 코드를 확인 할 수 있음.
- 코드가 길어지면서 생기는 실행에 필요없는 코드를 확인 할 수 있음.
- 부분 커버리지 :
- 분기 커버리지 :


>## 설치 및 실행 방법
1. poetry add --group dev coverage==7.6.9
2. poetry run coverage run -m pytest temp.py : 
3. poetry run coverage report --help : coverage report의 옵션을 확인
4. poetry run coverage report -m : test로 실행되지 않은 코드의 비율을 보여줌
* 위 실행 방법은 test 코드를 포함하여 연산하므로 옵션을 줘 test코드는 제외되도록 해야함.
5. .toml에 옵션을 추가함.
    - [toll.coverage.run]
    - omit = ["*/test_*.py] : 어디에 있던지 test_로 시작하고 .py로 끝나면 제외함.
    - test_.py 파일을 따로 만들어 test함수를 관리함.
6. 4개의 stmts(순수 코드로만된 라인)만 인식하여 실행되지 않은 코드를 뺀 75% 반환
7. poetry run coverage html : 해당 결과값을 html파일로 반환함.

<br>
<br>

---

# Poetry로 개발용 의존성 관리하기(종속성 분리)

- 배포 단계에서 실행 시 필요없는 종속성을 따로 관리 가능.
- docker 환경에서 종속성 분리가 빛을 발함.

>## 종속성 분리 하여 설치하는 방법
1. poetry install --no-root --only main : dev group 이 아닌 main 그룹만 설치

## 추가 설명
- 프로젝트를 git에서 받고 가상환경을 설치할 때 사용하는 방법임.
- 타인이 git에서 내 프로젝트를 받을 때 용량 문제로 가상환경은 gitignore 해놓음
- 해당 프로젝트를 받은 사람은 poetry install 를 통해 .toml 과 .lock을 통해서 가상환경을 다시 설치함
- 이 때 해당 프로젝트까지 toml에 포함되어 라이브러리로 취급됨. 프로젝트까지 라이브러리로 2번 받아버리는거
- 이 때 자기자신을 제외한 종속성만 받기위해 설정하는 것이 --no-root임.


<br>
<br>

---

# test script
- 코드 수정, 추가, 생성시 일일이 명령어로 test를 돌리는게 아닌 script를 만들어 해당 파일 실행 시 자동으로 test가 가등하도록함.

## 설치 및 실행 방법
1. poetry add --group=dev pytest-asyncio==0.25.0
2. toml 옵션 추가
    - [tool.pytest.ini_option]
    - asyncio_mode = "auto" : 비동기 테스트 실행 방식을 자동으로 결정
    - asyncio_default_fixture_loop_scope = "session" : 전체 pytest 실행 동안 이벤트 루프를 1개만 공유

3. test.sh 알고리즘을 만들어 자동 test하기
```shell
#!/user/bin/env bash
set -eo pipefail

COLOR_GREEN=`tput setaf 2;`
COLOR_NC = `tput sgr0`

echo "starting black"
poetry run black .
echo "OK"

echo "Starting ruff"
poetry run ruff check --select I --fix
poetry run ruff check --fix
echo "OK"

echo "Starting mypy"
poetry run mypy .
echo "OK"

echo "STarting pytest with coverage"
poetry run coverage run -m pytest
poetry run coverage report -m
poetry run coverage html
echo "OK"

echo "${COLOR_GREEN}ALL tests passed successfully!${COLOR_NC}"
```
- 위에서부터 아래로 자동으로 실행되며 오류 검사. 
3. chmod +x ./test.sh : 실행 권한 부여
4. ./test.sh : 테스트 실행

<br>
<br>

---

# Github action script(IC)
>공식 문서 : https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions#on

- CI(Continuous Integration, 지속적 통합) : 코드를 합칠 때마다 자동으로 검사/테스트하는 시스템
- git에서 특정 행위를 할때마다 검사가 가능하도록 파이프라인을 구성함.

## 생성 방법
1. .github/workflows/ci.yml 생성
2. 코드 작성
```yaml
name: CI

on:
  push:


jobs:
  static-analysis: # mypy, black, ruff 등 정적 분석
    runs-on: ubuntu-22.04 # 실제 프로덕션에서는 모든 버전을 고정하는 것이 좋다.
    # 예기치 못한 버전이 올라가서 장애나는 것을 막기 위해
    steps:
      - name: Check out the codes
        uses: actions/checkout@v2

      - name: Setup python environment
        id: setup-python
        uses: actions/setup-python@v2
        with:
          python-version: "3.13"

      - name: Install Poetry
        run: |
          curl -sSL https://install.python-poetry.org | python3 - --version 1.8.5

      - name: Register Poetry bin
        run : echo "$(HOME).poetry/bin" >> $GITHUB_PATH

      - name: Install dependencies
        run: poetry run black. --check # 수정이 아닌 확인 옵션

      - name: Run Ruff
        run: |
          poetry run ruff check --select I
          poetry run ruff check

      - name: Run Mypy
        run: poetry run mypy .


  test: # 전체 테스트 실행
    runs-on: ubuntu-22.04
    steps:
      -
      - name: Check out the codes
        uses: actions/checkout@v2

      - name: Setup python environment
        id: setup-python
        uses: actions/setup-python@v2
        with:
          python-version: "3.13"

      - name: Install Poetry
        run: |
          curl -sSL https://install.python-poetry.org | python3 - --version 1.8.5

      - name: Install dependencies
        run: poetry install --no--root # 수정이 아닌 확인 옵션

      - name: Run tests
        run: |
          poetry run coverage run -m pytest .
          poetry run coverage report -m
```
3. git push
4. 깃허브 해당 프로젝트 레포지토리로 가서 Actions 들어가기
5. introduce CI 클릭하여 실행 중인지 확인하기