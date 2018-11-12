import socket
import requests

class Enumeration():

    @classmethod
    def ip_finder(self,url):
        ip=socket.gethostbyname(url)
        return ip
    @classmethod
    def header_finder(self, url):
        response = requests.get('http://' + url)
        return response