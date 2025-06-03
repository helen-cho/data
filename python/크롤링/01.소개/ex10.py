import requests
res = requests.get('http://google.com')

if res.status_code == requests.codes.ok:
    print(f'연결성공입니다. [코드:{res.status_code}]')

#오류인 경우 프로그램을 종료한다.
res.raise_for_status()

result = res.text

#res의 결과 글자 수를 출력한다.
print(f'검색글자수:{len(result)}')

#res의 결과를 파일로 출력한다.
with open('data/result.html', 'w', encoding='utf-8') as file:
    file.write(result)
    file.write(result)