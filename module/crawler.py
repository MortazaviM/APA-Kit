from bs4 import BeautifulSoup
import urllib 
from urllib.request import Request, urlopen
import re
from threading import Thread
#import requests
import urllib.parse as urlparse
from pathlib import Path 
import time
import requests
import random
from module.proxy import random_proxy, setter
from fake_useragent import UserAgent 

ave=[]
number=0
head=[]
ua = UserAgent() # From here we generate a random user agent
proxies = [] # Will contain proxies [ip, port]

def garbage(url, max=200, flag=False):
    global ave
    if flag:
        ave=setter()
    else:
        ave=''
    base=finalurl(url)
    folder=''
    threads=[]
    links=[base]
    i=0
    while(len(links) < 200):
        if( i <= len(links)):
            #webpage = urlparse.urlparse(links[i]).path.split('/')[-1]
            webpage = links[i].split('/')[-1]
            origin=links[i].replace(webpage,'')
            tmp=list(urlparse.urlparse(links[i]).path.replace(webpage,'')) #extract folders 
            vtmp=list(urlparse.urlparse(links[0]).path.replace(webpage,'')) #extract folders of final url
            #tmp=list(links[i].replace(webpage,''))
            if(len(tmp)!=0 and tmp[0]=='/'):tmp[0]=''
            if(len(vtmp)!=0 and vtmp[0]=='/'):vtmp[0]=''
            vfolder=''.join(vtmp)
            folder=''.join(tmp).replace(vfolder,'') #remove final url folder from other url
            #folder = urlparse.urlparse(links[i]).path.replace(webpage,'')
            if (folder=='/'): folder=''
            #if (folder.path=='/'): folder=''

            #links += spider(base+'', links[i])
            links += spider(links[i], origin)
            i+=1
        else:
            break


            
    for link in links:
        t=Thread(target=header, args=(link,flag,))
        threads.append(t)
        t.start()
        #header(link)
        

    [x.join(timeout=5) for x in threads]

    f = open('helloworld.txt','w')
    for x in head:
        f.write(str(x) + '\n')
    f.close()


def spider(url, origin):
    tmp=[]
    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page,  'html.parser')
    
    for link in soup.findAll('a'):
        #p=folder
        href=str(link.get('href'))
        if ('http' not in href):
            if ('https' not in href):
                if('#' not in href):
                    if(len(href) != 0 ):
                        if(href == '/'):
                            href=''
                        if(len(href) != 0 and href[0] == '/'):
                            t=list(href)
                            t[0]=''
                            href=''.join(t)
                        #r = requests.get(base+ str(link.get('href')))
                        tmp=tmp + [origin + href]
    return tmp


        #t=Thread(target=linker, args=(str(link.get('href')),url,))
        #t.start()
        #linker(link.get('href'),url)

    

def linker(url, base):
    if ('http' not in str(url)):
        if ('https' not in str(url)):
            if('#' not in str(url)):
                if(str(url) != None):
                    return base+url

                    #r = requests.get(base+url)
                    #contents = r
                    #print(base+url)
                    #print(contents.headers)
                    #print('\n')

def header(url, flag):
    agent =[
    'APA Kit Agent 1.0' ,
    'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)',
    'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko',
    'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
    'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02',
    'Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.10.229 Version/11.62',
    'Mozilla/5.0 (Windows NT 5.1; U; pl; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00',
    'Mozilla/5.0 (Windows; U; Win 9x 4.90; SG; rv:1.9.2.4) Gecko/20101104 Netscape/9.1.0285',
    'btbot/0.4 (+http://www.btbot.com/btbot.html)',
    'Googlebot/2.1 (+http://www.googlebot.com/bot.html)',
    'Gigabot/3.0 (http://www.gigablast.com/spider.html)',
    'Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
    'Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
    ]
    headers = {
    'User-Agent': agent[random.randint(0,21)],
    'From': 'ixtixt@domain.com'  # This is another valid field
    }
    time.sleep(2)
    global number
    number +=1

    session = requests.session()
    #session.proxies = {}

        #try:
    #    r = requests.head(url, headers=headers, verify=True)
    #    if(r.status_code==200):
    #        head.append(url+ str(r.headers))
        #return r.headers
    #    else:
    #        head.append(url + ' >>> error')
    #except:
    #    pass
    #if number % 10 == 0:
    #global ave
    try:
        if flag:
            proxy_index = random.randint(0, len(ave)-1)
            prxy = ave[proxy_index]
            r= session.get(url,headers={'user-agent':ua.random}, proxies= {'http': 'http://'+prxy['ip'] + ':' + prxy['port']} , timeout=5)
            z=session.get('http://icanhazip.com',headers={'user-agent':ua.random}, proxies= {'http': 'http://'+prxy['ip'] + ':' + prxy['port']} , timeout=5)

        else:
            r= session.get(url, timeout=7)
            z=" No Proxy "    

        if(r.status_code == 200):   
            head.append(url+ ' >>> ' + str(z) + ' >>> ' + str(r.headers).strip() )
        else:
            head.append(url + ' >>> '  + str(z)  + ' >>> '  + 'error')
    
    except:
        head.append(url + ' >>>'  + " [null] " + '>>>'  + 'error')    


def finalurl(url):
    with urllib.request.urlopen(url) as ur:
        response = ur.geturl()
    return response