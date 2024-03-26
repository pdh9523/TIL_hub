from django.shortcuts import render, redirect
from .models import Article
# Create your views here.

### Read
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        "article" : article,
    }
    return render(request, 'articles/detail.html', context)


#### create
def new(request):
    return render(request, 'articles/new.html')



def create(request):
    #request.GET == QueryDict
    # title = request.GET.get('title')
    # content = request.GET.get('content')
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 1.
    # 얘는 길다
    # article= Article()
    # article.title = title
    # article.content = content
    ############# 유효성 검증 이후
    # article.save()

    # 2.
    article = Article(title=title, content=content)
    ############# 유효성 검증 이후
    article.save()

    # 3.
    # 이 코드는 유효성 검증에 대한 시간이 없다.
    # Article.objects.create(title=title, content=content)
    return redirect('articles:detail', article.pk)

def delete(request, pk):
    # 몇번 글 삭제할건데..? (조회부터 시작)
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)

def update(request,pk):
    # 몇 번 게시글을 수정할 것인가?
    # 조회가 필요
    article = Article.objects.get(pk=pk)

    title = request.POST.get('title')
    content = request.POST.get('content')
    # 원래 있던 값을 지금 POST하는 값으로 변경
    article.title = title
    article.content = content

    article.save()

    return redirect('articles:detail', article.pk)