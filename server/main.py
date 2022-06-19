from flask import Flask,request
import sqlite3
import json
import serial
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome'

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        data = request.get_json()
        stringData = json.dumps(data)        

        if not stringData:
            print('data is required!')

        else:

            seria = serial.Serial(
                port='COM36',
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=1
            )

            seria.write(bytes(stringData), 'utf-8')
            seria.flush()
            print("Transaction stored succesfully")
    return 'Transaction sent  successfully'