# Git 시작하기

git이 뭘까? **분산 버전 관리 시스템**

**버전관리**

- 코드의 히스토리(버전)을 관리하는 도구
- 개발되어 온 **과정** 파악 가능
- 이전 버전과의 변경 사항 비교 및 분석



**분산**

- 깃은 변경 사항만을 저장
- *이전 히스토리와 비교해서 이전에 있던 것을 모두 저장하는 게 아니라 변경된 것만 저장하는 것*



버전관리를 하는 프로그램이 **git**

버전관리된 데이터들을 저장하는 곳이 **git hub**

깃허브와 비슷한 역할을 하는 저장소들이 깃랩과 비트버켓

다만 깃허브는 서버가 마이크로소프트에 귀속된 것이고

깃랩은 내가 서버를 구축해서 거기에다 저장할 수 있도록 해줌



*명령프롬프트에서는 unix, linux 명령어를 사용할 수 없음*

powershell에서는 일부 사용 가능

CLI -> 명령프롬프트처럼 명령어를 쳐서 실행하는 환경

GUI -> 윈도우나 맥오에스처럼 그래픽을 보며 컴퓨터에 명령을 내리는 환경



예: 파일과 폴더의 목록을 보여주는 명령어가 윈도우에서는 dir, 유닉스에서는 ls

명프 화면 줄 지우는 것은 cls, 유닉스에서는 clear

깃이나 파워셸 옆에 나오는 ~는 home 디렉토리를 말함(맨 처음에 나오는 위치)



## Unix / Linux 명령어

- 현재 위치의 폴더, 파일 목록보기 **ls**
- 현재 위치 이동하기 **cd <path>** (꺽쇠는 쓰는 거 아님), 폴더 이름이 길 때는 적당히 폴더 앞글자 쓰고 탭을 누르면 됨
- **cd ..** 상위 폴더로 이동 (깃에서는 cd ~)
- 폴더 생성하기 **mkdir <name>**
- 파일 생성하기 **touch <name>** 이거는 윈도우에서 지원 안됨... 깃에서는 지원 됨
- 파일 삭제하기 **rm<name>** / 폴더 삭제하기 **rm -r<name>**(보호받는 파일이라면 **-rf**해주면 됨)
- **code .** 해당 폴더에서 vs코드 엶

vscode에서도 git bash 터미널로 실행 가능



## Git 기본기

README를 깃허브에 올리면 프로젝트 설명서로 인식해 깃허브 맨 처음 화면에 이 문서를 보여줌



### Repository

특정 디렉토리를 버전 관리하는 저장소

- **git init** 명령어로 로컬 저장소를 생성
- **.git** 디렉토리에 버전관리에 필요한 모든 것이 들어있음(.으로 시작하는 파일은 숨김처리 되어 있어서 그냥 들어가면 안 보임, 깃이 알아서 관리해줌)
- .git 디렉토리 안이 repository라고 생각하면 됨



어떤 프로젝트를 **특정 버전**으로 남긴다 = **커밋(commit)** 한다

repository 안에 commit이 점점 쌓여 감

커밋은 3가지 영역을 바탕으로 동작

- **Working Directory**: 내가 작업하고 있는 실제 디렉토리(예: RacingGround)
- **Staging Area**: 커밋으로 **남기고싶은**, 특정버전으로 관리하고 싶은 파일이 있는 곳(변경사항이 잠시 위치하는 곳)
- **Repository**: 커밋들이 저장되는 곳

**git add** 명령어를 이용해야 변경사항들이 staging area로 올라옴(깃에 의해 추적됨) (git add <file_name>)



**git status** 명령어

- 깃에 추적되는 상태인지 아닌지를 알려줌(staging area에 있는지)

stage에 있는 상태에서 **git commit** 명령어를 쓰면 하나의 버전이 남게 되는 것

예)

git commit **-m** "init"

**-m**은 메시지를 남기겠다는 것(자세하게 적을수록 좋음)



**git add .** (여기서 .은 현재위치를 의미 )

- 추적되지 않은 모든 파일과 추적하고 있는 파일 중 수정된 파일을 모두 staging area에 올림



**git log**

- 깃을 사용한 내역을 보여줌



**유저 네임과 이메일을 깃 허브에 등록**

git config user.name "user_name"

git config user.email "user_email"

**하나의 계정으로 깃을 사용하려 할 때는**

git config --global user.name "user_name"

git config --global user.email "user_email"



*깃허브에는 하나의 유저네임에 여러개의 이메일을 둘 수 있고 메인 이메일을 그 중에서 설정할 수 있음*



*하나의 깃 repository가 있으면 그 안에 폴더를 만들어도 그 폴더 안에 있는 것까지 다 관리가 되기 때문에 하위 폴더에 대한 repository를 다시 만들 필요가 없음 **그렇게 하지 말 것!!!***



바탕화면을 가는 방법은 desktop

*잘못 디렉토리를 생성한 경우 .git 파일 찾아서 지우면 됨*



깃이 타자를 칠 수 없게 되었을 때는 **q**를 누르면 됨



깃으로 vscode여는 법은 열고싶은 폴더 안에서 **code .**



**git diff**

- 커밋간의 차이를 알려주는 명령어
- git diff 커밋아이디 비교할 커밋 아이디 <- 이렇게 사용하면 됨(커밋 아이디는 긴 코드 다가 아니라 앞에 4자리만 해도 거의 다 됨)

-----

**github repository 만들기**(이게 **remote**임)

프로필 들어가서 +누르고 new repository

public으로 설정하면 모두에게 공개되고 누구나 가져갈 수 있음 하지만 내 repository에 다른사람이 올리지는 못함



**github repository를 로컬(내 컴퓨터)로 가져오기**

- *git clone <repository 주소>*
- 깃창에 복붙은 마우스 우클릭 + paste
- 주소 옆에 뜨는 (master), (main) 은 그저 branch의 이름일 뿐임(하나의 큰 줄기의 이름) 



**git push**

파일을 깃허브에 올리는 명령어



잘못해서 git commit만 눌러서 파란 창이 떴으면 :에 **q**를 입력하면 됨

*파란 창의 의미는 거기에다 커밋 메시지를 입력하는 것, 길게 커밋메시지를 입력할 일이 있으면 거기서 치면 됨*



깃허브에서 수정하고 커밋을 하고 싶으면 파일 누르고 연필모양 누르면 됨

***그렇지만 그렇게 하지 마라!***

**git pull**

깃허브에 저장된 업데이트를 내 컴퓨터 저장소로 가져오는 명령어



**로컬 repository를 github로 올리는 방법**

- 깃 허브에서 빈 repository를 하나 만든다.
- *git remote add origin <repository 주소>* -> origin은 별명임(이 저장소를 앞으로 오리진이라고 부를 거야 라고 하는 것, 보통은 이 remote repo를 origin이라고 함 다른 별명보다는)
- 위처럼 한 다음 *git push -u origin master* 이렇게 침 -> -u 는 이렇게 리모트를 생성하고 그것을 보낼때 한 번만 씀, master는 로컬에 저장된 branch의 이름임

git push origin master ->  origin에 있는 master를 push할 거야(모든 push는 이런식으로 이루어져있는데 뒤에 origin master는 생략된 것 repo가 여러개 연결되어 있는 경우 이것들을 알맞은 별명으로 바꿔줘야 함)

-u를 붙이는 이유는 맨 처음 한 번 setup해주는 것

----

깃에서 협업을 할 때는 콜라보레이터를 만들면 됨

- 만들고싶은 repo에 들어가서 *settings*에서 collaborators 들어가기
- add people

그냥 퍼블릭 상태에서는 다른 사람은 push가 안됨

클론은 내가 만들고 싶은 위치에 가서 만들면 됨

*클론을 해도 git config 입력해야한다.*

***push 전에는 pull이 있다.***

*혹시 pull을 하지 않고 push를 한다면?*

- 두 사람이 모두 첫번째 줄을 수정하고 푸쉬를 했다 가정할 때 한 사람이 먼저 push를 했으면 그 다음사람은 pull을 하기 전까지 push를 하지 못함

*그렇다면 동일한 부분을 수정했는데 pull을 했다면?*

- conflict가 생겨서 그 부분에 >>>>>> 이런식으로 꺽쇠괄호가 생김
- 그래서 이 부분을 정상적으로 수정하고 commit, push를 해야함














