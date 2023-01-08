from kasa import *
import asyncio
from matplotlib import pyplot as plt
from datetime import datetime


plug = SmartPlug("192.168.86.245")
# asyncio.run(plug.update())
# print(plug.emeter_realtime["power"])

MAX_LEN = 200
UPDATE_INTERVAL_SEC = 3
times = []
powers = []

def add_power(arr_time, arr_power, time, power):
    if (len(arr_power) >= MAX_LEN):
        arr_time.pop(0)
        arr_power.pop(0)
    arr_time.append(time)
    arr_power.append(power)

async def update_graph():
    while True:
        plt.plot(times, powers)
        plt.gcf().autofmt_xdate()
        plt.show(block = False)
        plt.pause(0.1)

        await update_power()
        await asyncio.sleep(UPDATE_INTERVAL_SEC)

async def update_power():
    await plug.update()
    current_time = datetime.now()
    current_power = plug.emeter_realtime["power"]
    add_power(times, powers, current_time, current_power)
        

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(update_graph())
    finally:
        loop.close()

   
