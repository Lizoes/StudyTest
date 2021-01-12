import requests
import json


HEADER = {
    "content-type": "application/json"
}
DOMAIN = "http://newpaythrough.test.swiftpass.cn"
url = '/schoolpayment/pay/property/qrypaybill'
data = {
    "propOrgId": 220,
    "certNo": "2001",
    "houseUname": "林2001",
    "qryBillFlag'": 1,
}
# verify: False 支持http
response = requests.post(url=DOMAIN+url, json=data, verify=False, headers=HEADER)


j = json.dumps(response.json(), indent=4, ensure_ascii=False)
print(j)


"""
 data为参数，Content-Type为：application/x-www-form-urlencoded，后端拿到的数据为b'username=amy&password=123'
 json为参数，Content-Type为：application/json,自动调用dumps函数转换成json对象，后端拿到的数据为b'{"username": "amy", "password": "123"}'
"""