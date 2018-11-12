import socket
from module.enum import Enumeration

class PortScanning(object):

    __port=0
    __host=''
    def setPort(self, port):
        self.__port=int( port)
    def setHost(self, host):
        self.__host=host

    @staticmethod
    def openports(ip,port):
        #ip=Enumeration.ip_finder(self.__host)
        soc=socket.socket()
        ip=Enumeration.ip_finder(ip)
        result=soc.connect_ex((ip,port))
        #print('working on port >>> %s'+ %(port)) 
        if (result == 0):
            soc.close
            print('Port %s is open' %(port) )
            #return port
        else:
            soc.close
            print('Port %s is close' %(port))
            #return 0

