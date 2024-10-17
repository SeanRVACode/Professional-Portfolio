import pyautogui
import pyscreeze



class Dino:
    def __init__(self):
        
        self.screenWidth,self.screenHeight = pyautogui.size()
        
    def check_window(self,x,y):
        # window = pyautogui.screenshot(region=(x,y,200,100))
        try:
            check = pyautogui.locateOnScreen('./Images/color_of_obstacle.jpg',region=(x,y,200,100))
        except:
            return None
        return check
    def Auto_jump(self):
        while True:
            check = self.check_window(x=471,y=984)
            if check is not None:
                self.jump()
    
    def jump(self):
        pyautogui.press('space')
            
            
            
            