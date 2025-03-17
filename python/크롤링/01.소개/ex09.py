import requests

try:
    url = 'http://google.com/user'
    res = requests.get(url)
    print(res)
    if res.status_code == requests.codes.ok: #코드 200
        print(f'연결성공입니다. [코드:{res.status_code}]')
    else:
        print(f'연결실패입니다. [코드:{res.status_code}]')

    #만약 에러가 있다면 멈춰주고 에러를 알려 준다
    res.raise_for_status()

    url = 'http://google.com'
    res = requests.get(url)
    print(res)
    if res.status_code == requests.codes.ok: #코드 200
        print(f'연결성공입니다. [코드:{res.status_code}]')
    else:
        print(f'연결실패입니다. [코드:{res.status_code}]')
except requests.HTTPError as err:
    print(f'에러:{err}')
    