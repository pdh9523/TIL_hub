## Git branch
브랜치 조회, 생성, 삭제 등 브랜치와 관련된 Git 명령어

```bash
$ git branch # 브랜치 목록 확인

$ git branch -r # 원격 저장소의 브랜치 목록 확인

$ git branch < 브랜치 이름 > # 새로운 브랜치 생성

# 특정 브랜치 삭제

$ git branch -d < 브랜치 이름 > # 병합된 브랜치만 생성 가능

$ git branch -D < 브랜치 이름 > # 병합되지 않은 브랜치도 강제 삭제 
```

## Git switch
현재 브랜치에서 다른 브랜치로 'HEAD'를 이동시키는 명령어
```bash

# 다른 브랜치로 이동
$ git switch < 다른 브랜치 이름 >

# 브랜치를 새로 생성과 동시에 이동
$ git switch -c < 브랜치 이름 >

# 특정 커밋 기준으로 브랜치 생성과 동시에 이동
$ git switch -c < 브랜치 이름 > < 커밋 ID >
```

### Branch Merge

```bash
$ git merge branch1 # 현재 HEAD에 branch1을 병합한다. 


```

### 병합의 종류
1. Fast-Forward
  - 브랜치를 병합할 때 마치 빨리감기 처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 것
2. 3-Way Merge (Merge commit)
  - 병합 시 각 브랜치의 커밋 두 개와 공통 조상 커밋 하나를 사용하여 병합하는 것으로, 두 브랜치에서 다른 파일 혹은 같은 파일의 다른 부분을 수정했을 때 수행가능한 병합
3. Merge Conflict
  - 