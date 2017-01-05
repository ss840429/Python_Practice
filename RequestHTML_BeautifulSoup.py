#	Get currency on website and print formatted data  
#	Also save data into csv file named by date

from bs4 import BeautifulSoup
import requests
import csv
import datetime

request = requests.get('https://www.cathaybk.com.tw/cathaybk/personal_info07_print.asp')
request.encoding = 'big5'

soup = BeautifulSoup(''.join(request.text), "lxml")
#print(request.encoding)

now = datetime.datetime.now().strftime("%Y%m%d")

for ps in soup.find_all('p'):				# Find all <p> tags
	print( ps.find('b').string, end='    ')
	for ps1 in ps('font'):
		print( ps1.string, end='')			# Title
	print('\n')

for ps in soup('tr', bgcolor='#FFFFFF'):	# Find all <tr> where bgcolor='#FFFFFF'
	for index, ps1 in enumerate(ps('td')):
		print( '{:12}'.format(ps1.string.replace(' ', '')), end='\t')
	print()

with open( str(now+'.csv'), 'w', newline='') as csvfile:				# Open csv file named by time
	fieldnames = ['Currency', '幣別', 'Buy', 'Sell']
	writer = csv.writer(csvfile)
	writer.writerow( fieldnames )

	for ps in soup('tr', bgcolor='#FFFFFF'):				# Find all <tr> where bgcolor='#FFFFFF'
		row = ['{:10}'.format(ps1.string.replace(' ', '')) for ps1 in ps('td')]	
		writer.writerow( row )

