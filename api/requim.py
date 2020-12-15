import requests
import pprint
import xml.etree.ElementTree as ET
import codecs
r=requests.get('http://yahoo.com')
print(r.text)
'''
api_url='http://web.kma.go.kr/wid/queryDFSRR.jsp?zone=1159068000'
weather_data=requests.get(api_url).text
pprint.pprint(weather_data)


url='http://web.kma.go.kr/wid/queryDFSRR.jsp'
payload={'zone':'1159068000'}
weather_data=requests.get(url,payload).text
#pprint.pprint(weather_data)

xml_data = ET.fromstring(weather_data)
for tag in xml_data.iter("data"):
    print (tag.find("hour").text + "/" + tag.find("temp").text)
'''

api_url = 'http://en.wikipedia.org/w/api.php'
api_params={'format':'xmlfm', 'action':'query','titles':'Jack Bauer', 'prop':'revisions', 'rvprop':'content'}
wiki_data=requests.get(api_url,params=api_params)
#pprint.pprint(wiki_data)
fo=open('./class/wiki.html','w')
fo.write(wiki_data.text)
fo.close()