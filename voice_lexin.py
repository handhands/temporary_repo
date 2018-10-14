# coding:utf-8

import requests

def send_voice_lexin(phone_num, alarm_type, product_id = 1012838, template_id = 126179):
    """

    :param phone_num: 电话号码 ，输入数字就行
    :param alarm_type: 警报类型，字符串类型
    :param product_id: 产品ID，数字，在乐信后台管理能看到，1012838对应行业智能语音，这个一般固定不用改
    :param template_id: 模板ID，数字，新增模板需要联系客服，从客服那拿到模板号才能正常使用
                        126179对应于：您有一条新的#alarm_type#信息，请注意查看。
    发送信息内容格式为：126179;q:             冒号后接变量
    :return:
    """
    api_voice_lexin = 'http://api.51welink.com/json/sms/g_Submit'
    msg_text = str(template_id) + ";q:" + str(alarm_type)
    payload = {
        "sname": "dlbaixf",
        "spwd": "",
        "scorpid": "",
        "sprdid": str(product_id),
        "sdst": str(phone_num),
        "smsg": msg_text
    }

    res = requests.post(api_voice_lexin, data=payload)
    print res.text

if __name__ == '__main__':
    send_voice_lexin(15671641556, "设备故障")
