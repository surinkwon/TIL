#  Git 정리

**로컬 저장소 생성**

```
폴더를 만들고 그 안에서 명령
git init
```

**파일 관리(애드, 커밋)**

```
staging area 로 올리기
git add (.으로 하면 현재 디렉토리에 있는 모든 내용을 staging area로 올림, 하나의 파일만 하고 싶으면 파일 이름을 확장자와 함께 적어주면 됨)

커밋 남기기
git commit -m "커밋 메시지"

로컬에서 깃허브 레포에 올리기
git push

깃허브 레포에서 로컬로 가져오기
git pull

깃 사용 내역
git log
```

**유저 이름 / 이메일 등록**

```
저장소 별 유저 등록 시(global 옵션보다 우선 적용)
git config user.name "유저 이름"
git config user.email "유저 이메일"

하나의 계정을 계속 사용 시
git config --global user.name "유저 이름"
git config --global user.email "유저 이메일"
```

**현재 저장소 유저 이름 / 이메일 확인**

```
git config user.name
git config user.email
```

**유저 이름 / 이메일 삭제**

```
저장소 설정 삭제
git config --unset user.name
git config --unset user.email

global 설정 삭제
git config --global --unset user.name
git config --global --unset user.email
```

**커밋 간 차이**

```
git diff 커밋아이디(앞 4자리) 비교할 커밋아이디
```

**깃허브 레포를 로컬에 카피 / 로컬 레포를 깃허브에 올리기**

```
로컬에 카피
git clone 레포 주소

깃허브에 카피
1. 깃허브에 빈 레포 만들기
2. git remote add origin 레포 주소
3. git push -u origin master(로컬에 저장된 branch 이름)
```

**add 취소**

```
저장소에 커밋이 있었을 때
git restore --staged 파일명

저장소에 커밋이 하나도 없었을 때
git rm --cached 파일명
```

