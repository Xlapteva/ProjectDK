from django.conf import settings
from pprint import pprint
import json
import requests


"""
структура запроса от такая д.б.

A = input1
B = input2
C = input3
D = input4

reportdata = {'key1':'value1', 'key2':['value2', 'value3']}
requests.get('здесь url', params=reportdata/verify=False)
print(r.url)

_________________________

def get_data_from_api():
r = requests.get(https://api.dzdata.affise.com/3.0/stats/custom?slice%5B%5D=offer&filter%5Bdate_from%5D=A&filter%5Bdate_to%5D=B&filter%5Badvertiser%5D=5b2a22d373bdda49008b4604&API-key=API_KEY; params=)
r = requests.get(https://api.dzdata.affise.com/3.0/stats/custom?slice%5B%5D=offer&filter%5Bdate_from%5D=C&filter%5Bdate_to%5D=D&filter%5Badvertiser%5D=5b2a22d373bdda49008b4604&API-key=API_KEY; params=)

В A,B,C,D - даты введенные через интерфейс нужно подставлять

http://docs.python-requests.org/en/master/user/quickstart/#passing-parameters-in-urls - ссылочка на описание

Список Advertisers:
https://api.dzdata.affise.com/3.0/admin/advertisers?API-key=API_KEY

Список Publisher (Affiliate):
https://api.dzdata.affise.com/3.0/admin/partners?API-key=API_KEY

https://docs.google.com/spreadsheets/d/1N9eVQ8eds9HC6AQP5CcJaULLaB3u5tJt2QxlpzG8_0M/edit?ts=5c14d0fd#gid=0 - структура отчета, который мы ваяем

"""
r = requests.get(
    'https://api.dzdata.affise.com/3.0/stats/custom?slice%5B%5D=offer&filter%5Bdate_from%5D=2018-10-01&filter%5Bdate_to%5D=2018-10-02&filter%5Badvertiser%5D=5b2a22d373bdda49008b4604&API-key=37796ce6525a581c56a493ccd39402eadca187de', 
    verify=False
)

data = json.loads(r.content) # делаем массив из того, что вернулось в ответе
pprint(data)






