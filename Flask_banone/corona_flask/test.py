# test.py

from datetime import date, timedelta
import corona_data

now = date.today() # 오늘은 20211103
now_str = now.strftime("%Y%m%d")
print(now_str)

data = corona_data.get_corona_data(211104,211104)
print(data)

if not data:
    # 어제 날짜로 데이터를 보여줌
    yesterday = now - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y%m%d")
    print(yesterday_str)

    # corona_data.get_corona_data(now_str)