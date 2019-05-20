import requests
from bs4 import BeautifulSoup    # PyPI name: beautifulsoup4
import pandas as pd
import csv
url = 'http://web.studenti.math.pmf.unizg.hr/~silovro/strojno'

#r = requests.get(url)
#data = r.text
#with open('html_kod.html', 'w', encoding='utf-8') as f:
#    f.write(data)

with open('html_kod.html', 'r', encoding='utf-8') as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')
table = soup.find('tbody')
print(table.prettify())
cells= table.find_all('td')
for cell in cells:
    print(cell.text)
n_row=len(table.find_all('tr'))
n_col=int(len(cells)/n_row)
print(n_row)
print(n_col)
rows = []
for i in range(n_row):
    row = []
    for j in range(n_col):
        text = cells[i*n_col + j].text
        row.append(text)
    if i == 0:
        column_names = row
    else:
        rows.append(row)

assert len(rows) == n_row - 1

df = pd.DataFrame(rows, columns=column_names)

pd.set_option('display.max_columns', n_col)
pd.set_option('display.width', 200)
#print(df)
#print(df[2:4])
print(rows[0][1])
print(rows[0][2])
print(rows[1][1])
print("Tu samo sada ")
DATA_LOCATION = "dr1.csv"
FIRST_ATTRIBUTE = "drzava"
SECOND_ATTRIBUTE = "overall"
treci="koef"
datas = pd.read_csv(DATA_LOCATION)
data1 = datas[[FIRST_ATTRIBUTE, SECOND_ATTRIBUTE, treci]]
r=csv.reader(open('dr1.csv'))
lines=list(r)
K = data1.values
print("Duljina od K je--------------------------------------------------------- ")
print(rows[0][2])
print(lines[71][2])
print(n_row)
for i in range(0,72):
    print("Usao sam...")
    for j in range(0,210):
        #print("Usao sam1")
        print(lines[i][0])
        #print(rows[j][2])
        #print("Prije prvog ifa")
        if(lines[i][0]==rows[j][1]):
            lines[i][2]=rows[j][2]
            print(rows[j][1])
            print(lines[i][0])
            print(rows[j][2])
            print("Kraj....")
#print(df[0])
#print(df[1])
writer=csv.writer(open('dr1.csv','w'))
writer.writerows(lines)
