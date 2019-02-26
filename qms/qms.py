import requests

server = "http://heatermeter.mccorkle.co"
path = "/luci/lm/api/status"
apikey = "5c4dfbd597b59c9af5a218a0dff00b9a"

print(server + path + "?apikey=" + apikey)
