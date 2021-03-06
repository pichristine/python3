import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import urllib

#the website that you wanna crawl for pdfs
url = "http://tehetseg.inf.elte.hu/szakkorefop2017/pdf/"
folder_location = r'C:\Users\PK\Desktop\crawledPdfs'
if not os.path.exists(folder_location):os.mkdir(folder_location)


response = requests.get(url).text
soup = BeautifulSoup(response,"html.parser")
for link in soup.select("a[href$='.pdf']"):
	filename = os.path.join(folder_location,link['href'].split('/')[-1])
	with open(filename,'wb')as f:
		f.write(requests.get(urljoin(url,link['href'])).content)