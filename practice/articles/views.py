from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

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

@login_required
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
            article = form.save(commit = False)
            article.user = request.user
            article.save()
            return redirect('articles:index')

    else :
        # GET 요청이 들어온 경우, Article 생성할 수 있도록 하기
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('article:index')


def detail(request,pk):
    article = Article.objects.get(pk=pk)
    # READ - 특정 게시글에 작성된 모든 댓글 조회 (Article -> Comment 역참조)
    comments = article.comment_set.all()

    # CREATE - 
    comment_form = CommentForm()

    like_count = len(article.like_users.all())
    
    context = {
        'article' : article,
        'comment_form' : comment_form,
        'comments' : comments,
        'like_count' : like_count,
    }    

    return render(request, 'articles/detail.html', context)

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == "POST": 
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)    
    else :
        return redirect('articles:index')
    
    form = ArticleForm(instance=article)
    
    context = {
        'form' : form,
        'article' : article,
    }
    return render(request, 'articles/update.html', context)

@login_required
def delete(request,pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user :
        article.delete()
    return redirect('articles:index')

@login_required
def create_comments(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all()
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        ## commit : SAVE 하는데, DB에 저장하지 않고 인스턴스만 일단 반환해줌
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article.pk)
    
    context = {
        'article' : article,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def delete_comments(request, article_pk, comment_pk):
    # 어떤 댓글을 삭제할건지 조회
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)


@login_required
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    # if request.user in article.like_users.all():
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else :
        article.like_users.add(request.user)
    

    return redirect('articles:detail', article_pk)
