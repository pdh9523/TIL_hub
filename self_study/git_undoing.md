# 깃 취소

깃의 수정 사항을 만들어 staging area에 등록한 것을 취소하는 과정

`git restore` : 현재 작업 중인 워킹 디렉토리의 변화를 원래대로 되돌린다. 

`git restore --staged` : 현재 staging area에 올라간 작업물을 다시 워킹 디렉토리로 데려온다 

`git rm --cached {file}` : 아직 커밋 되기 전 캐싱 되어 있는 자료를 삭제한다

`git commit --amend` : 깃 커밋명을 수정하고 싶을 때.
수정 하는 그 당시의 add 된 파일도 같이 commit 된다.

`git reset --soft` : 커밋하기 직전으로 돌리기

`git reset --mixed` : soft + 언스테이지까지 

`git reset --hard` : mixed + 워킹디렉토리 삭제까지 





`git --` :