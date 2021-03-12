import requests
import re

username='username'
password='password'


payload = {'username': username, 'password': password}
url='https://ogero.gov.lb/myogero/login.p.php'

with requests.Session() as sess:
    sess.post(url, data=payload)
    index=sess.get('https://ogero.gov.lb/myogero/index.php')
    txt=index.text

    gb=re.findall('[0-9]+\.[0-9]+ GB.*GB',txt)
    if(len(gb)==1):    
        print(gb[0])
    else:
        print('error')


input()
