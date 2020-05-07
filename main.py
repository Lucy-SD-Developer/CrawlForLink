from urllib.request import urlopen
from urllib.parse import urljoin
import re
import socket
import urllib.parse

def downloadWeb(url,pageId):
    if url in urlMap:
        pass
    else:
        pageId += 1
        urlMap[url]=pageId
        idMap[pageId]=url
        htmlFile=open('C:\\Users\\Lu Lin\\Desktop\\EasyCrawler-master\\output'+(str(pageId)+'.txt'),'w')
        htmlFile.write(str(urlopen(url).read()))
        htmlFile.close()
        
        htmlFile=open('C:\\Users\\Lu Lin\\Desktop\\EasyCrawler-master\\output'+(str(pageId)+'.txt'),'r')
        for line in htmlFile:
            ans=re.findall(pattern,line)
            for one in ans :
                urlTail=one.split('"')[1]            
                url=urljoin(url,urlTail)
                if url in urlMap:
                    print('skip---'+url)
                else:
                    print('download---'+url)
                    pageId += 1
                    urlMap[url]=pageId
                    idMap[pageId]=url
                    catchFile=open('C:\\Users\\Lu Lin\\Desktop\\EasyCrawler-master\\output\\'+(str(urlMap[url])+'.txt'),'w')
                    try:
                        catchFile.write(urlopen(url).read())
                    except:
                        pass
                    finally:
                        catchFile.close()               
        htmlFile.close()

    urlMapFile=open('C:\\Users\\Lu Lin\\Desktop\\EasyCrawler-master\\map.txt','w')
    for key in idMap.keys():
        urlMapFile.write(str(key)+'\t'+str(idMap[key])+'\n')
    urlMapFile.close()
    
    print('success!')

if __name__=='__main__':
    socket.setdefaulttimeout(10)
    entrance='http://usaco.org/'
    pattern=re.compile('href="[^(javascript)]\S*[^(#)(css)(js)(ico)]\"')
    pageId=0
    idMap={}
    urlMap={}
    downloadWeb(entrance,pageId)