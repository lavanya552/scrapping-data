import urllib2
wiki="html/html/University.htm"
a=open(wiki,'r')
wiki=a.read()

from bs4 import BeautifulSoup
soup=BeautifulSoup(wiki)
print soup.prettify()
all_tables=soup.find_all('table')
right_table=soup.find_all('table',class_='wikitable sortable collapsible plainrowheaders jquery-tablesorter')
#print right_table
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
for line in right_table:
	for row in line.findAll("tr"):
		uni=row.findAll('th')
		cells=row.findAll('td')
		if (len(cells)==6):
			A.append(uni[0].find(text=True))
			B.append(cells[0].find(text=True))
			C.append(cells[1].find(text=True))
			D.append(cells[2].find(text=True))
			E.append(cells[3].find(text=True))
			F.append(cells[4].find(text=True))
			
			
	

import pandas as pd
df=pd.DataFrame(A,columns=['University'])
df['State']=B
df['Location']=C
df['Section12(B)?']=D
df['Established']=E
df['Specialization']=F
print df
df.to_csv("out2.csv") 




