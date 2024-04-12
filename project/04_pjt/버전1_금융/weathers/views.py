from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from io import BytesIO
import base64

# Create your views here.
def index(request):
    return render(request, 'weathers/index.html')


def problem1(request):
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path, encoding="cp949")

    # df = df.drop(df.columns[0], axis=1)

    context = {
        'df': df.to_html(classes='table table-striped', index=False)
    }
    return render(request, 'weathers/problem1.html', context)


def problem2(request):
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path, encoding="cp949")

    x = pd.to_datetime(df["Date"])
    label_name = ['', 'High Temperature', 'Average Temperature', 'Low Temperature']
    for i in range(1, 4):
        plt.plot(x, df.iloc[:, i], label=label_name[i])

    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.legend(loc='lower center')
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()

    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    context = {
        'image' : f'data:image/png;base64, {img_base64}'
    }

    return render(request, 'weathers/problem2.html', context)


def problem3(request):
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path, encoding="cp949")

    # 'Date' 열을 datetime 형식으로 변환
    df['Date'] = pd.to_datetime(df['Date'])

    # 월별로 데이터를 그룹화하고 평균을 계산
    monthly_avg = df.groupby(df['Date'].dt.to_period('M')).agg({'TempHighF': 'mean', 'TempAvgF': 'mean', 'TempLowF': 'mean'})

    # Matploblib을 사용하여 그래프 그리기
    # x = pd.to_datetime(monthly_avg.index, format='%m')
    x = monthly_avg.index.to_timestamp()
    label_name = ['High Temperature', 'Average Temperature', 'Low Temperature']
    for i in range(3):
        plt.plot(x, monthly_avg.iloc[:, i], label=label_name[i])

    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.legend(loc='lower right')
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()

    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    context = {
        'image' : f'data:image/png;base64, {img_base64}'
    }

    return render(request, 'weathers/problem3.html', context)



def problem4(request):
    csv_path = 'austin_weather.csv'
    df = pd.read_csv(csv_path, encoding="cp949")

    df['Events'].fillna('None', inplace=True)
    events_list = df['Events'].str.split(',').tolist()

    # all_events = [event.strip() for sublist in events_list for event in sublist]
    all_events = [event.strip() if event.strip() != '' else 'No events' for sublist in events_list for event in sublist]

    event_counts = pd.Series(all_events).value_counts()

    # event_counts['No Events'] = event_counts.pop('None')

    plt.figure(figsize=(10, 6))
    event_counts.plot(kind='bar')

    # plt.bar(events, counts)

    plt.title('Event Counts')
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.xticks(rotation=0)

    
    plt.grid(True)

    plt.tight_layout()
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()

    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    context = {
        'image' : f'data:image/png;base64, {img_base64}'
    }
    
    return render(request, 'weathers/problem4.html', context)