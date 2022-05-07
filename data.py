from pymongo import *
#from requests import *
from json import *
from  urllib.request import *
myclient=MongoClient('mongodb://localhost:27017/')
mydba=myclient["weather"]
mytba=mydba['app']
entre=input("Please enter your location")

data=urlopen("http://api.weatherapi.com/v1/current.json?key=b5fef2042fbb497faeb182122220505&q="+entre+"&aqi=no")
fg=loads(data)
datas = {
    "location": fg["location"]["name"],
    "region": fg["location"]["region"],
    "temp": fg["current"]["temp_c"],
    "temp_f": fg["current"],
    "icon": fg["current"]["condition"]["icon"],


}
print(datas)
print(fg["location"]["name"])
print(fg["current"]["temp_c"])