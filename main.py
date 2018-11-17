import os
import optparse
from module.enum import Enumeration
from module.ports import PortScanning
from threading import Thread
from module.crawler import garbage

url=""
port=""
def main():

    clear = lambda: os.system('cls')
    clear()
    parser = optparse.OptionParser()

    parser.add_option('-s','--server', dest='server', type='string', help='specify target URLs with http(s) [http(s)://example.com]')
    parser.add_option('-p','--port', dest='port', type='string', help='specify target file with URLs')
    parser.add_option('-r','--resolve', dest='resolve',action="store_true", default=False, help='hostname to ip')
    parser.add_option('-o','--openport', dest='openport', type='string', help='Open Port Scanning')
    parser.add_option('-e','--header', dest='header',action="store_true", default=False, help='extract header info')
    parser.add_option('-v','--vuln', dest='vulnerability',action="store_true", default=False, help='HTTP vulnerability scanner')
    options, args = parser.parse_args()


    if(options.port != None):
        port=options.port
        print('Port has been set! ' + '[' + port + ']')
    if(options.server != None):
        url=options.server
        #print('Url has been set! ' + '[' + url + ']')
    if(options.resolve == True):
        ip=Enumeration.ip_finder(url)
        print('ip >>> [' + ip + ']')
        print('Done!')
    if(options.openport != None):
            ip=Enumeration.ip_finder(url)
            threads = []
            pp=str(options.openport)
            if(pp.find("-")!=-1):
                from_port=int(pp.split("-")[0])
                to_port=int(pp.split("-")[1])
                for i in range(from_port, to_port+1):
                    t = Thread(target=PortScanning.openports, args=(ip,i,))
                    threads.append(t)
                    t.start()

            elif(pp.find(",")!=-1):
                fullport=pp.split(",")
                for i in (fullport):
                    t = Thread(target=PortScanning.openports, args=(ip,int(i),))
                    threads.append(t)
                    t.start()


    if(options.header == True):
        ip=Enumeration.ip_finder(url)
        header_ip = Enumeration.header_finder(url)
        print('Header status code >>> ' + str(header_ip))
        for header, value in header_ip.headers.items():
            print(header + " : " + str(value).replace(';','\n'))
        print('Done!')

    if (options.vulnerability == True):
        garbage(url)
        #thread2=[]
        #t2=Thread(target=spider, args=(url,))
        #thread2.append(t2)
        #t2.start()


if __name__ == "__main__":
    main()