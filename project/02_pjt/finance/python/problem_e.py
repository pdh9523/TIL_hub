import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

def file_open_by_numpy () :
    np_arr = np.loadtxt('NFLX.csv', delimiter=",", encoding="cp949", dtype=str)
    return np_arr
# numpy를 통해 파일 열기
arr = file_open_by_numpy()

# pandas를 통해 데이터 프레임 정렬
columns = arr[0] # 컬럼명은 0번째 줄에 있습니다. (변수에 저장)
arr = np.delete(arr, 0, 0) # 저장했으면 데이터만 남게 잘라내고
df = pd.DataFrame(arr, columns = columns) # 컬럼을 컬럼 변수로 해서 프레임을 만듭니다
df["Date"] = pd.to_datetime(df["Date"]) # Date의 type을 datetime으로 변경
df = df.query("Date >= '2022-01-01'") # Date를 2022-01-01 이상으로 필터링
df["Close"] = df["Close"].astype(float) # y축들의 type을 float으로 변경
df["High"] = df["High"].astype(float) 
df["Low"] = df["Low"].astype(float) 

x = df["Date"]
y1 = df["Close"]
y2 = df["High"]
y3 = df["Low"]

plt.plot(x, y1, label= "Close")
plt.plot(x, y2, label= "High")
plt.plot(x, y3, label= "Low")

plt.legend()

plt.title("High, Low, And Close Prices since January 2022")
plt.xlabel("Date")
plt.ylabel("Price")

plt.show()