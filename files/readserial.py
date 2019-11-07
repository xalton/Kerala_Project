import serial
from datetime import datetime
from time import strftime
import csv
ser = serial.Serial('COM5', 9600, timeout=300)
b = 0

print("Demarrage")
with open('Test.txt','w') as f:
    fieldnames = ['Température:','temps:']
    write = csv.DictWriter(f,fieldnames=fieldnames,delimiter='\t')
    write.writeheader()
    for  b in range(73):
        temp = str(ser.readline())
        time = datetime.now().strftime('%H:%M:%S')
        print(temp)
        print(time)
        write.writerow({'Température:': temp ,'temps:':time})
        b = b + 1
        # if time != '20:00:00':
        #     write.writerow({'Température:': temp ,'temps:':time})
        # else:
        #     b = False
