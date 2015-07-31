# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route,template
import requests
import get_weather
import get_list
import time
import datetime
from datetime import date




@route('/map800')
def kentweather3():
    alls= get_list.get_all_list("https://data.sparkfun.com/output/aGOE6rY5mxcxX1GNnOKq.json?")
    temps=alls[0]
    lans=alls[1]
    lons=alls[2]
    temps=temps[0:800]
    lans=lans[0:800]
    lons=lons[0:800]

    # get cur data
    #cur=datetime.datetime.today()
    array=[['ID', 'Longitude', 'Latitude', 'Temperature']]
    for i,item in enumerate(temps):
        #d=datetime.datetime.strptime(item,"%Y-%m-%d")
        #if (d-cur).days==-1:
        #    temps.append(t[i])
        #    lans.append(la[i])
        #    lons.append(lo[i])
        list=[]
        list.append('')
        list.append(float(lons[i]))
        list.append(float(lans[i]))
        list.append(float(temps[i]))
        array.append(list)

    return template("mapdraft", temps=temps,lans = lans,lons=lons,array=array)



application = default_app()

