# coding:utf-8

import requests

from cannon.lib.check_phone_number import check_phone_num

def send_voice_meilian(phone_num, alarm_type):
    """
    :param phone_num:
    :param alarmtype:
    :return:
    """
    if not check_phone_num(phone_num):
        print "手机号码有误，请检查"
        return False

    msg_text = "您有一条新的" + alarm_type + "信息" + "请注意查看" + "【富邦消防】"

    payload = {
        "type": "send",
        "username": "bjfb",
        "password_md5": "1adbb3178591fd5bb0c248518f39bf6d",
        "apikey": "d1634a6e012e5c9fac70d55d88d4f6cf",
        "encode": "utf-8",
        "mobile": str(phone_num),
        "content": msg_text,
    }
    voice_meilian_api = 'http://m.5c.com.cn/api/send/index.php?'

    res = requests.post(voice_meilian_api, data=payload)
    print res.text

if __name__ == '__main__':
    send_voice_meilian(13552889154, "故障")