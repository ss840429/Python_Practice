from bs4 import BeautifulSoup
import requests

request = requests.get('https://www.cathaybk.com.tw/cathaybk/personal_info07_print.asp')
request.encoding = 'big5'

soup = BeautifulSoup(''.join(request.text), "lxml")
#print(request.encoding)


# print(soup.prettify())  # 標準縮排格式
# print("\n")
# print(soup.title.string) # Title  
# print("\n")
# print(soup.p)	# <p> tag
# print(soup.a)	# <a> tag
# print("\n")


for ps in soup.find_all('p'):				# Find all <p> tags
	print( ps.find('b').string, end='    ')
	for ps1 in ps('font'):
		print( ps1.string, end='')			# Title
	print('\n')

for ps in soup('tr', bgcolor='#FFFFFF'):	# Find all <tr> where bgcolor='#FFFFFF'
	for index, ps1 in enumerate(ps('td')):
		print( '{:10}'.format(ps1.string.replace(' ', '')), end='\t')
	print()



