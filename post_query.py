import requests
from config import username, password

url = 'http://forum-wec.com/index.php'
data = {
        'UserName': username,
        'PassWord': password,
        'x': '21',
        'y': '13'
        }

session = requests.session()
session.headers = 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
response = session.post(url, data)

print(response.text)