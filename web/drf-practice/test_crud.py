"""
CRUD API 테스트 가이드

1. 서버 실행
python manage.py runserver

2. 슈퍼유저 생성 (테스트용)
python manage.py createsuperuser

3. API 엔드포인트 및 CRUD 테스트
"""

# User CRUD
user_endpoints = {
    "CREATE": "POST /api/v1/signup/",
    "READ_LIST": "GET /api/v1/users/",
    "READ_DETAIL": "GET /api/v1/users/{user_id}/",
    "UPDATE": "PUT /api/v1/users/{user_id}/",
    "DELETE": "DELETE /api/v1/users/{user_id}/",
    "FOLLOW": "POST /api/v1/users/{user_id}/follow/"
}

# Article CRUD
article_endpoints = {
    "CREATE": "POST /api/v1/articles/",
    "READ_LIST": "GET /api/v1/articles/",
    "READ_DETAIL": "GET /api/v1/articles/{article_id}/",
    "UPDATE": "PUT /api/v1/articles/{article_id}/",
    "DELETE": "DELETE /api/v1/articles/{article_id}/"
}

# Comment CRUD
comment_endpoints = {
    "CREATE": "POST /api/v1/articles/{article_id}/comments/",
    "READ_LIST": "GET /api/v1/articles/{article_id}/comments/",
    "UPDATE": "PUT /api/v1/articles/comments/{comment_id}/",
    "DELETE": "DELETE /api/v1/articles/comments/{comment_id}/"
}

# 예제 요청 데이터
sample_requests = {
    "user_signup": {
        "username": "testuser",
        "password": "testpass123",
        "email": "test@example.com",
        "nickname": "테스터",
        "bio": "안녕하세요"
    },
    "article_create": {
        "title": "테스트 게시글",
        "content": "테스트 내용입니다."
    },
    "comment_create": {
        "content": "댓글 내용입니다."
    }
}

print("=" * 50)
print("CRUD API 테스트 준비 완료")
print("=" * 50)
print("\n1. User CRUD")
for action, endpoint in user_endpoints.items():
    print(f"  - {action}: {endpoint}")

print("\n2. Article CRUD")
for action, endpoint in article_endpoints.items():
    print(f"  - {action}: {endpoint}")

print("\n3. Comment CRUD")
for action, endpoint in comment_endpoints.items():
    print(f"  - {action}: {endpoint}")

print("\n" + "=" * 50)
print("테스트 방법:")
print("1. python manage.py runserver")
print("2. python manage.py createsuperuser (테스트 계정 생성)")
print("3. Admin 페이지(/admin)에서 로그인")
print("4. API 테스트 (브라우저 또는 Postman)")
print("=" * 50)