import requests as r
import time as t
import sys

theme = ['light', 'dark']

token = input('token: ')
delay = input('delay (seconds): ')

while True:
    for x in theme:
        headers = {
            'Authorization': token,
            'Content-type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        }

        json = {
            'theme': x  
        }

        res = r.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=json)
        if res.status_code != 200:
            print(str(res.status_code) + ' - ' + 'an error has occured, maybe try again with a new token?')
            t.sleep(int(delay))
            sys.exit('ended script')
        print(str(res.status_code) + ' - ' + x)
        t.sleep(int(delay))
