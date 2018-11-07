# coding:utf-8

import time
import hashlib
import base64
import json

import requests

def send_voice_ChinaMobile(phone_num):

    APIKey = "f7466b97cc6b4ac19ec9f9f498b6a9c4"
    SecretKey = "e30aa0cece454b78b52a41560e37bc62"
    time_unix_13 = str(int(round(time.time() * 1000)))
    sign_string = APIKey + SecretKey + time_unix_13


    m = hashlib.md5()
    m.update(sign_string)
    signStr = m.hexdigest()

    jsonStr = {
        "apiKey": "f7466b97cc6b4ac19ec9f9f498b6a9c4",
        "time": time_unix_13,
        "sign": signStr
    }

    authorization = base64.b64encode(json.dumps(jsonStr))

    payload = {
        "Authorization": authorization,
        "to": str(phone_num),
        "playTimes": 3,
        "templateId": 2,
    }
    api_voice_ChinaMobile = 'http://dev.cmccopen.cn/api/v1/voice/voiceNotify'

    res = requests.post(api_voice_ChinaMobile, data=payload)
    print res.text

if __name__ == '__main__':
    send_voice_ChinaMobile(13051693825)
