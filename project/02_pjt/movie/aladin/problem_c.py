import requests
from pprint import pprint
import api_key

def bestseller_book():

    ttbkey = api_key.ttbkey
    QueryType = "Author"
    MaxResults = 20
    start = 1
    SearchTarget = 'Book'
    output = 'js'
    Version = 20131101

    # 검색어
    Query = '파울로 코엘료'

    URL = f'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={Query}&QueryType={QueryType}&MaxResults={MaxResults}&start={start}&SearchTarget={SearchTarget}&output={output}&Version={Version}'
    response = requests.get(URL).json()
    

    # sort의 key를 설정해 내림차순으로 설정
    response['item'].sort(key=lambda x : x['salesPoint'], reverse=True)

    # 5개만 받아서 리스트에 담기
    result = []
    for i in range(5) :
        result.append(response['item'][i]['title'])
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(bestseller_book())
