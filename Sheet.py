from urllib import request
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
hum = sense.get_humidity()
press = sense.get_pressure()

while True:
# if sensor.get.data.temperature():
 
 sleep(3)
 #x = temp
 #print(temp)
 #print(hum)
 #print(press)
 #form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfjn9WJ-RALsDMmJ0-gdEKvAWlMlMxPJR6KvFpOn0lhkF-gtg/formResponse?usp=pp_url&entry.413193452={}&submit=Submit".format(hum)
 #form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfjn9WJ-RALsDMmJ0-gdEKvAWlMlMxPJR6KvFpOn0lhkF-gtg/formResponse?usp=pp_url&entry.413193452={}&submit=Submit".format(temp)
 #form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfjn9WJ-RALsDMmJ0-gdEKvAWlMlMxPJR6KvFpOn0lhkF-gtg/formResponse?usp=pp_url&entry.665622763={}&submit=Submit".format(hum)
 #form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfjn9WJ-RALsDMmJ0-gdEKvAWlMlMxPJR6KvFpOn0lhkF-gtg/formResponse?usp=pp_url&entry.1198532352={}&submit=Submit".format(press)
 form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfjn9WJ-RALsDMmJ0-gdEKvAWlMlMxPJR6KvFpOn0lhkF-gtg/formResponse?usp=pp_url&entry.413193452={}&entry.665622763={}&entry.1198532352={}&submit=Submit".format(temp,hum,press)
 request.urlopen(form_url)




