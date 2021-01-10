import requests


DOMAIN = ""


# 下载并保存文件
download_url = DOMAIN + ""
response = requests.get(download_url)
with open("", mode="wb", encoding="utf-8") as f:
    f.write(response.content)


# 上传文件
upload_url = DOMAIN + ""
fileObj = open("", mode="rb", encoding="utf-8")
upload_data = {
    "fileName": ("fileName", fileObj, "image/jpg")
}
upload_response = requests.post(url=upload_url, files=upload_data, verify=False)

print(5*'=')
