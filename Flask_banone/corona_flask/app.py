# app.py

from flask import Flask
from flask.templating import render_template

from datetime import date, timedelta
import corona_data


# 앱 생성
app = Flask(__name__)

# url 라우터
@app.route('/')
def index():

    now = date.today() # 오늘은 20211103
    now_str = now.strftime("%Y%m%d")
    print(now_str)

    # 오늘 날짜로 요청해라
    data = corona_data.get_corona_data(now_str, now_str)
    print(data)

    # 없으면 어제 날짜로 요청해라
    if not data:
        yesterday = now - timedelta(days=1)
        yesterday_str = yesterday.strftime("%Y%m%d")
        print(yesterday_str)

        data = corona_data.get_corona_data(yesterday_str, yesterday_str)
        print(data)

    return render_template('index.html', data=data)

# 메인 영역
if __name__ == "__main__":
    app.run(debug=True)