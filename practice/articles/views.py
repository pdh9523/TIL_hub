from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article
# Create your views here.
def index(request):
    # articles = Article.objects.order_by('-pk')
    is_hidden = request.GET.get('is_hidden')
    if is_hidden == None or is_hidden == "True" :
        articles = Article.objects.order_by('pk')
    else : 
        articles = Article.objects.filter(is_hidden = False)

    context= {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def create(request):

    '''
        1. 생성 하기 위한 데이터를 입력할 수 있는 페이지
        2. 입력한 데이터를 토대로 실제로 데이터를 생성하는 함수    
    '''
    if request.method == 'POST' :
        form = ArticleForm(request.POST)
        # 상속 받은 Model Form 에 정의되어 있다.
        # 유효성 메서드 통과 : DB에 저장할 수 있을 것 같음
        # 항상 모든 필드에 대한 정보를 받는건 아니고
        # 사용자가 보내온 데이터가 정의된 field에 삽입하기 적절하면 저장한다.
        if form.is_valid():
            form.save()
            return redirect('articles:index')

    else :
        # GET 요청이 들어온 경우, Article 생성할 수 있도록 하기
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)