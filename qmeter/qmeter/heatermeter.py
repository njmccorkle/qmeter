from apicalls import APIcalls
import requests

class Heatermeter(object):

    def __init__ (self, httpConnect = True, server = 'localhost', port='80', apikey=None):
        #self.httpConnect = 1 # 0=Serial, 1=http
        #self.server = "http://" + config.SERVER_ADDRESS
        #self.port = str(config.SERVER_PORT)
        #self.apikey = config.API_KEY
        #self.apiCalls = APIcalls()
        self.httpConnect = httpConnect
        self.server = 'http://' + server
        self.port = str(port)
        self.apikey = apikey
        self.apiCalls = APIcalls()
        return

    def sendRequest (self, path, index):
        if index >= 0:
            # replace "XX" in the path with the index value
            path = path.replace('XX', str(index))

        if self.httpConnect == False:
            # send request over serial
            # send dummy return for now
            return {'serial': 'call'}
        else:
            return self.sendHttpRequest(path)

    def sendHttpRequest(self, path):
        requestParams = {'apikey': self.apikey}
        url = self.server + ':' + self.port + path
        return requests.get(url, params=requestParams)
