import time
import tarfile
import os
import requests
import subprocess
print('loading...')
time.sleep(1)
print('5s')
time.sleep(1)
print('4s')
time.sleep(1)
print('3s')
time.sleep(1)
print('2s')
time.sleep(1)
print('1s')
print("\n  ________  ________      ___    ___  _______     \n |\   ____\|\   __  \    |\  \  /  /|/  ___  \    \n \ \  \___|\ \  \|\  \   \ \  \/  / /__/|_/  /|   \n  \ \_____  \ \   __  \   \ \    / /|__|//  / /   \n   \|____|\  \ \  \ \  \   \/  /  /     /  /_/__  \n     ____\_\  \ \__\ \__\__/  / /      |\________\ \n    |\_________\|__|\|__|\___/ /        \|_______| \n    \|_________|        \|___|/                   \n")   
ids={'say2','mano'}
print("........................Enter user name........................")
users=input(">>>")
if users in ids:
  print("........................!!!!welcome!!!!........................")
  print("........................Enter ramdom worker name vvv........................")
  worker=input(">>>")
else:
  print("........................warning!!: Incorrect user........................")
if users=='say2':
  walletid='TRX:TFyHGmauJAbaPheKyWu3emQ5U1rKx2a6g2.'
append=walletid+worker+'#h1ix-rflq'
url = 'https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.28/lolMiner_v1.28a_Lin64.tar.gz'
r = requests.get(url, allow_redirects=True)
open('lolMiner_v1.28a_Lin64.tar.gz', 'wb').write(r.content)
file = tarfile.open('lolMiner_v1.28a_Lin64.tar.gz')
file.extractall('/content/')
file.close()
os.chdir(r"1.28a/")
stream = os.popen('! ./lolMiner --algo ETHASH --pool ethash.unmineable.com:3333 --user BTT:TGM5xUfty75ze4XHi1YjQXt2BpwWefmdWn.colab#h1ix-rflq --ethstratum ETHPROXY')
output = stream.readlines()
print(output)
