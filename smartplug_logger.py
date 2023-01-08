from kasa import *
import asyncio
from matplotlib import pyplot as plt
from datetime import datetime
import traceback

FILE_NAME = "./logfile.txt"
logfile = open(FILE_NAME, "a")
logfile.write("Start time: " + str(datetime.now()) + '\n')

plug = SmartPlug("192.168.86.245")
# asyncio.run(plug.update())
# print(plug.emeter_realtime["voltage"])

UPDATE_INTERVAL_SEC = 5
SAVE_INTERVAL = 50 # Saves data to file every this many measurements
times = []
powers = []

save_counter = 0

async def log_power():
    global logfile, save_counter
    while True:
        await plug.update()
        current_time = datetime.now().strftime("%H:%M:%S")
        current_power = plug.emeter_realtime["power"]
        logfile.write(current_time + ' ' + str(current_power) + '\n')
        save_counter += 1

        if (save_counter >= SAVE_INTERVAL):
            save_counter = 0
            logfile.close()
            logfile = open(FILE_NAME, "a")

        await asyncio.sleep(3)

        

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(log_power())
    except Exception as e:
        logfile.write(traceback.format_exc())
        logfile.close()
        loop.close()

   
