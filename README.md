# flask
### flask 를 이용한 게시판 제작



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
