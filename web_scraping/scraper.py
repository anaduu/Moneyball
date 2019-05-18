import requests
from bs4 import BeautifulSoup    # PyPI name: beautifulsoup4
import pandas as pd

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
print(df)
print(df[2:4])
print(rows[0][1])

#print(df[0])
#print(df[1])

