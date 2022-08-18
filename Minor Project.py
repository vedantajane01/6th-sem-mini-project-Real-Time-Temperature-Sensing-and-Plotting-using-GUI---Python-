#Program to receive data from port and form a csv file

import csv
import datetime
import serial

current_date_and_time = datetime.datetime.now()
current_date_and_time_string = str(current_date_and_time)

from datetime import date, datetime

extension = ".csv"
#current_date_and_time_string = current_date_and_time_string.replace(".","-")
#current_date_and_time_string = current_date_and_time_string.replace(":","`")
#current_date_and_time_string = current_date_and_time_string.replace(" ","-Time-")
file_name =  current_date_and_time_string[0:10] + extension

serialPort = serial.Serial(port ="COM3", baudrate=9600) 

title=["Time","Date","Temperature"]

with open("2022-05-11.csv", "w", newline="") as csvfile :
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(title)

while True:
    # Wait until there is data waiting in the serial buffer
    if serialPort.in_waiting > 0:
    
        serial = serialPort.read(2)     # We used serialPort.read(2) to read only first two characters 
        
        data=serial.decode('Ascii')
        
        data=list(data.split(","))

        if len(data)==1:                       #We will be receiving only Temperature through USB
            data=data[::-1]
            day = date.today()
            today = day.strftime("%d/%m/%Y")   #Conversion in day-month-year format
            data.append(today)
            noww = datetime.now()
            time = noww.strftime("%H:%M:%S.%f") #Conversion in hour-min-sec-millisec format
            data.append(time)
            data=data[::-1]
    
            print(data)

            with open("2022-05-11.csv", "a", newline="") as csvfile :
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(data)

# print('Transfer Completed')
