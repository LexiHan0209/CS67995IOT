import time

def get_temp():


  f = open("/sys/bus/w1/devices/28-000006dfea27/w1_slave",'r')
  s = f.readlines()
  f.close()
  if not s[0].strip().endswith("YES"):
    return None
  else:
    t = float(s[1].split("=")[-1].strip())/1000;
    return t


#for i in range(0,100):
 # print "Temperature = ", get_temp()
 # time.sleep(2.0)


