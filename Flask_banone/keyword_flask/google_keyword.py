# googel_keyword.py

from bs4 import BeautifulSoup
import requests


def get_keyword_number(keyword):
    # keyword = "나루토"
    url = 'https://www.google.com/search?q={}&hl=en'.format(keyword)
    headers = {
        'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }

    # 웹 요청
    res = requests.get(url, headers=headers)
    # print(res.text)


    # 구문 분석 - 파싱
    soup = BeautifulSoup(res.text, 'lxml')
    # print(type(soup))


    # 원하는 것 추출(검색결과 갯수)
    number = soup.select_one('#result-stats').text
    # print(number)


    # 정리
    # number = int(number[number.find('약')+2 : number.rfind('개')].replace(',', ''))
    number = int(number[number.find('About')+6 : number.rfind('result')-1].replace(',', ''))
    # print(number)

    return number

# 테스트 코드
if __name__ == "__main__":
    pass
    # print(get_keyword_number("침책맨"))