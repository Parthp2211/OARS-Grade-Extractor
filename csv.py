# Creates CSV containing spi1, spi2 and cpi

from bs4 import BeautifulSoup
import pandas as pd

rol = []
name = []
dept = []
sem1 = []
sem2 = []
cpi = []
cols = ['Roll No.', 'Name', 'Dept', 'Sem1', 'Sem2', 'CPI']

for i in range(1007):
    try:
        if i < 1000:
            file = open('./Gradesheets/' + str(190001 + i) + '.html').read()
        else:
            file = open('./Gradesheets/' + str(190075 + i) + '.html').read()
        soup = BeautifulSoup(file, 'html.parser')
        td_list = soup.find_all('td')
        if td_list[-15].text.strip():
            rol.append(td_list[0].text.strip())
            name.append(td_list[1].text.strip())
            dept.append(td_list[2].text.strip())
            sem1.append(td_list[-15].text.strip())
            sem2.append(td_list[-8].text.strip())
            cpi.append(td_list[-2].text.strip())
            if i < 1000:
                print(str(190001 + i) + ' successful!')
            else:
                print(str(190075 + i) + ' successful!')
        else:
            if i < 1000:
                print(str(190001 + i) + ' failed!')
            else:
                print(str(190075 + i) + ' failed!')
    except:
        if i < 1000:
            print(str(190001 + i) + ' failed!')
        else:
            print(str(190075 + i) + ' failed!')

df = pd.DataFrame(columns=cols)
df['Roll No.'] = rol
df['Name'] = name
df['Dept'] = dept
df['Sem1'] = sem1
df['Sem2'] = sem2
df['CPI'] = cpi

print(df)
df.to_csv('data.csv')