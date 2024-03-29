from django.db import models

from django.contrib.auth.models import AbstractUser
# 내장 유저 클래스를 import 합니다. 
# 기설정된 유저 클래스는 별도 설정 없이 사용할 수 있어 간편하지만
# 개발자가 직접 수정할 수 없는 문제가 존재합니다.


# AbstratUser 클래스를 상속받는 커스텀 User 클래스를 작성하여
# 커스텀 User 클래스도 기존 User 클래스와 완전히 같은 모습을 가지게 할 수 있습니다.

# 이거는 Django 프로젝트의 User를 나타내는 데 사용하는 모델을 지정하는데
# 프로젝트 중간에 AUTH_USER_MODEL을 변경할 수 없습니다.
# 이미 프로젝트가 진행되고 있을 경우 데이터베이스 초기화 후 진행해야 정상적으로 작동합니다. 
# Django는 새 프로젝트를 시작하는 경우 커스텀 User모델을 설정하는 것을 권장
# 커스텀 User모델은 기본 User 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있다.

# 단, User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 합니다.

class User(AbstractUser):
    pass