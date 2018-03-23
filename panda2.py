import urllib2
wiki="https://en.wikipedia.org/wiki/List_of_current _Indian_chief_ministers"
page=urllib2.urlopen(wiki)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page)
print soup.prettify()
all_tables=soup.find_all('table')
right_table=soup.find_all('table',class_='wikitable sortable plainrowheaders')
print right_table
A=[]
B=[]
C=[]
D=[]
E=[]
for line in right_table:
	for row in line.findAll("tr"):
		cells=row.findAll('td')
		#states=row.findAll('th')
		if len(cells)==5:
			A.append(cells[0].find(text=True))
			B.append(cells[1].find(text=True))
			C.append(cells[2].find(text=True))
			D.append(cells[3].find(text=True))
			E.append(cells[4].find(text=True))
			
		

import pandas as pd
df=pd.DataFrame(A,columns=['Portrait'])
df['Name']=B
df['State']=C
df['Took_office']=D
df['Party']=E
print df
df.to_csv("out1.csv", sep='\t', encoding='utf-8')




