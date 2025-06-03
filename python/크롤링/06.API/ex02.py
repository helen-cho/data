import requests
import datetime
import os

def getNaver(url, query):
    headers = {
        'X-Naver-Client-Id':'DSISkunI4gxjpwj6Yl6J',
        'X-Naver-Client-Secret':'CxLnF9_VmQ'
    }
    params = {
        'query':query,
        'display':100
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data_json = response.json()
            images = []
            for item in data_json['items']:
                image = item['image']
                print(image)
                images.append(image)
            return images
    except Exception as e:
        print(e)
        print(f'[{datetime.datetime.now()}] Error for URL : {url}')
        return None
    
if __name__ == '__main__':
    query = '노트북'
    url = 'https://openapi.naver.com/v1/search/shop.json'
    images = getNaver(url, query)
    try:
        if not os.path.exists('shop'):
            os.mkdir('shop')
        for index, url in enumerate(images):
            res_image = requests.get(url)
            res_image.raise_for_status()
            with open(f'shop/{index}.jpg', 'wb') as file:
                file.write(res_image.content)
    except Exception as e:
        print('error', e)