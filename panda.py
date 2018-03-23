import urllib2
wiki="html/html/capitals.htm"
a=open(wiki,'r')
page=a.read()
from bs4 import BeautifulSoup
soup=BeautifulSoup(page)
print soup.prettify()
all_tables=soup.find_all('table')
right_table=soup.find_all('table',class_='wikitable sortable plainrowheaders jquery-tablesorter')
print right_table
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for line in right_table:
	for row in line.findAll("tr"):
		cells=row.findAll('td')
		states=row.findAll('th')
		if len(cells)==6:
			A.append(cells[0].find(text=True))
			B.append(states[0].find(text=True))
			C.append(cells[1].find(text=True))
			D.append(cells[2].find(text=True))
			E.append(cells[3].find(text=True))
			F.append(cells[4].find(text=True))
			G.append(cells[5].find(text=True))

import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
print df
df.to_csv("out.csv", sep='\t', encoding='utf-8')




