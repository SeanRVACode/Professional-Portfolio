import pyautogui
import pyscreeze



class Dino:
    def __init__(self):
        
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
        while True:
            # im = pyautogui.screenshot(region=(x,y,400,100))
            
            pix = pyautogui.pixelMatchesColor(x,y,(83,83,83))
            print(pix)
            return pix
    def get_cursor(self):
        '''Exists solely so I can check where my cursor is.'''
        while True:
            cursor = pyautogui.position()
            im = pyautogui.screenshot(region=(500,994,400,200))
            im.save('test.png')
            # pix = im.getpixel(cursor)
            print(cursor)
            # print(pix)
    # def check_window_night(self,x,y):
    #     try: 
    #         check_white = pyautogui.locateOnScreen('./Images/white_color_of_obstacle.jpg',region=(x,y,400,100),grayscale=True)
            
    #     except:
    #         return None
    #     return check_white
    def Auto_jump(self):
        while True:
            check = self.check_pixel(x=701,y=1100)
            # check_bird = self.check_pixel(x=801,y=897)
            if check:
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
        pyautogui.press('space')
            
            
            
            