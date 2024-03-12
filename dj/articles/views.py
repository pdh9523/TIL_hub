from django.shortcuts import render

# Create your views here.

# 모든 view 함수는 첫번째 인자로 request 요청 객체를 필수적으로 받는다.
# 매개변수는 항상 request
def index(request):
    '''
    렌더링 과정에 요청 객체가 필요한가보다!
    render(request, 템플릿 경로)
    템플릿 이후의 경로를 상대경로로 작성하면 된다.
    '''
    return render(request, 'articles/index.html')