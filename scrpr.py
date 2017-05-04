from bs4 import BeautifulSoup
import urllib,sys,requests,re

import scrapy 

page3 = urllib.urlopen(sys.argv[1]).read()

print("raw \n\n")
print(page3)


table =re.findall(r'<table.*?>(.*?)</table.*?>',page3,(re.IGNORECASE|re.DOTALL)) #locate table for data from stdin 

res = []
line = []

res1 = [] 

print('\n')
tablecount = 1 
for t in table:
		row = re.findall(r'<tr.*?>(.*?)</tr.*?>',t) #locate row per table

		res1.extend((re.findall(r'itemprop="name" content="(.*?)"',t,re.IGNORECASE|re.DOTALL) ) )
		
		#links = re.findall() #locate links		

		for r in row: 


			res.append((re.findall(r'<meta(.*?)>',r,re.IGNORECASE|re.DOTALL)))
			
			line.extend((re.findall(r'itemprop="name" content="(.*?)"',t,re.IGNORECASE|re.DOTALL) ) )



#print(res)
print('')
#print(line)
print(res1)
