from bs4 import BeautifulSoup,SoupStrainer
import re
##Get HTML Body from .sgm files
text = []
for i in range(22):
	if i < 10:
		print('reut2-00'+str(i)+'.sgm')
		#to path auto einai to directory, pou exw ta .sgm arxeia
		f = open('C:/Users/User/Desktop/Data Mining/reut2-00'+str(i)+'.sgm', 'r')
		data= f.read()
		soup = BeautifulSoup(data)
		contents = soup.findAll('reuters')
		for reuter in contents:
			text.append(reuter.text)
	else:
		print('reut2-0'+str(i)+'.sgm')
		#to path auto einai to directory, pou exw ta .sgm arxeia
		f = open('C:/Users/User/Desktop/Data Mining/reut2-0'+str(i)+'.sgm', 'r')
		data= f.read()
		soup = BeautifulSoup(data)
		contents = soup.findAll('reuters')
		for reuter in contents:
			text.append(reuter.text)
print('Ta sunolika documents einai:', len(text))
##from documents remove special characters and split each documents to words
text = [re.sub(r'[^\w]', ' ', elem).lower() for elem in text]
with open('clened_text.txt', 'w') as output:
	for t in range(len(text)):
		output.writelines('##text'+str(t)+'##')
		output.writelines('\n')
		output.writelines('\n')
		output.writelines(text[t])
		output.writelines('\n')
		output.writelines('\n')
output.close()
