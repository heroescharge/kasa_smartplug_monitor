from matplotlib import pyplot as plt

FILE_NAME = "./logfile.txt"
input_file = open(FILE_NAME, "r")

contents = input_file.read().split('\n')
contents.pop(0)
contents = [v for v in contents if v != '']

times = []
powers = []

def HMS_to_hours(time_str):
    hour_str = time_str[0:2]
    minute_str = time_str[3:5]
    second_str = time_str[6:]

    total_hours = int(hour_str) + int(minute_str) / 60 + int(second_str) / 3600
    return total_hours

for data in contents:
    data = data.split(' ')
    times.append(HMS_to_hours(data[0]))
    powers.append(float(data[1]))

plt.plot(times, powers)
plt.show()
