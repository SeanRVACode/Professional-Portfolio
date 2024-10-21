import pyautogui
import pyscreeze
from PIL import ImageGrab
import time



class Dino:
    def __init__(self):
        pyautogui.FAILSAFE = False
        self.screenWidth,self.screenHeight = pyautogui.size()
        
    def check_window(self,x,y):
        # Attempts to locate the exact color in a specific region of the screen.
        try:
            check = pyautogui.locateOnScreen('./Images/color_of_obstacle.jpg',region=(x,y,400,100),grayscale=True)
        except:
            return None
        return check
    def check_pixel(self,x,y):
        # TODO need to figure out if its easier to just check pixels
        
            # im = pyautogui.screenshot(region=(x,y,400,100))
        while True:
            pix = pyautogui.pixelMatchesColor(x,y,(83,83,83))
            pix_air = pyautogui.pixelMatchesColor(x,1011,(83,83,83))
            pix_mid = pyautogui.pixelMatchesColor(x,1152,(83,83,83))
            pix_wh = pyautogui.pixelMatchesColor(x,y,(172,172,172))
            pix_wh_mid = pyautogui.pixelMatchesColor(x-10,1152,(172,172,172))
            pix_wh_air = pyautogui.pixelMatchesColor(x,1011,(172,172,172))
            if pix or pix_air or pix_mid or pix_wh or pix_wh_mid or pix_wh_air:
                self.jump()
                print(f'Pix: {pix} pix_air: {pix_air} pix_mid: {pix_mid}')
                
                # im = pyautogui.screenshot(region=(x-200,y-200,200,200))
                # im.save('test_fail.png')
            # time.sleep(.01)

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
            
            
            
            