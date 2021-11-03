# app.py

import re
from flask import Flask, render_template, request
import google_keyword


# Flask 앱 서버 인스턴스
app = Flask(__name__)

# url 패턴 - 라우터 설정 - decorater
@app.route('/')
def index():
    # get 을 통한 전달받은 데이터를 확인 
    key1 = request.args.get('keyword1')
    key2 = request.args.get('keyword2')
    print(key1, key2)

    if not key1 or not key2: # key == 빈문자열 == False
        return render_template('index.html')
    else:
        # 모듈(google_keyword)로 키워드 개수 가져오기
        value1 = google_keyword.get_keyword_number(key1)
        value2 = google_keyword.get_keyword_number(key2)

        # 사용자 보낼 데이터
        data = {key1: value1, key2: value2}

        return render_template('index.html', data=data)

# 메인 테스트
if __name__ == "__main__":
    app.run(debug=True)

