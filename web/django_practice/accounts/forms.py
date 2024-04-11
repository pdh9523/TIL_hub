from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

'''
from .models import User
- 결과는 같은데 직접 참조하는 이유는 ? 

유저 모델 자체가 바뀌거나 수정되는 경우 유저를 직접 참조하는 모든 함수를 교체해야 한다.
그래서, get_user_model() 함수를 통해 유저 객체가 대체되는 경우에도 수정 없이 적용이 가능하다. 
'''

# 빌트인 form을 쓴다고 하더라도, 커스텀이 필요한 경우가 있다. 
# 커스텀 유저 모델을 사용하려면, UserCreationForm 과 UserChangeForm의 User 또한 커스텀 해야한다.

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta) :
        # 현재 django 프로젝트에 활성화된 User 객체를 반환하는 함수
        model = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)