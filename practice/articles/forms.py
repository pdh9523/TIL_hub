from django import forms
from .models import Article
'''
    Form : 모델에 대한 정보가 없는 Form을 위한 클래스

    ModelForm : 모델에 대한 정보가 있는 Form을 위한 클래스
'''
class ArticleForm(forms.ModelForm):
    '''
        HTML에서 쓸 form 태그를 구성해주는 class인데,
        field에 대한 정보가 없으면 input tag에 뭘 써야할지 알 수 없다.
        그래서, 그 field를 직접 짜준다. 정의하는 방법은 django model 정의하는 것과 똑같다.
    '''

    title = forms.CharField(
        # form 내부에서 보여줄 input을 어떻게 정의할 것인가?
        # 어떤 input으로 만들어 주는지는 누가 가지고 있는가?
        # html 태그는 여러개의 속성을 가지고 있는데, 이 속성을 쓰는 방법은 "속성명=값"방식이다.
        widget = forms.TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder' : '제목을 입력하세요.',
            }
        )
    )
    content = forms.CharField(
        widget = forms.Textarea(
            attrs= {
                'class' : 'form-control',
                'placeholder' : '내용을 입력하세요.',
            }
        )
    )
    class Meta:
        model = Article
        fields = '__all__'
        '''
            내가 가진 필드들 중 어떤 이름을 가진 필드들의 속성만 간단하게 수정하고 싶어.
            필드 각 이름은 고유값이니까, 
        '''
        widgets = {
            'is_hidden' : forms.RadioSelect(
                attrs={
                    'class' : 'form-check',
                },
                choices=((True, '공개'), (False, '비공개')
                         
                ),
            )


        }