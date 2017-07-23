# -*- coding: utf-8 -*-
import requests
import re
import os

client_id = os.getenv('PAPAGO_CLIENT_ID', None)
client_secret = os.getenv('PAPAGO_CLIENT_SECRET', None)

url = "https://openapi.naver.com/v1/language/translate"

headers = {'X-Naver-Client-Id': client_id,
           'X-Naver-Client-Secret': client_secret}

# http://jokergt.tistory.com/52
def isKorean(text):
    hangul = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')  # 위와 동일
    result = hangul.findall(text)
    return len(result)

def translate(text):
    if isKorean(text):
        return _translate(text, 'ko', 'en')
    else:
        return _translate(text, 'en', 'ko')

def _translate(text, source='en', target='ko'):
    # text = '안녕하세요. 파파고 입니다.'
    data = {'source': source,
            'target': target,
            'text': text}

    response = requests.post(url, data=data, headers=headers)
    res_code = response.status_code

    if res_code is not 200:
        print("Error Code:" + str(res_code))
        return 'Cannot translate'

    json = response.json()

    return json['message']['result']['translatedText']

if __name__ == "__main__":
    print(translate("Hello World!"))
    print(translate("아름다운 세상입니다."))