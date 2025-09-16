# Django REST Framework 연습 프로젝트

## 개요
User - Article - Comment 구조를 가진 DRF API 연습 프로젝트

## 연습 순서

### 1. Django 프로젝트 초기 설정
- [x] DRF 패키지 설치
- [x] settings.py에 DRF 설정 추가
- [x] INSTALLED_APPS에 rest_framework 추가
- [x] 기본 DRF 설정 구성

### 2. User 모델 커스터마이징
- [x] accounts 앱 생성
- [x] AbstractUser 상속한 커스텀 User 모델 생성
- [x] settings.py에 AUTH_USER_MODEL 설정

### 3. Article, Comment 모델 생성
- [x] articles 앱 생성
- [x] Article 모델 생성 (제목, 내용, 작성자, 작성일 등)
- [x] Comment 모델 생성 (내용, 작성자, 게시글, 작성일 등)
- [x] ForeignKey 관계 설정
- [x] 마이그레이션 실행

### 4. DRF Serializers 작성
- [x] UserSerializer 작성
- [x] ArticleSerializer 작성 (List/Detail 분리)
- [x] CommentSerializer 작성
- [x] 중첩 관계 처리 (Nested Serializers)
- [x] SerializerMethodField 활용

### 5. ViewSets/APIViews 구현
- [x] UserViewSet 구현 (회원가입, 프로필 조회/수정)
- [x] ArticleViewSet 구현 (CRUD)
- [x] CommentViewSet 구현 (CRUD)
- [x] 커스텀 액션 추가 (좋아요, 팔로우 등)

### 6. URL 라우팅 설정
- [x] DefaultRouter 설정
- [x] ViewSet 라우터 등록
- [x] 커스텀 URL 패턴 추가
- [x] API 버전 관리 (v1/)

### 7. 인증/권한 설정
- [ ] Token 또는 JWT 인증 구현
- [ ] 로그인/로그아웃 API
- [ ] Permission Classes 설정
- [ ] 작성자만 수정/삭제 가능하도록 권한 설정

### 8. 고급 기능 추가
- [ ] 페이지네이션 설정
- [ ] 필터링 기능 (django-filter)
- [ ] 검색 기능 구현
- [ ] 정렬 기능 추가
- [ ] Throttling 설정

### 9. API 테스트
- [ ] 테스트 코드 작성 (APITestCase)
- [ ] Postman 컬렉션 생성
- [ ] 각 엔드포인트 테스트
- [ ] 예외 처리 테스트

### 10. API 문서화
- [ ] drf-spectacular 또는 drf-yasg 설치
- [ ] Swagger UI 설정
- [ ] API 스키마 생성
- [ ] 문서화 커스터마이징

## API 엔드포인트 (예정)

### 인증
- `POST /api/v1/auth/signup/` - 회원가입
- `POST /api/v1/auth/login/` - 로그인
- `POST /api/v1/auth/logout/` - 로그아웃

### Users
- `GET /api/v1/users/` - 사용자 목록
- `GET /api/v1/users/{id}/` - 사용자 상세
- `PUT /api/v1/users/{id}/` - 사용자 정보 수정
- `DELETE /api/v1/users/{id}/` - 회원 탈퇴

### Articles
- `GET /api/v1/articles/` - 게시글 목록
- `POST /api/v1/articles/` - 게시글 작성
- `GET /api/v1/articles/{id}/` - 게시글 상세
- `PUT /api/v1/articles/{id}/` - 게시글 수정
- `DELETE /api/v1/articles/{id}/` - 게시글 삭제
- `POST /api/v1/articles/{id}/like/` - 좋아요

### Comments
- `GET /api/v1/articles/{article_id}/comments/` - 댓글 목록
- `POST /api/v1/articles/{article_id}/comments/` - 댓글 작성
- `PUT /api/v1/comments/{id}/` - 댓글 수정
- `DELETE /api/v1/comments/{id}/` - 댓글 삭제

## 주요 학습 내용
- Django REST Framework 기본 구조
- Serializer와 ViewSet 활용
- 인증과 권한 관리
- API 설계 패턴
- RESTful API 원칙