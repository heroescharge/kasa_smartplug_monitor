from kasa import *
import asyncio
from matplotlib import pyplot as plt
import matplotlib.dates as mpl_dates
from datetime import datetime
import time
import threading

plug = SmartPlug("192.168.86.245")
# asyncio.run(plug.update())
# print(plug.emeter_realtime["voltage"])

MAX_LEN = 200
UPDATE_INTERVAL_SEC = 3
times = []
voltages = []

def add_voltage(arr_time, arr_voltage, time, voltage):
    if (len(arr_voltage) >= MAX_LEN):
        arr_time.pop(0)
        arr_voltage.pop(0)
    arr_time.append(time)
    arr_voltage.append(voltage)

async def update_graph():
    while True:
        plt.plot(times, voltages)
        plt.gcf().autofmt_xdate()
        plt.show(block = False)
        plt.pause(0.1)

        await update_voltage()
        await asyncio.sleep(UPDATE_INTERVAL_SEC)

async def update_voltage():
    await plug.update()
    current_time = datetime.now()
    current_voltage = plug.emeter_realtime["power"]
    add_voltage(times, voltages, current_time, current_voltage)
        

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(update_graph())
    finally:
        loop.close()

   
