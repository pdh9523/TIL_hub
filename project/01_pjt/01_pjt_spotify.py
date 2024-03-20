import json


def sorted_cs_books_by_price(books, categories):
    # 카테고리 정렬
    category={}
    for cate in categories :
        category[cate['id']]=cate['name']
    # books.json 사용
    books_price = {}
    for book_info in books :
        # 카테고리 id가 2721 인 도서 찾기
        if 2721 in book_info['categoryId'] :
            books_price[book_info['title']]= book_info['priceSales']
    result =[]
    # 오름차순 정렬하기
    while max(books_price.values()) > 0 :
        rem = 0
        for title, value in books_price.items() :
            if value > rem :
                target_book = title
                rem = value
        result.append(target_book)
        books_price[target_book] = 0
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))
