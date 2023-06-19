from machine import Pin

import time
import network
light2 = Pin(2,Pin.OUT)
def do_connect():
    wlan = network.WLAN(network.STA_IF)
#     wlan.active(False)
    wlan.active(True)
    print("开始连接...")
    print("连接中...")
#   连接超时设置
    start_time = time.time()
    if not wlan.isconnected():
        wlan.connect("Xiaomi_A246","zy415415666")
#         wlan.connect("redrun","0123456789")
        while not wlan.isconnected():
            light2.value(1)
            time.sleep(1)
            light2.value(0)
            time.sleep(1)
            if time.time() - start_time > 15:
                print("wifi连接超时！！！")
                break
        return False
    else:
        print("连接成功！！！！")
        light2.value(0)
        print("网络配置:",wlan.ifconfig())
        return True
