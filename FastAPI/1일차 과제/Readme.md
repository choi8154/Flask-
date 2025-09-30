# Poetry
>공식 문서 : 
<br>

- pip의 상위호환 : pip + venv + requirements.txt
- 가상환경을 생성하고, 설치한 라이브러리나 프레임워크를 일일이 freeze로 기록해야하는 pip와 다르게  
알아서 poetry.lock으로 종속성을 관리해줌. 
- PEP 518 표준인 pyproject.toml 로 프로젝트를 관리하는 것을 도와줌
    - PEP : 파이썬의 개선 제안 문서. 파이썬을 사용할 때 기능이나 표준을 정의할 때 쓰는 일종의 파이썬계의 법안.
    - blck, isort, mypy, ruff, coverage, pytest 설정을 pyproject.toml 한곳에 모읍니다.
    - 모든 종속성 fastapi의 버전을 관리함 : fastapi가 의존하는 하위 라이브러리 버전을 관리함.
- pip 보다 좀 똑똑한 dependency resolving : 라이브러리가 요구하는 다른 라이브러리를 설치할 때 자동으로 버전을 맞춰줌.



>## Poetry 설치 및 사용 방법
1. python3 --version : 파이썬 버전 확인. 3.8 이상만 호환됨
2. curl -sSL https://install.python-poetry.org | python3 - --version 1.8.5 : Poetry 설치
3. echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc : PATH 환경변수에 Poetry가 설치된 디렉터리 경로를 추가.
4. source ~/.zshrc : 추가한 사항 적용
5. poetry --version : 버전 확인. 버전이 나오면 성공.

<br>
<br>
<br>

# black
>공식 문서 : https://github.com/psf/black
<br>

- black . : 기능적인 부분에서 차이가 없지만 명령어 한번으로 코드의 가독성을 높여준다.
- 쓰는 이유 : 코드 스타일로인해 팀원들간의 마찰을 줄여줌.



>## black 설치 및 사용 방법
1. poetry add --group=dev black : poetry 가상환경에 black 설치.
2. black --version : 설치가 되었는지 확인.
3. black . 혹은 poetry run black . : black을 사용하여 현재 폴더의 모든 파일의 코드 스타일을 수정.
4. [tool.black] line-length = 10 : .toml 파일에서 black의 스타일을 수정 할 수 있음.

<br>
<br>
<br>

# ruff
>공식 문서 : https://github.com/astral-sh/ruff
<br>

- rust언어로 작성된 formatter + linter 임
- 현재 디렉터리의 코드에서 수정해야할 부분과 오류의 원인을 분석, 수정해줌.
- formatter란?
- E401 과 같은 flake8rules 코드로 오류의 종류를 확인 가능.
- flake8rules 링트 : https://www.flake8rules.com/



>## ruff 설치 및 사용 방법
1. poetry add --group=dev ruff : ruff를 가상환경에 설치.
2. ruff --version : 설치 확인.
    - [tool.ruff], target-version = "py313" : .toml에서 파이썬 버전 설정
3. ruff check : 터미널에 실행하면 현재 디렉터리의 코드에서 수정해야할 부분과 오류의 원인을 분석해줌.
4. ruff check . --fix : 검사 후 가능한 범위에서 자동으로 수정해줌.
5. ruff check --select I --fix : 임포트 순서를 정렬해줌.
5. '# noqa' : 의도한 경우 코드 뒤에 이 주석을 달면 오류로 인식하지 않음.

<br>
<br>
<br>

# Git
1. init : 해당 폴더를 git으로 초기화
2. git ignore : 파일을 만들어 push 할 필요 없응 파일을 따로 관리
3. git remote add origin url : 해당 git 폴더를 원격저장소와 연결
- 지켜야하는 습관
    - commit 하기 전 "자신이 무엇을 커밋하는지" 꼭 확인하기.
    - print I/O라서 CPU 연산보다 훨씬 느려림. 서버 코드에서 너무 많이 쓰면 성능에 부담을 줄 수 있음. 의도하지 않은 경우 확실히 제거할 것

<br>
<br>
<br>

# mypy
>공식문서 : https://github.com/python/mypy
<br>

- 개발 환경에서 발생할 수 있는 문제를 사전에 예방할 수 있는 툴.
- 쓰는 이유 : 파이썬은 동적언어임. 타입힌팅은 말그대로 힌트이기 때문에 강제성이 없음. 그때문에 mypy를 써야함.
- fastapi에서 pydentic 모델이 있는데 왜 mypy를 써야함?
    - mypy : 서버 열기 전 타입힌트와 코드가 맞는지 검사하고 아니면 오류 호출
    - pydentic : 서버 실행중 클라이언트에게서 들어오는 데이터를 검증
