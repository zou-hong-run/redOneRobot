from common.servo import Servo
from machine import Pin
import time
# 顺时针四个脚
class Move:
    
    s1 = None
    s2 = None
    s3 = None
    s4 = None
    
    isSquatAllFoot = False
    isSquatOneFoot = False
    isSquatTwoFoot = False
    isSquatThreeFoot = False
    isSquatFourFoot = False
    
    isForward = False
    isBackward = False
    isTowardLeft = False
    isTowardRight = False
    
    Angle0 = 0 #100
    Angle15 = 15
    Angle25 = 25
    Angle35 = 35
    Angle45 = 45
    Angle60 = 60
    Angle75 = 75
    Angle90 = 90
    Angle105 = 105
    Angle120 = 120
    Angle135 = 135
    Angle150 = 150
    Angle165 = 165
    Angle180 = 180
    
    
    timers = 500
    
    
    def __init__(self):
        self.s1 = Servo(Pin(15))
        self.s2 = Servo(Pin(17))
        self.s3 = Servo(Pin(25))
        self.s4 = Servo(Pin(27))
        
        time.sleep(1)
        self.resetAllFoot()
        time.sleep(1)
        
    def resetAllFoot(self):
        self.chooseAllFoot(self.Angle0)
    def resetAllProperty(self):
        print("reset")
        self.isSquatAllFoot = False
        self.isSquatOneFoot = False
        self.isSquatTwoFoot = False
        self.isSquatThreeFoot = False
        self.isSquatFourFoot = False
        
        self.isForward = False
        self.isBackward = False
        self.isTowardLeft = False
        self.isTowardRight = False
        
    def oneFoot(self,angle):
        self.s1.write_angle(angle)
        
    def twoFoot(self,angle):
        self.s2.write_angle(180-angle)
    
    def threeFoot(self,angle):
        self.s3.write_angle(180-angle)
    
    def fourFoot(self,angle):
        self.s4.write_angle(angle)
    
    def chooseAllFoot(self,angle):
        self.oneFoot(angle)
        self.twoFoot(angle)
        self.threeFoot(angle)
        self.fourFoot(angle)
        
    def downAllFoot(self):
        self.chooseAllFoot(self.Angle0)
        
    def upAllFoot(self):
        self.chooseAllFoot(self.Angle90)
        
    def squatAllFoot(self):
        self.downAllFoot()
        time.sleep_ms(self.timers)
        self.upAllFoot()
        time.sleep_ms(self.timers)
    
    def downOneFoot(self):
        self.oneFoot(self.Angle0)
    def downTwoFoot(self):
        self.twoFoot(self.Angle0)
    def downThreeFoot(self):
        self.threeFoot(self.Angle0)
    def downFourFoot(self):
        self.fourFoot(self.Angle0)
        
    def upOneFoot(self):
        self.oneFoot(self.Angle90)
    def upTwoFoot(self):
        self.twoFoot(self.Angle90)
    def upThreeFoot(self):
        self.threeFoot(self.Angle90)
    def upFourFoot(self):
        self.fourFoot(self.Angle90)
        
    def squatOneFoot(self):
        self.downOneFoot()
        time.sleep_ms(self.timers)
        self.upOneFoot()
        time.sleep_ms(self.timers)
    def squatTwoFoot(self):
        self.downTwoFoot()
        time.sleep_ms(self.timers)
        self.upTwoFoot()
        time.sleep_ms(self.timers)
    def squatThreeFoot(self):
        self.downThreeFoot()
        time.sleep_ms(self.timers)
        self.upThreeFoot()
        time.sleep_ms(self.timers)
    def squatFourFoot(self):
        self.downFourFoot()
        time.sleep_ms(self.timers)
        self.upFourFoot()
        time.sleep_ms(self.timers)
        
            
    def forward(self):
#         self.oneFoot(self.Angle35)
#         self.twoFoot(self.Angle35)
#         self.threeFoot(self.Angle90)
#         self.fourFoot(self.Angle90)
#         
#         time.sleep_ms(self.timers)
#         
#         self.oneFoot(self.Angle90)
#         self.twoFoot(self.Angle90)
#         self.threeFoot(self.Angle35)
#         self.fourFoot(self.Angle35)
#         
#         time.sleep_ms(self.timers)

        self.oneFoot(self.Angle90)
        self.twoFoot(self.Angle75)
        
        self.threeFoot(self.Angle135)
        self.fourFoot(self.Angle60)
        
        time.sleep_ms(self.timers)
        
        self.oneFoot(self.Angle75)
        self.twoFoot(self.Angle90)
        
        self.threeFoot(self.Angle60)
        self.fourFoot(self.Angle135)
        
        time.sleep_ms(self.timers)
            
            
    def backward(self):

        self.oneFoot(self.Angle135)
        self.threeFoot(self.Angle135)
        self.twoFoot(self.Angle45)
        self.fourFoot(self.Angle45)
        
        time.sleep_ms(self.timers)
        
        self.oneFoot(self.Angle45)
        self.threeFoot(self.Angle45)
        self.twoFoot(self.Angle135)
        self.fourFoot(self.Angle135)
        
        time.sleep_ms(self.timers)
            
    def towardLeft(self):
        self.oneFoot(self.Angle90)
        self.threeFoot(self.Angle90)
        self.twoFoot(self.Angle45)
        self.fourFoot(self.Angle45)
       
        
        time.sleep_ms(self.timers)
        
        self.oneFoot(self.Angle45)
        self.threeFoot(self.Angle45)
        self.twoFoot(self.Angle90)
        self.fourFoot(self.Angle90)
        
        time.sleep_ms(self.timers)
        
    def towardRight(self):
        
        self.oneFoot(self.Angle45)
        self.threeFoot(self.Angle45)
        self.twoFoot(self.Angle90)
        self.fourFoot(self.Angle90)
        
        time.sleep_ms(self.timers)
        
        self.oneFoot(self.Angle90)
        self.threeFoot(self.Angle90)
        self.twoFoot(self.Angle45)
        self.fourFoot(self.Angle45)
        
        time.sleep_ms(self.timers)
        
        
