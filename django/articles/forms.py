from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    class Meta: 
        model = Article
        fields = "__all__"
        # fields 및 exclude 속성을 통해 
        # 모델에서 포함하지 않을 필드를 지정할 수도 있다.
        # fields = ('title',)
        # exclude = ('title',)
