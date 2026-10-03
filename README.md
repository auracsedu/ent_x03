# 시작하기

vscode에서 프로젝트를 열고, 아래 명령어를 실행하세요.
(명령어 대신 [VS Code 작업으로 실행하기](#vs-code-작업으로-실행하기)의 `환경 설정` 작업을 써도 됩니다.)

Windows:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\setup.ps1
```

MacOS:

```bash
chmod +x ./setup.sh
./setup.sh
```

# 테스트 돌리기

터미널에서 다음을 붙여넣으면 테스트가 됩니다.

## 전체 테스트하기

```bash
python -m pytest
```

## 특정 번호만 테스트하기

```bash
python -m pytest -k problem_01
```

# VS Code 작업으로 실행하기

터미널 명령어 대신 VS Code 메뉴 `Terminal > Run Task...` (한국어 UI: `터미널 > 작업 실행...`)에서 아래 작업을 선택해도 됩니다.

| 작업                 | 하는 일                                                                       |
| -------------------- | ----------------------------------------------------------------------------- |
| `환경 설정`          | `setup.ps1` / `setup.sh` 실행 (Windows에서는 실행 정책 설정 없이 바로 됩니다) |
| `전체 테스트`        | `python -m pytest`                                                            |
| `특정 번호만 테스트` | 문제 번호를 입력받아 `python -m pytest -k problem_번호` 실행                  |

# 문제 목록 (3주차: 직접 만들어 보기, 그리고 재귀)

각 파일 맨 위의 설명을 읽고, `raise NotImplementedError` 를 지우고 그 자리에
코드를 작성하세요.

| 파일                  | 주제                                     | 핵심              |
| --------------------- | ---------------------------------------- | ----------------- |
| `problem_01.py`       | `split` 직접 만들기                      | 조각 모으기       |
| `problem_02.py`       | `find` 직접 만들기 (함수 2개)            | 슬라이싱으로 비교 |
| `problem_03.py`       | `join`, `replace` 직접 만들기 (함수 2개) | 위치 직접 옮기기  |
| `problem_04.py`       | `round` 직접 만들기                      | 자릿수 계산       |
| `problem_05.py`       | 중첩 리스트 펼치기                       | **재귀 입문**     |
| `problem_06.py`       | 하노이 탑                                | 재귀로 생각하기   |
| `problem_07.py`       | 조합 (combinations)                      | 쓴다 / 안 쓴다    |
| `problem_08.py`       | 순열 (permutations)                      | 첫 자리 고르기    |
| `problem_09.py`       | 한 줄에서 단어 찾기                      | **백트래킹**      |
| `problem_extra_01.py` | 보드에서 단어 찾기                       | 백트래킹 (2차원)  |
| `problem_extra_02.py` | 보드에서 단어 찾기 (재사용 불가)         | 백트래킹 (2차원)  |

숙제는 `python -m pytest -k problem_extra_01` 처럼 테스트합니다.
