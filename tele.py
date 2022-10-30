import sys
import time
import random
import datetime
import telepot
from sense_hat import SenseHat
from time import sleep

sense= SenseHat()
sense.clear()

temp = sense.get_temperature()
hum = sense.get_humidity()
press = sense.get_pressure()

def handle(msg):
        chat_id = msg['chat']['id']
        command = msg['text']
#print 'Got command: %s ' % command
        if command == 'temp':
                bot.sendMessage(chat_id="1745183471", text=(temp))

bot = telepot.Bot("5789390248:AAEk3WTWIuSTGNtfCjBteK7GOe1xr9QbPCg")
bot.message_loop(handle)

while 1:
        time.sleep(10)
