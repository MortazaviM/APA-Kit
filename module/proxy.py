from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import random
import requests
from fake_useragent import UserAgent
from threading import Thread
import time
ua = UserAgent() # From here we generate a random user agent
proxies = [] # Will contain proxies [ip, port]
ave=[]
# Main function
def setter():
  time.sleep(1)
  # Retrieve latest proxies
  proxies_req = Request('https://www.sslproxies.org/')
  proxies_req.add_header('User-Agent', ua.random)
  proxies_doc = urlopen(proxies_req).read().decode('utf8')

  soup = BeautifulSoup(proxies_doc, 'html.parser')
  proxies_table = soup.find(id='proxylisttable')

  # Save proxies in the array
  for row in proxies_table.tbody.find_all('tr'):
    proxies.append({
      'ip':   row.find_all('td')[0].string,
      'port': row.find_all('td')[1].string
    })

  # Choose a random proxy
  proxy_index = random_proxy()
  proxy = proxies[proxy_index]
  counter=[]
  for n in range(1, len(proxies)):
    proxy_index = random_proxy()
    proxy = proxies[n]

    req = 'http://icanhazip.com'
    #req.set_proxy( proxy['ip'] + ':' + proxy['port'], 'http')
    #counter +=1
    T=Thread(target=lookout, args=(req,n,proxy,))
    counter.append(T)
    T.start()



  
  [x.join() for x in counter]

    
  #global ave

  return ave


# Retrieve a random index proxy (we need the index to delete it if not working)
def random_proxy():
    return random.randint(0, len(proxies) - 1)


def lookout(req, i, proxy):
  global ave
  #n=1
  # Every 10 requests, generate a new proxy
  #if n % 1 == 0:
  #proxy_index = i #random_proxy()
  #proxy = proxies[proxy_index]

  # Make the call
  my_ip=''
  try:
    amp={'http': 'http://'+ proxy['ip'] + ':' + proxy['port']}
    hmp={'user-agent': ua.random}
    #my_ip = urlopen(req).read().decode('utf8')
    my_ip=requests.get(req, proxies=amp, headers=hmp)
    print('#' + str(i) + ': ' + my_ip.text)
    #if (my_ip.status_code == '200'):

    ave.append(proxy)
  except: # If error, delete this proxy and find another one
    #del proxies[proxy_index]
    print('Proxy ' + proxy['ip'] + ':' + proxy['port'] + ' my ip: ' + str(my_ip) + ' deleted.')
    proxy_index = random_proxy()
    proxy = proxies[proxy_index]




if __name__ == '__main__':
    setter()



