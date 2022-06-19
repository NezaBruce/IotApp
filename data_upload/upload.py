import requests
import csv
import serial
import json
def readFile(file);
    jsonArray = []

    with open(file, encoding = 'utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            jsonArray.append(row)
        return  jsonArray

data = readFile('transactions.txt')
res = requests.post(
    'http://localhost:8050/upload',json=data)

if res.ok:
    print("Data uploaded successfully!")
    print(data)
    seria = serial.Serial(
        port='COM4'
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1    
    )

    seria.write(bytes(data),'utf-8')
    seria.flush()
    print("Data sent to serial successfully!")