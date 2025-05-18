import os
import sys
os.system("clear")
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip uninstall pycurl -y && pip install pycurl')
os.system("clear")
try:os.system("git pull")
print("error")