# Poetry 란?
- pip의 상위호환 : pip + venv + requirements.txt
- 가상환경을 생성하고, 설치한 라이브러리나 프레임워크를 일일이 freeze로 기록해야하는 pip와 다르게  
알아서 poetry.lock으로 종속성을 관리해줌. 
- PEP 518 표준인 pyproject.toml 로 프로젝트를 관리하는 것을 도와줌
    - PEP : 파이썬의 개선 제안 문서. 파이썬을 사용할 때 기능이나 표준을 정의할 때 쓰는 일종의 파이썬계의 법안.
    - blck, isort, mypy, ruff, coverage, pytest 설정을 pyproject.toml 한곳에 모읍니다.
    - 모든 종속성 fastapi의 버전을 관리함 : fastapi가 의존하는 하위 라이브러리 버전을 관리함.
- pip 보다 좀 똑똑한 dependency resolving : 라이브러리가 요구하는 다른 라이브러리를 설치할 때 자동으로 버전을 맞춰줌.

# Poetry 설치 방법
1. python3 --version : 파이썬 버전 확인. 3.8 이상만 호환됨
2. curl -sSL https://install.python-poetry.org | python3 - --version 1.8.5 : Poetry 설치
3. echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc : PATH 환경변수에 Poetry가 설치된 디렉터리 경로를 추가.
4. source ~/.zshrc : 추가한 사항 적용
5. poetry --version : 버전 확인. 버전이 나오면 성공.