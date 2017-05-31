import urlparse,urllib,sys,re
from bs4 import BeautifulSoup
#crawling setup      #

if (len(sys.argv) < 2):
	print('specify url')
	quit()


site ='https://www.1001tracklists.com'

html = urllib.urlopen(sys.argv[1]).read() 
#print(html)
print("~~~~~~~~~~")


ll = [] 
ll.extend((re.findall(r'<tr(.*?)>',html,re.IGNORECASE|re.DOTALL)) )
#print(ll)
#for article in page3,  if data-minute in <article  > tag and data-minute!=0 ,grabe minute and grab comment in <p> tag
print('\n')

gglinks = [] 
listCount =0
for l in ll:
		 
		#res1.extend((re.findall(r'<p>(.*?)</p>',t,re.IGNORECASE | re.DOTALL) ) )
		gglinks.extend((re.findall(r'class=" action" onclick="window.open\(\'(.*?)\',',l,re.IGNORECASE|re.DOTALL)) )
		
		#del gg[0]
		#del gg[1] 

print("ggLINKS ~~~.  __    .~~~~~")		
print(gglinks)
linkCount = 0 
print('\nlinkCount set @ : !')


rocks = []

output = [] 

for link in gglinks:
	rocks = site + link
	print(rocks)
	

	pebble = urllib.urlopen(rocks).read()

	table =re.findall(r'<table.*?>(.*?)</table.*?>',pebble,(re.IGNORECASE|re.DOTALL)) #locate table for data from stdin 

	for tt in table: 

		output.extend((re.findall(r'itemprop="name" content="(.*?)"',tt,re.IGNORECASE|re.DOTALL) ) )


	
	linkCount = linkCount + 1


print(output)
