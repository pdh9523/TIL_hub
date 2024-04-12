import numpy as np 
import pandas as pd

def file_open_by_numpy () :
    np_arr = np.loadtxt('NFLX.csv', delimiter=",", encoding="cp949", dtype=str)
    return np_arr
# numpy를 통해 파일 열기
arr = file_open_by_numpy()

# pandas를 통해 데이터 프레임 정렬
columns = arr[0] # 컬럼명은 0번째 줄에 있습니다. (변수에 저장)
arr = np.delete(arr, 0, 0) # 저장했으면 데이터만 남게 잘라내고
df = pd.DataFrame(arr, columns = columns) # 컬럼을 컬럼 변수로 해서 프레임을 만듭니다
print(df.loc[:, "Date" : "Close"]) # Date - close 구간 출력