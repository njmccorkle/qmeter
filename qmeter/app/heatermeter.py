#from apicalls import APIcalls
import requests

class APIcalls (object):
    # time series data
    status = "/luci/lm/api/status"
    time = "/luci/lm/api/status/time"
    set = "/luci/lm/api/status/set"
    lid = "/luci/lm/api/status/lid"
    fan = "/luci/lm/api/status/fan"
    fan_c = "/luci/lm/api/status/fan/c"
    fan_a = "/luci/lm/api/status/fan/a"
    fan_f = "/luci/lm/api/status/fan/f"
    adc = "/luci/lm/api/status/adc"
    temps = "/luci/lm/api/status/temps"
    tempsXn = "/luci/lm/api/status/temps/XX/n"
    tempsXc = "/luci/lm/api/status/temps/XX/c"
    tempsXdph = "/luci/lm/api/status/temps/XX/dph"
    tempsXal = "/luci/lm/api/status/temps/XX/a/l"
    tempsXah = "/luci/lm/api/status/temps/XX/a/h"
    tempsXar = "/luci/lm/api/status/temps/XX/a/r"
    tempsXrfs = "/luci/lm/api/status/temps/XX/rf/s"
    tempsXrfb = "/luci/lm/api/status/temps/XX/rf/b"
    
    # read config values
    config = "/luci/lm/api/config"
    #sp = "/luci/lm/api/config/sp"
    fflor = "/luci/lm/api/config/fflor"
    fmax = "/luci/lm/api/config/fmax"
    fmin = "/luci/lm/api/config/fmin"
    fsmax = "/luci/lm/api/config/fsmax"
    ip = "/luci/lm/api/config/ip"
    lb = "/luci/lm/api/config/lb"
    lbn = "/luci/lm/api/config/lbn"
    ld = "/luci/lm/api/config/ld"
    le0 = "/luci/lm/api/config/le0"
    le1 = "/luci/lm/api/config/le1"
    le2 = "/luci/lm/api/config/le2"
    le3 = "/luci/lm/api/config/le3"
    lo = "/luci/lm/api/config/lo"
    oflag = "/luci/lm/api/config/oflag"
    palh0 = "/luci/lm/api/config/palh0"
    palh1 = "/luci/lm/api/config/palh1"
    palh2 = "/luci/lm/api/config/palh2"
    palh3 = "/luci/lm/api/config/palh3"
    pall0 = "/luci/lm/api/config/pall0"
    pall1 = "/luci/lm/api/config/pall1"
    pall2 = "/luci/lm/api/config/pall2"
    pall3 = "/luci/lm/api/config/pall3"
    pca0 = "/luci/lm/api/config/pca0"
    pca1 = "/luci/lm/api/config/pca1"
    pca2 = "/luci/lm/api/config/pca2"
    pca3 = "/luci/lm/api/config/pca3"
    pcb0 = "/luci/lm/api/config/pcb0"
    pcb1 = "/luci/lm/api/config/pcb1"
    pcb2 = "/luci/lm/api/config/pcb2"
    pcb3 = "/luci/lm/api/config/pcb3"
    pcc0 = "/luci/lm/api/config/pcc0"
    pcc1 = "/luci/lm/api/config/pcc1"
    pcc2 = "/luci/lm/api/config/pcc2"
    pcc3 = "/luci/lm/api/config/pcc3"
    pcr0 = "/luci/lm/api/config/pcr0"
    pcr1 = "/luci/lm/api/config/pcr1"
    pcr2 = "/luci/lm/api/config/pcr2"
    pcr3 = "/luci/lm/api/config/pcr3"
    pcurr0 = "/luci/lm/api/config/pcurr0"
    pcurr1 = "/luci/lm/api/config/pcurr1"
    pcurr3 = "/luci/lm/api/config/pcurr3"
    pidb = "/luci/lm/api/config/pidb"
    pidd = "/luci/lm/api/config/pidd"
    pidi = "/luci/lm/api/config/pidi"
    pidp = "/luci/lm/api/config/pidp"
    pn0 = "/luci/lm/api/config/pn0"
    pn1 = "/luci/lm/api/config/pn1"
    pn2 = "/luci/lm/api/config/pn2"
    pn3 = "/luci/lm/api/config/pn3"
    po0 = "/luci/lm/api/config/po0"
    po1 = "/luci/lm/api/config/po1"
    po2 = "/luci/lm/api/config/po2"
    po3 = "/luci/lm/api/config/po3"
    prfn0 = "/luci/lm/api/config/prfn0"
    prfn1 = "/luci/lm/api/config/prfn1"
    prfn2 = "/luci/lm/api/config/prfn2"
    prfn3 = "/luci/lm/api/config/prfn3"
    pt0 = "/luci/lm/api/config/pt0"
    pt1 = "/luci/lm/api/config/pt1"
    pt2 = "/luci/lm/api/config/pt2"
    pt3 = "/luci/lm/api/config/pt3"
    sceil = "/luci/lm/api/config/sceil"
    smax = "/luci/lm/api/config/smax"
    smin = "/luci/lm/api/config/smin"
    sp = "/luci/lm/api/config/sp"
    ucid = "/luci/lm/api/config/ucid"


class Heatermeter(object):

    def __init__ (self, httpConnect = True, server = 'localhost', port='80', apikey=None):
        #self.httpConnect = 1 # 0=Serial, 1=http
        #self.server = "http://" + config.SERVER_ADDRESS
        #self.port = str(config.SERVER_PORT)
        #self.apikey = config.API_KEY
        self.apiCalls = APIcalls()
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
