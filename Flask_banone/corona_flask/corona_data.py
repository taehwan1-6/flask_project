# corona_data.py

import requests
import xmltodict
import json
from pprint import pprint

def get_corona_data(startCreateDt, endCreateDt):
    url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"
    params = {
        'ServiceKey': 'Yox4quwxHE8v9TM6BNSfnwGiwLD6VJLG49kZDdrLztHSxGtgs94ZzVjtoxRHC9PqUsGohO+qzoE7PsF8TRkYOA==',
        'pageNo': '1',
        'numOfRows': '10',
        'startCreateDt': startCreateDt, #'20211103',
        'endCreateDt': endCreateDt, #'20211103',
    }

    # xml데이터를 받아옴
    res = requests.get(url, params=params)
    # print(res.url)
    # print(res.text)


    # xml to dict
    dict_data = xmltodict.parse(res.text)


    # dict to json
    json_data = json.dumps(dict_data)


    # json to dict
    dict_data = json.loads(json_data)
    # pprint(dict_data)

    # totalCount로 제대로 데이터가 가져와졌는지 확인하기
    totalCount = dict_data['response']['body']['totalCount']
    if totalCount == '0':
        return False

    # 지역 정보를 담은 리스트
    area_data = dict_data['response']['body']['items']['item']
    area_data.reverse()
    
    return area_data

    
