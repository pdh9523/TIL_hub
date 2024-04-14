import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django.shortcuts import render,redirect


from .forms import KeywordForm
from .models import Keyword, Trend

# Create your views here.

def keyword(request):
    if request.method == "POST":
        form = KeywordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trends:keyword')

    form = KeywordForm()
    keywords = Keyword.objects.all()

    context = {
        'form' : form,
        'keywords' : keywords,
    }
    return render (request, 'trends/keyword.html', context)

def delete(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')


def crawling(request):
    keywords = Keyword.objects.all()
    
    for keyword in keywords :
        name = keyword.name
        url = f'https://www.google.com/search?q={name}'

        driver = webdriver.Chrome()
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        lst = soup.select_one('div#result-stats')
        if lst.text:
            num = int(lst.text.split()[2][:-1].replace(",", ""))
        try:
            trend = Trend.objects.get(name=name, search_period="all")
            # 해당 객체가 존재한다면 result 값을 업데이트
            trend.result = num
            trend.save()  # 업데이트된 값을 저장
        except Trend.DoesNotExist:
            # 해당 객체가 존재하지 않으면 새로 생성
            Trend.objects.create(name=name, result=num, search_period='all')
    
    trends = Trend.objects.all()

    context = {
        'trends' : trends,
        'keywords' : keywords,
    }
    return render(request, 'trends/crawling.html', context)

def crawling_histogram(request):
    trends = Trend.objects.filter(search_period='all')
    trends_data = trends.values('name', 'result')
    df = pd.DataFrame(trends_data)

    plt.bar(df['name'],df['result'])
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.title('Search Results by Keyword')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    
    context = {
        'image' : f'data:image/png;base64, {image_base64}'
    }
    return render(request, 'trends/crawling_histogram.html', context)

def crawling_advanced(request):
    keywords = Keyword.objects.all()
    
    for keyword in keywords :
        name = keyword.name
        url = f'https://www.google.com/search?q={name}&tbs=qdr:y'

        driver = webdriver.Chrome()
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        lst = soup.select_one('div#result-stats')
        if lst.text:
            num = int(lst.text.split()[2][:-1].replace(",", ""))
        try:
            trend = Trend.objects.get(name=name, search_period="year")
            # 해당 객체가 존재한다면 result 값을 업데이트
            trend.result = num
            trend.save()  # 업데이트된 값을 저장
        except Trend.DoesNotExist:
            # 해당 객체가 존재하지 않으면 새로 생성
            Trend.objects.create(name=name, result=num, search_period='year')
    
    # 그래프 생성

    trends = Trend.objects.filter(search_period = 'year')
    trends_data = trends.values('name', 'result')
    df = pd.DataFrame(trends_data)

    plt.bar(df['name'],df['result'])
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.title('Search Results by Keyword')
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    
    context = {
        'image' : f'data:image/png;base64, {image_base64}'
    }
    return render(request, 'trends/crawling_advanced.html', context)