from bs4 import BeautifulSoup as BS
import requests
url = "http://thehackernews.com/"

r=requests.get(url)
html = r.text

soup = BS(html,'html.parser')

h2 = soup.find_all('h2',align='justify',class_='post-title url')
for ix in range(len(h2)):
	print ix,h2[ix].find_all('a')[0].getText()
	
