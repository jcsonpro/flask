# flask
### flask 를 이용한 게시판 제작 (Windows 개발환경 기준)



### 1. github repository 생성 및 clone

```bash
kcomwel@DESKTOP-9D5BLO8 D:\workspace
$ git -c http.sslVerify=false clone https://github.com/jcsonpro/flask.git
Cloning into 'flask'...
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (4/4), done.

kcomwel@DESKTOP-9D5BLO8 D:\workspace
$ git config --global http.sslVerify false
```

- 클론시 SSL 오류가 발생 : git -c http.sslVerify=false clone <repository> 명령을 사용함



### 2. Typora / ConEmu설치



### 3. Python 3.8.5 버전 설치

- [파이썬 3.8.5 다운로드 ](https://www.python.org/downloads/release/python-385/) 
- 윈도우즈 설치시 Add Python 3.8 to Path 옵션 체크

### 

### 4. 가상환경 설정

```bash
kcomwel@DESKTOP-9D5BLO8 D:\workspace\flask
$ mkdir venvs

kcomwel@DESKTOP-9D5BLO8 D:\workspace\flask
$ cd venvs

kcomwel@DESKTOP-9D5BLO8 D:\workspace\flask\venvs
$ dir
 Volume in drive D has no label.
 Volume Serial Number is 0D32-1255

 Directory of D:\workspace\flask\venvs

2022-03-29  오전 10:27    <DIR>          .
2022-03-29  오전 10:27    <DIR>          ..
               0 File(s)              0 bytes
               2 Dir(s)  1,999,189,688,320 bytes free

kcomwel@DESKTOP-9D5BLO8 D:\workspace\flask\venvs
$ python -m venv myproject

kcomwel@DESKTOP-9D5BLO8 D:\workspace\flask\venvs
$ dir
 Volume in drive D has no label.
 Volume Serial Number is 0D32-1255

 Directory of D:\workspace\flask\venvs

2022-03-29  오전 10:35    <DIR>          .
2022-03-29  오전 10:35    <DIR>          ..
2022-03-29  오전 10:35    <DIR>          myproject
               0 File(s)              0 bytes
               3 Dir(s)  1,999,174,053,888 bytes free
```

- #### 가상환경 진입 / 해제

  ```bash
  kcomwel@DESKTOP-9D5BLO8 D:\workspace\flask\venvs\myproject
  $ cd scripts
  
  kcomwel@DESKTOP-9D5BLO8 D:\workspace\flask\venvs\myproject\Scripts
  $ dir
   Volume in drive D has no label.
   Volume Serial Number is 0D32-1255
  
   Directory of D:\workspace\flask\venvs\myproject\Scripts
  
  2022-03-29  오전 10:35    <DIR>          .
  2022-03-29  오전 10:35    <DIR>          ..
  2022-03-29  오전 10:35             2,304 activate
  2022-03-29  오전 10:35               976 activate.bat
  2022-03-29  오전 10:35            18,456 Activate.ps1
  2022-03-29  오전 10:35               368 deactivate.bat
  2022-03-29  오전 10:35           106,373 easy_install-3.8.exe
  2022-03-29  오전 10:35           106,373 easy_install.exe
  2022-03-29  오전 10:35           106,364 pip.exe
  2022-03-29  오전 10:35           106,364 pip3.8.exe
  2022-03-29  오전 10:35           106,364 pip3.exe
  2022-03-29  오전 10:35           532,040 python.exe
  2022-03-29  오전 10:35           531,016 pythonw.exe
                11 File(s)      1,616,998 bytes
                 2 Dir(s)  1,999,174,053,888 bytes free
  
  kcomwel@DESKTOP-9D5BLO8 D:\workspace\flask\venvs\myproject\Scripts
  $ activate
  
  (myproject) kcomwel@DESKTOP-9D5BLO8 D:\workspace\flask\venvs\myproject\Scripts
  $ deactivate
  ```

  

### 5. Pycharm 설치

- [파이참 community 버전 다운로드](https://www.jetbrains.com/ko-kr/pycharm/download/#section=windows)

- 설치완료후 "Server's certificate is not trusted " 오류 해결
  - File > Settings > Tools > Server Certificates > Accept non-trusted certificates automatically 체크
  - Appearance & Behavior > System Settings > Updates > Use Secure connection 체크 해제
  
- trusted-host 옵션 지정
  - 업무망에서 플라스크등 파이썬 패키지를 설치할때, ssl 오류가 발생한다
  
  - c:\user\<사용자명>\pip\pip.ini 파일을 만들어서 해결
  
    ```bash
    [global]
    #### 이부분은 혹시 몰라서 기록해둔다
    # proxy = http://PROXYSERVERIP:PORT    
    # cert = C:\\CERTIFICATION.cer
    
    ### 아래부분만 기록해도 해결됬음
    trusted-host = pypi.python.org
                   pypi.org
                   files.pythonhosted.org
    ```
  
  - pip도 최신버전으로 업그레이드 한다
  
    ```bash
    > python -m pip install --upgrade pip
    ```
  
- 가상환경 인터프리터 설정
  - windows : D:\workspace\flask\venv\Scripts\python.exe
  - (OLD) mac : /Users/jongchanson/.pyenv/versions/3.8.12/bin/python3.8
    - mac은 python 버전관리인 pyenv가 적용되어 있으므로, 인터프리터를 .pyenv/versions/3.8.12/bin/python3.8로 설정
  - (NEW) mac : /workspace/flask/venv/bin/python
    ```bash
    # pyenv를 이용해서, python 3.8.5를 설치한다
    > pyenv install 3.8.5
    > pyenv global 3.8.5
    > pyenv versions
    ```
  - github에서 flask.git을 clone한다
  - 프로젝트 디렉토리(flask)에 가상환경을 생성한다
    ```bash
    python -m venv flask/venv
    ```
  - mac pycharm에서 flask 디렉터리를 "열기"

- windows에서 pip 패키지 requirement.txt 작성
  ```bash
  pip freeze > requirement.txt
  ```
- mac에서 설치목록으로 환경 생성 (CLI 가 venv 환경인지 확인해야 한다)