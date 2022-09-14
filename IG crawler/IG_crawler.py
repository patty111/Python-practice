import urllib.request as req
from bs4 import *
import os
import requests
import json
import time
from urllib import parse

baseurl = 'https://www.instagram.com/twioux.0627/'
request = req.Request(baseurl,headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'})
startT = time.time()

with req.urlopen(baseurl) as response: 
	data = response.read().decode('utf-8')
root = BeautifulSoup(data,'html.parser')
print(root)
search = root.find_all('script')

#取得json格式的 image url
links = []
for i in search:
	i = list(i)
	try:
		if len(i[0]) > 5000:
			links.append(i[0])
	except:
		pass

#調整成正確格式 ~~~最重要！！！！！
links[0] = links[0].replace('window._sharedData = ','')
links[0] = links[0].replace(';','')
data = json.loads(links[0])
links.clear()
rdata = data['entry_data']['ProfilePage'][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]
Head = data["entry_data"]["ProfilePage"][0]["graphql"]["user"]['edge_owner_to_timeline_media']

for i in range(len(rdata)):
	links.append(rdata[i]["node"]["display_url"])

#設定 XHR request
nxtpg = Head["page_info"]["has_next_page"]
endcursor = Head["page_info"]["end_cursor"]
ownerId = rdata[0]["node"]["owner"]["id"]

table = {
	"id":ownerId,
	"first":12,
	"after":endcursor
}

#開始跑
while nxtpg:
	text = json.dumps(table)
	url = 'https://www.instagram.com/graphql/query/?query_hash = 2c5d4d8b70cad329c4a6ebe3abb6eedd&variables = ' + parse.quote(text)
	
	with req.urlopen(url) as response:
		data = json.load(response)
		
	data = data['data']['user']['edge_owner_to_timeline_media']
	nodes = data["edges"]
	endcursor = data["page_info"]["end_cursor"]
	nxtpg = data["page_info"]["has_next_page"]
	for i in nodes:
		links.append(i["node"]["display_url"])
		table["after"] = endcursor
# print(len(links))
# print('%.5f'%(time.time()-startT)+' second')

"""
#donload start
#os.mkdir('/Users/user/Desktop/pics test/Taiwan pics')
print('%d pics to download~'%(len(links)))
for i in range(30,400):
	filename = os.path.join('/Users/user/Desktop/pics test/Taiwan pics/pic %s.png'%i)
	req.urlretrieve(links[i-1],filename)
	print('#' + str(i) + ' picture')
print('Finish Download')
"""