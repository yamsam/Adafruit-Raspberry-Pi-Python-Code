import time
import subprocess
import re
import thingspeak

def doit(channel):
    output = subprocess.check_output(["./Adafruit_DHT", "11", "4"]);
    print output
    matches = re.search("Temp =\s+([0-9.]+)", output)
    if (not matches):
	time.sleep(3)
        return
    temp = float(matches.group(1))
  
  # search for humidity printout
    matches = re.search("Hum =\s+([0-9.]+)", output)
    if (not matches):
	time.sleep(3)
        return
    humidity = float(matches.group(1))

    print "Temperature: %.1f C" % temp
    print "Humidity:    %.1f %%" % humidity

    try:
        response = channel.update([temp, humidity])
        print response.status, response.reason
        data = response.read()
    except:
        print "connection failed"


#sleep for 16 seconds (api limit of 15 secs)
if __name__ == "__main__":
    channel = thingspeak.channel('YOUR_API_KEY')
    while True:
        doit(channel)
        time.sleep(60)
