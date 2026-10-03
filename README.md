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

# 문제 목록 (3주차: 반복, 그리고 재귀로 하는 완전탐색)

각 파일 맨 위의 설명을 읽고, `raise NotImplementedError` 를 지우고 그 자리에
코드를 작성하세요. 01~04는 반복문과 문자열 다루기, 05~06은 재귀와 백트래킹입니다.

| 파일            | 주제                              | 핵심                   |
| --------------- | --------------------------------- | ---------------------- |
| `problem_01.py` | n번째 소수                        | 반복문, 제곱근까지 검사 |
| `problem_02.py` | 알파벳 첫 위치                    | str.find()             |
| `problem_03.py` | 반올림 직접 만들기                | 자릿수 계산            |
| `problem_04.py` | 대소문자 바꾸기                   | 문자열 만들기          |
| `problem_05.py` | 보드에서 단어 찾기 (재사용 가능)  | 재귀                   |
| `problem_06.py` | 보드에서 단어 찾기 (재사용 불가)  | 재귀 + 백트래킹        |

`problem_05.py` 와 `problem_06.py` 는 함수 이름이 같고 규칙만 다릅니다.
05를 먼저 풀고, 그 코드를 고쳐서 06을 푸는 것이 가장 쉽습니다.
