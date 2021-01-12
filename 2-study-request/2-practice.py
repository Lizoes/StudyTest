import requests
import json


HEADER = {
    "content-type": "application/json"
}
DOMAIN = "http://newpaythrough.test.swiftpass.cn"
url = '/schoolpayment/propertypay/billpay'
data = {
    "propOrgId": "220",
    "totalAmount": "1",
    "certNo": "2001",
    "billNoList": "WYZD2020111111401676610004",
    "tierId": "1834",
    "houseNo": "L2001"
}
response = requests.post(url=DOMAIN+url, json=data, verify=False, headers=HEADER)
j = json.dumps(response.json(), indent=4, ensure_ascii=False)
print(j)
