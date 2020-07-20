# Formats raw html using soup.prettify() for better analysis

from bs4 import BeautifulSoup

for i in range(1007):
	try:
		if i < 1000:
			file = open('./Gradesheets/' + str(190001 + i) + '.html').read()
		else:
			file = open('./Gradesheets/' + str(190075 + i) + '.html').read()
		soup = BeautifulSoup(file, 'html.parser')
		if i < 1000:
			file1 = open('./Gradesheets/' + str(190001 + i) + '.html', 'w')
		else:
			file1 = open('./Gradesheets/' + str(190075 + i) + '.html', 'w')
		file1.write(soup.prettify())
		file1.close()
		if i < 1000:
			print(str(190001 + i)+' successful!')
		else:
			print(str(190075 + i)+' successful!')
	except:
		if i < 1000:
			print(str(190001 + i)+' failed!')
		else:
			print(str(190075 + i)+' failed!')
