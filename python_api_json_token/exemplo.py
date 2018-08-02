import requests

data = dict(
    placa='IHF0716',
    data_hora='2018-08-01 17:11:00'
)

token = 'xxxxxxxxxxxxxxxxxxxxxx'
headers={'Authorization': 'token {}'.format(token)}

url = 'https://glatesat.herokuapp.com/api_odometro/'
r = requests.post(url, json=data, headers=headers)

print(r, r.content)
