import pyautogui
import pyscreeze
from PIL import ImageGrab
import time



class Dino:
    def __init__(self):
        # pyautogui.FAILSAFE = False
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
        check_day = pyautogui.pixelMatchesColor(287,328,(32,33,36))
        if check_day:
            check_change_night = pyautogui.pixelMatchesColor(x,y,(32,33,36))
            return check_change_night
        else:
                    
            check_change = pyautogui.pixelMatchesColor(x,y,(255,255,255))
            if check_change:
                check_air = pyautogui.pixelMatchesColor(825,996,(255,255,255))
                return check_air
            elif not check_change:
                return check_change
        
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
    # def check_window_night(self,x,y):
    #     try: 
    #         check_white = pyautogui.locateOnScreen('./Images/white_color_of_obstacle.jpg',region=(x,y,400,100),grayscale=True)
            
    #     except:
    #         return None
    #     return check_white
    def Auto_jump(self):
        # TODO need to account for birds flying and night time cactus
        while True:
            check = self.check_pixel(x=701,y=1100)
            # check_bird = self.check_pixel(x=801,y=897)
            if check:
                print(check)
                self.jump()
            # if check_bird:
            #     self.jump()
            # check = self.check_window(x=471,y=984)
            # if check is not None:
            #     self.jump()
            # elif check is None:
            #     check_night = self.check_window_night(x=471,y=984)
            #     if check_night is not None:
            #         self.jump()
    
    def jump(self):
        pyautogui.press('up')
        # time.sleep(.1)
            
            
            
            