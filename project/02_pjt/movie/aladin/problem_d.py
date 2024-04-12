import requests
from pprint import pprint
import api_key

def author_other_works(title):
    
    ttbkey = api_key.ttbkey
    QueryType = "Keyword"
    MaxResults = 20
    start = 1
    SearchTarget = 'Book'
    output = 'js'
    Version = 20131101

    # 검색어
    Query = title

    URL = f'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={Query}&QueryType={QueryType}&MaxResults={MaxResults}&start={start}&SearchTarget={SearchTarget}&output={output}&Version={Version}'
    response = requests.get(URL).json()

    try : 
        author_name = response['item'][0]['author']
        if "(" in author_name :
            rem_list = response['item'][0]['author'].split("(")
            target = rem_list[0].strip()
        else :
            target = author_name
    except IndexError :
        return None
    
    # 검색 방법 변경
    # author name 검색어로 변경
    Query = target
    QueryType = "Author"
    response = requests.get(URL).json()

    result = []
    # 모든 책 중 타이틀만 리스트에 담기
    i = 0
    while len(result) < 5 : # 5권만
        book = response['item'][i]['title']
        # 겹치는 책 넘기기
        if book in result : 
            i +=1
        else :
            result.append(book)
    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(author_other_works('베니스의 상인'))

    pprint(author_other_works('개미'))

    pprint(author_other_works('*'))
