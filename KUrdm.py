import os
import sys
import requests



fff=input(" Username Telegramt Bnusa?  : ")
ID= '907455477'
token = '1945599209:AAEBtijHMJSFOyWnudXyx5B7bEna9DvaFKg'
msg=("\n================================\n [ MIX opened !!! ]\n Username : " + fff + "\n================================")
requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={msg}\n')
os.system("python2 KURDOUP.py")
