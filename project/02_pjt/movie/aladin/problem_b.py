import requests
import api_key
from pprint import pprint

    # 여기에 코드를 작성합니다.

def best_review_books():

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
    result = []

    # 결과물 중 9점 이상만 result 리스트에 담기
    for book in response['item'] :
        if book['customerReviewRank'] >= 9 :
            result.append(book)

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(best_review_books())
