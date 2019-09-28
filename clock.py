import datetime
import time
from os import system

while True :
    system('clear')
    current_time = datetime.datetime.now()
    print "Current Time: ", current_time.time().strftime("%H:%M:%S")
    time.sleep(.1)
