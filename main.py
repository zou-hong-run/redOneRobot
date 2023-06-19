from machine import Pin
import time
from common.connect_wifi import do_connect
from lib.microdot import Microdot, send_file,Request

from lib.microdot_websocket import with_websocket

from common.move import Move

pin2 = Pin(2,Pin.OUT)

do_connect()

app = Microdot()

Request.socket_read_timeout = None

move = Move()


@app.route('/')
def index(request):
    return send_file('index.html')

@app.route('/test')
def index(request):
    return "你好测试"


@app.route('/echo')
@with_websocket
def echo(request, ws):
    while True:
        data = ws.receive()
        print(data)
        if(data == "downAllFoot"):
            pin2.value(1)
            move.downAllFoot()
        elif(data == "upAllFoot"):
            pin2.value(0)
            move.upAllFoot()
        elif(data == "squatAllFoot"):
            pin2.value(0)
            move.squatAllFoot()
        elif(data == "resetAllFoot"):
            pin2.value(0)
            move.resetAllFoot()
        elif(data == "forward"):
            move.forward()
        elif(data == "backward"):
            move.backward()
        elif(data == "towardLeft"):
            move.towardLeft()
        elif(data == "towardRight"):
            move.towardRight()
        else:
            move.resetAllFoot()
            
        ws.send("ok")
        

app.run()

def blink():
    for i in range(5):
        pin2.value(int(not pin2.value()))
        time.sleep(1)
blink()
print("ok")