from flask import Flask,render_template,request
from pymongo import *
import requests


app=Flask(__name__,template_folder="template",static_folder="static")





@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
        city = request.form['city']
    else:
        city = "vadodara"

    source = requests.get(
        "http://api.weatherapi.com/v1/current.json?key=b5fef2042fbb497faeb182122220505&q=" + city + "&aqi=no")
    fg = source.json()
    datas = {
        "location": fg["location"]["name"],
        "region": fg["location"]["region"],
        "country": fg["location"]["country"],
        "time": fg["location"]["localtime"],
        "temp": fg["current"]["temp_c"],
        "temp_f": fg["current"]["temp_f"],
        "icon": fg["current"]["condition"]["icon"],
        "text": fg["current"]["condition"]["text"],
        "wind":fg["current"]["wind_mph"],
        "dir": fg["current"]["wind_dir"],
        "humi": fg["current"]["humidity"],
        "cloud": fg["current"]["cloud"],


    }


    return render_template("index.html",data=datas)

@app.route('/weather',methods=['POST','GET'])
def weather():


    source = requests.get(
        "http://api.weatherapi.com/v1/current.json?key=b5fef2042fbb497faeb182122220505&q=" + city + "&aqi=no")
    fg = source.json()
    datas = {
        "location": fg["location"]["name"],
        "region": fg["location"]["region"],
        "time": fg["location"]["localtime"],
        "temp": fg["current"]["temp_c"],
        "temp_f": fg["current"]["temp_f"],
        "icon": fg["current"]["condition"]["icon"],
        "text": fg["current"]["condition"]["text"],
        "wind": fg["current"]["wind_mph"],

    }

    return render_template("index.html",data=datas)




if __name__=="__main__":
    app.run(debug=True)

