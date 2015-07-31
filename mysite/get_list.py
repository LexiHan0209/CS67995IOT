import requests


def get_stream_list(url):
    req=requests.get(url)
    return req.json()

def get_all_list(url):
    stream=get_stream_list(url)
    all_list=[]
    temp_list=[]
    lan_list=[]
    lon_list=[]
    time_list=[]
    all_list.append(temp_list)
    all_list.append(lan_list)
    all_list.append(lon_list)
    all_list.append(time_list)
    for entry in stream:
        if ((isinstance(entry["temperature"],unicode))==False):
            continue
        if ((isinstance(entry["latitude"],unicode))==False):
            continue
        if ((isinstance(entry["longitude"],unicode))==False):
            continue
        if ((isinstance(entry["timestamp"],unicode))==False):
            continue
        if((entry["latitude"]is None) or (entry["longitude"]is None) or (entry["temperature"] is None )):
            continue
        #if((entry["latitude"]>"90") or (entry["latitude"]<"-90")):
        #    continue
        #if((entry["longitude"]>"180") or (entry["longitude"]<"-180")):
        #    continue

        try:
            float(entry["temperature"])
        except ValueError:
            continue

        try:
            float(entry["longitude"])
        except ValueError:
            continue

        try:
            float(entry["latitude"])
        except ValueError:
            continue
        try:
            str(entry["timestamp"])
        except ValueError:
            continue


        t= float(entry["temperature"])
        lon=float(entry["longitude"])
        lan=float(entry["latitude"])
        ti=str(entry["timestamp"])
        ti=ti[0:10]


        if lan>90 or lan<-90:
            continue
        if lon>180 or lon<-180:
            continue

        temp_list.append(t)
        lan_list.append(lan)
        lon_list.append(lon)
        time_list.append(ti)

    return all_list

