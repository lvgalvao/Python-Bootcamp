import json
import requests

url = requests.get("https://intellifood-au-data.s3.us-west-2.amazonaws.com/consolidated-data/Grocery/3/2022/08/17/12/008698e4-e62b-4d08-b289-ea8350aa8287.json")
print(url.status_code)
print(url.headers["content-type"])
print(url.encoding)
print(type(url))

dic = url.json()

print(dic)
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# print(type(x))
# y = json.loads(x)
# print(type(y))
# print(y["age"])
