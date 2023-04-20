from bs4 import *
import pandas as pd
import json
import csv
import re
import time
import importlib

# Check if selenium is installed
try:
    print("Checking Requirments...")
    importlib.import_module('selenium')
    print('selenium is already installed')
except ImportError:
    print('selenium is not installed, installing now...')
    import subprocess
    subprocess.check_call(['pip', 'install', 'selenium'])
    print('selenium has been installed')


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


baseurl = "https://www.winentaste.com/collections/"
wine_type_id = ['36', '39', '40', '41', '42', '43', '769', '278', '884']

driver = webdriver.Chrome('./chromedriver') 

# clear all
with open('out.csv', 'w', encoding='utf-8') as f:
    f.write('')

for i in wine_type_id:
    url = baseurl + i

    driver.get(url) 
    print("Connecting to", url, "...")

    html = driver.page_source

    # find dynamic html data
    pattern = "</a></div><p><a href=\"/products/" + r"\d+" "\">" + r".{0,50}" + "</a></p>"
    result = re.findall(pattern, html)

    
    with open('out.csv', 'a', encoding='utf-8') as f:
        fieldnames = ['編號','名稱']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()


        # find title and write in csv
        pattern = "<title>" + r".{0,50}" + "</title>"
        idx = 1
        writer.writerow({'編號' : '-','名稱': '-'})
        writer.writerow({'編號' : 0,'名稱': re.search(pattern, html).group().replace("<title>","").replace("</title>", "").replace("&amp;", "").replace("精選好酒商城｜WINETASTE 品迷網", "")})
        
        for j in result:
            tmp = re.sub(r'[^\u4e00-\u9fff]+', '', j)
            writer.writerow({'編號': idx, '名稱': tmp})
            idx += 1




# print csv content
data_HW3csv = pd.read_csv("out.csv",index_col=0)
print(data_HW3csv)



# write in json , csv file and output
with open('out.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)
with open('out.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(rows, jsonfile, ensure_ascii=False, indent=2)
    
outjson = open('out.json',encoding="utf8")

data1_out_json=json.load(outjson)
print(data1_out_json)