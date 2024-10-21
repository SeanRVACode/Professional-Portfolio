import pyautogui
import pyscreeze
from PIL import ImageGrab
import time



class Dino:
    def __init__(self):
        pyautogui.FAILSAFE = False
        self.screenWidth,self.screenHeight = pyautogui.size()
        
    # def check_window(self,x,y):
    #     # Attempts to locate the exact color in a specific region of the screen.
    #     try:
    #         check = pyautogui.locateOnScreen('./Images/color_of_obstacle.jpg',region=(x,y,400,100),grayscale=True)
    #     except:
    #         return None
    #     return check
    def check_pixel(self,x,y):
        while True:
            if not self.detect_change(x,y):
                print('Jump')
                self.jump()
                
    def detect_change(self,x,y):
        check_night = pyautogui.pixelMatchesColor(287,328,(32,33,36))
        if check_night:
            check_change_night = pyautogui.pixelMatchesColor(x,y,(32,33,36))
            if check_change_night:
                   check_air_night = pyautogui.pixelMatchesColor(825,996,(32,33,36))
                   return check_air_night
            elif not check_change_night:
                return False
        else:    
            check_change = pyautogui.pixelMatchesColor(x,y,(255,255,255))
            if check_change:
                check_air = pyautogui.pixelMatchesColor(825,996,(255,255,255))
                return check_air
            elif not check_change:
                return False
        
    def get_cursor(self):
        '''Exists solely so I can check where my cursor is.'''
        while True:
            cursor = pyautogui.position()
            print(cursor)
            im = pyautogui.screenshot(region=(625,1178,400,200))
            im.save('test.png')
            # pix = im.getpixel(cursor)
            print(cursor)
            # pyautogui.moveTo(725,1100)
            pix = pyautogui.pixel(cursor.x,cursor.y)
            print(pix)
            # print(pix)

    
    def jump(self):
        pyautogui.press('up')
        # time.sleep(.1)
            
            
            
            