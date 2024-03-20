import pprint
import requests
from api_key import api_key


def get_deposit_products():
    # url 설정 (정기 예금 API)
    url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1"
    
    full_data = requests.get(url).json()['result'] # full_data = 'result' key
    base_list = full_data['baseList'] # base_list = 'result''baseList' key
    # optionList 정리
    option_list = []
    for inner_dict in full_data["optionList"] :
        # 임시 딕셔너리 rem 설정 / 초기화
        rem = {}
        rem["금융상품코드"]=inner_dict["fin_prdt_cd"] #이걸로 같은지 비교
        rem["저축 금리"]=inner_dict["intr_rate"]
        rem["저축 기간"]=inner_dict["save_trm"]
        rem["저축금리유형"]=inner_dict["intr_rate_type"]
        rem["저축금리유형명"]=inner_dict["intr_rate_type_nm"]
        rem["최고 우대금리"]=inner_dict["intr_rate2"]
        # optionList에 rem 추가
        option_list.append(rem)
    
    test_list=[]
    for inner_dict in option_list :
        test_list.append(inner_dict["금융상품코드"]) #금융상품코드를 모두 취합
    key_set = set(test_list) #집합으로 중복제거

    result = []
    for key in key_set : # 각 키값에서
        #base_list 처리 구문 
        for base_key in base_list : 
            if base_key["fin_prdt_cd"] == key :
                bank = base_key["kor_co_nm"]
                name = base_key["fin_prdt_nm"]
        sub_dict={}
        sub_result=[]
        for test_dict in option_list : #그리고 옵션리스트에의 각 딕셔너리에서
            if key == test_dict["금융상품코드"] : # 금융상품 코드를 돌면서 키값이 같은걸 찾기
                #키값이 같으면?
                rem = {} #rem에 담아넣자
                rem["저축 금리"] = test_dict["저축 금리"]
                rem["저축 기간"] = test_dict["저축 기간"]
                rem["저축금리유형"] = test_dict["저축금리유형"]
                rem["저축금리유형명"] = test_dict["저축금리유형명"]
                rem["최고 우대금리"] = test_dict["최고 우대금리"]
                sub_result.append(rem) #rem에 다 넣고
            sub_dict["금리정보"] = sub_result # 그 외 정보 base_list에서 가져와서 입력
            sub_dict["금융상품명"] = name 
            sub_dict["금융회사명"] = bank
        result.append(sub_dict)
    return result


if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)