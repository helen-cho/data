import requests
import json
import datetime

def getKakao(url, query, size):
    headers = {
        'authorization':'KakaoAK 7dc21d5852274d162cc3c15163505083'
    }
    try:
        page = 1
        json_list = []
        while True:
            query_url = f'{url}?query={query}&size={size}&page={page}'
            response = requests.request(method='get', url=query_url, headers=headers)
            #응답(response)결과를 JSON 형식으로 파싱한다.
            json_data = response.json()
            #is_end가 True이면 마지막 페이지지
            is_end = json_data['meta']['is_end']
            #is_end가 True이면 반복문을 빠져나간다.
            if bool(is_end):
                break
            else:
                #is_end가 False이면 'documents' 배열을 반복한다.
                documents = json_data['documents']
                for index, item in enumerate(documents):
                    title = item['title']
                    authors = item['authors']
                    price = item['price']
                    #sequence number를 계산한다.
                    seq = (page-1) * size + index + 1
                    print(seq, title, authors, price)
                    #json_list 배열에 item 딕션너리를 추가한다.
                    json_list.append(item)
            #page를 1증가한다.
            page += 1
        #추가한 json_list 배열을 반환한다.
        return json_list
    except Exception as e:
        print(e)
        print(f'[{datetime.datetime.now()}] Error for URL : {url}')
        return None

#해당 파이썬 파일을 직접 실행했을 때만 아래 코드를 실행    
if __name__ == '__main__':
    query = '파이썬'
    size = 10
    url = '	https://dapi.kakao.com/v3/search/book'

    #카카오 검색 함수를 호출한다.
    json_data = getKakao(url, query, size)

    #검색결과를 파일에 저장
    with open(f'data/도서.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)