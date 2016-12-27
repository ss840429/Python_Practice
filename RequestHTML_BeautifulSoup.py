from bs4 import BeautifulSoup
import urllib

request = urllib.request.urlopen('https://www.cathaybk.com.tw/cathaybk/personal_info07_print.asp')
content = request.read().decode('big5')

soup = BeautifulSoup(''.join(content), "lxml")

print(soup.prettify())  # 標準縮排格式
print("\n")
print(soup.title.string) # Title  
print("\n")
print(soup.p)	# <p> tag
print(soup.a)	# <a> tag
print("\n")

for ps in soup.find_all('p'):	# Find all <p> tags
	print( ps )

for ps in soup.find_all('tr', bgcolor='#FFFFFF'):	# Find all <tr> where bgcolor='#FFFFFF'
	print( ps,'\n' )