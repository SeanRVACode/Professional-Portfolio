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
    
    def check_window_night(self,x,y):
        try: 
            check_white = pyautogui.locateOnScreen('./Images/white_color_of_obstacle.jpg',region=(x,y,400,100),grayscale=True)
        except:
            return None
        return check_white
    def Auto_jump(self):
        while True:
            check = self.check_window(x=471,y=984)
            if check is not None:
                self.jump()
            elif check is None:
                check_night = self.check_window_night(x=471,y=984)
                if check_night is not None:
                    self.jump()
    
    def jump(self):
        pyautogui.press('space')
            
            
            
            