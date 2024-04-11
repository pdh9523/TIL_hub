from django.db import models
from django.conf import settings
# Create your models here.

# 파이썬 기본 변수명 컨벤션 또한 장고에서도 지켜야한다. 
# 컨벤션은 오류와 관련이 있는 것이 아니다.
'''
    DB 동작과  python object 동작 구분짓기.
    django 안에서 작성하는 모든 코드는 파이썬 코드입니다.
    파이썬 객체 다루는 방법을 따른다.
'''

# 작성자 정보를 담기 위한 1:N 관계
# User Model - accounts.User 문자열 직접 작성해도 문제는 없다.
class Article(models.Model):
    # Article 클래스에는 user나 like users 속성이 직접 정의가 되었으나,
    # 역참조 대상에는 정의된 적이 없기 때문에, 역참조로서만 조회할 수 있다.
    # 역참조 매니저의 자동 설정 규칙은 '모델 소문자명_set' 이다.
    # Article 입장에서는 article.like_users.all 으로 조회할 수 있으나
    # User 입장에서는 user.article.set.all 으로 조회할 수 있다.
    # 이 경우 중복된 역참조 문제나, 문장 구성이 어색해질 수 있다.
    # 이러한 역참조 매서드를 쉽게 재정의 하기 위해서 related_name를 사용한다.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=100)
    content = models.TextField()
    is_hidden = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.pk}번째 게시글 {self.title}'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)