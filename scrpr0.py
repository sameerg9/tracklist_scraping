import sys,re,csv 
import pandas as pd
from urllib3 import PoolManager
from sys import argv

# if (len(sys.argv) < 2):
# 	print('~-----specify url------~')
# 	quit()

site ='https://www.1001tracklists.com' 
url='https://www.1001tracklists.com/source/gh73v3/ignite-radio/index.html'
url2= 'https://www.1001tracklists.com/source/tgg1cc/maxximize-on-air/index.html'
#resp = http.request('GET',argv[1])	
http = PoolManager()
resp = http.request('GET',url)	
html = resp.data.decode("utf-8")

ll = []
ll.extend((re.findall(r'<tr(.*?)>',html,re.IGNORECASE|re.DOTALL)) )
print(ll)
links0 = []
listCount =0
for l in ll:
	links0.extend((re.findall(r'class=" action" onclick="window.open\(\'(.*?)\',',l,re.IGNORECASE|re.DOTALL)) )
linkCount = 0
print(ll)
print(links0)

var0 = [] 
tracks = [] 
span0 = [] 
plays= [] 
span1 = [] 
span= [] 
v00 = [] 
artists = [] 
rec_labels = [] 
v03 = [] 
v04 = [] 
v2 = [] 
rocks = []

output = []
var1 = []

info = []
info1 = []

i = 0 
print("\ngoing in+\n +\n ++\n  ++++")

for link in links0:
	if(i>3):
		quit()
	episodes = site + link

	# print(linkCount)
	# print(i,'______',episodes)
	
	resp = http.request('GET',episodes)	
	ep = resp.data.decode("utf-8")
	
	info1.extend((re.findall(r'itemprop="interactionCount" content="(.*?)"',ep,re.IGNORECASE | re.DOTALL  )))
	
	table =re.findall(r'<table.*?>(.*?)</table.*?>',ep,(re.IGNORECASE|re.DOTALL)) #locate table for data from stdin
	#plays for tracks within episode 
	
	span1.extend(re.findall(r'<i class="fa fa-play-circle-o fa-24 floatL blueTxt" title="tracklist number support"></i> <span class="greenTxt tgInfoCount">(.*?)x' , ep , (re.IGNORECASE|re.DOTALL)  ))
	if span1 == '':
		span1.extend(0)

	var0 = re.findall(r'itemprop="name" content=".*?-(.*?)"',ep,re.IGNORECASE|re.DOTALL)  
	v00.extend(re.findall(r'<meta itemprop="byArtist" content="(.*?)">' , ep , re.IGNORECASE|re.DOTALL))
	rec_labels.extend(re.findall(r'class=" blueTxt ">(.*?)<', ep , re.IGNORECASE|re.DOTALL ) )
	
	var1.extend(var0[:1])		

	var0 = var0[3:] # clean up tracks

	
	artists.extend(v00)
	tracks.extend(var0)
	# print(artists," [] ",tracks)
	

	#plays/likes for episode

	var1.extend(re.findall(r'itemprop="interactionCount" content="UserPageVisits:(.*?)"',ep, re.IGNORECASE | re.DOTALL))
	var1.extend(re.findall(r'title="play time"> <i.*?></i> <span.*?>(.*?)<' , ep , re.IGNORECASE | re.DOTALL ))
	#var1.extend(re.findall(r'title="musicstyle(s)"> <i class=	"fa fa-music fa-20 blueTxt"></i> <span class="tlBrowseItem">(.*?)</span>' ,ep , re.IGNORECASE | re.DOTALL) )
	var1.extend(re.findall(r'title="musicstyle(s)"> <i.*?></i> <span class="tlBrowseItem">(.*?)<' , ep,re.IGNORECASE|re.DOTALL ) ) 
	
	linkCount = linkCount + 1
	i = i+1
	#clear buffers
	var1 = []
	var0 = [] 
	v00= [] 


listy0 = list(zip(tracks,artists,rec_labels,span1))
dd = pd.DataFrame(listy0)
dd.to_csv('trackinfo0.csv' , index = False , header = ['track_name' , 'artist' , 'label' ,'plays'] ) # add the tracklist_id to list zip


