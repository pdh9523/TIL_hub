import requests
from pprint import pprint
import api_key

def ebook_list(title):
    
    ttbkey = api_key.ttbkey
    QueryType = "Keyword"
    MaxResults = 20
    start = 1
    SearchTarget = 'eBook'
    output = 'js'
    Version = 20131101

    # 검색어
    Query = title

    URL = f'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={Query}&QueryType={QueryType}&MaxResults={MaxResults}&start={start}&SearchTarget={SearchTarget}&output={output}&Version={Version}'
    response = requests.get(URL).json()

    # *을 넣으면 값이 없어 IndexError가 발생. 예외처리
    result = {}
    try :
        if response['item'][0]['subInfo']['paperBookList'][0]['priceSales'] * 0.9 > response['item'][0]['priceSales'] :
            result['itemId']=(response['item'][0]['itemId'])
            result['isbn']=(response['item'][0]['isbn'])
            result['priceSales']=(response['item'][0]['priceSales'])
            result['link']=(response['item'][0]['link'])
        return result
    except IndexError :
        return None
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(ebook_list('베니스의 상인'))

    pprint(ebook_list('*'))
