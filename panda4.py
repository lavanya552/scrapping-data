import urllib2
wiki="https://en.wikipedia.org/wiki/List_of_Indian_cities_on_rivers"
page=urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page)
print soup.prettify()
all_tables=soup.find_all('table')
right_table=soup.find_all('table',class_='wikitable sortable')
print right_table
A=[]
B=[]
C=[]

for line in right_table:
	for row in line.findAll("tr"):
		cells=row.findAll('td')
		
		if len(cells)==3:
			A.append(cells[0].find(text=True))
			B.append(cells[1].find(text=True))
			C.append(cells[2].find(text=True))
			

import pandas as pd
df=pd.DataFrame(A,columns=['City'])
df['River']=B
df['State']=C

print df
df.to_csv("out3.csv", sep='\t', encoding='utf-8')




