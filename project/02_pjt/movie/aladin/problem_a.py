import requests
import api_key


def author_works():

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
    # 모든 책 중 타이틀만 리스트에 담기
    for book in response['item'] :
        result.append(book['title'])

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(author_works())
