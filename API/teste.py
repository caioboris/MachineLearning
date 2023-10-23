from requests import post

url = 'http://127.0.0.1:5000/predict'

dict_json = {
  "Comprimento do abdômen": "",
  "Comprimento das Antenas": ""
}

r = post(url, json=dict_json)

print(r.json())