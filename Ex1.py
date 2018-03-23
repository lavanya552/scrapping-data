import csv
import urllib2
wiki="html/html/chief.htm"
#page=urllib2.urlopen(wiki)
a=open(wiki,'r')
wiki=a.read()
from bs4 import BeautifulSoup
soup=BeautifulSoup(wiki,'lxml')
all_tables=soup.find_all('table')
right_table=soup.find_all('table',class_='sortable wikitable jquery-tablesorter')
#print right_table
A=[]
B=[]
C=[]
D=[]
E=[]
state=[]
name=[]
party=[]
for line in right_table:
	for row in line.findAll("tr"):
		cells=row.findAll('td')
		states=row.findAll('th')
		if(len(cells)>0):
			state.append(cells[0].find(text=True))
			name.append(cells[1].find(text=True))
			party.append(cells[4].find(text=True))
	
#print name
'''for i in right_table:
	for j in i.findAll("tr"):
		cells=j.findAll('th')
		states=j.findAll('td')
		if len(cells)==6:
			A.append(cells[0].find(text=True))
			#B.append(states[0].find(text=True))
			C.append(cells[2].find(text=True))
			D.append(cells[3].find(text=True))
			E.append(cells[4].find(text=True))
			
print A
'''
import pandas as pd
df=pd.DataFrame(state,columns=['State'])
df['Name']=name
df['Party']=party
print df
df.to_csv("out1.csv")
db=
df.to_sql("1.sql",flavor='mysql',con=db,index='false')
