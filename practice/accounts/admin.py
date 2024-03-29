from django.contrib import admin

# admin site에 대체한 User 모델을 등록해야합니다.
# 기본 User 모델이 아니기 때문에 등록하지 않으면 출력되지 않습니다.
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User,UserAdmin)