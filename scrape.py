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


"""
<tr class=" action" onclick="window.open('/tracklist/1yjslymt/noisia-noisia-radio-s03e17-2017-04-28.html', '_self');" id="tlRow_134651">
urls = [url] #stack of urls to scrape
visited = [url] #record of all urls

while len(urls) > 0:
	try:
		htmltext = urllib.urlopen(urls[0]).read()
	except: 
		print urls[0]
	
	soup = BeautifulSoup(htmltext,"lxml")
	urls.pop(0) # grab first element 
	print(len(urls))
	for tag in soup.findAll('a' , href = True):
		#print(tag['href'])
		
		tag['href'] = urlparse.urljoin(url , tag['href'] )
		#grabbing urls from urls found 
		
		#
		if url in tag['href'] and tag['href'] not in visited: 
			urls.append(tag['href']) #
			visited.append(tag['href']) # will have complete record of sites
print(visited)
"""		
		 	
