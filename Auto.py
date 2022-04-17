import pyautogui
import datetime
import time
 
size = pyautogui.size()  
print('Screen Size: {0}'.format(size))
 
while True:
    try :
        nowTime = datetime.datetime.now()
        location = pyautogui.locateCenterOnScreen('adskip.png', region = (1200, 750, 300, 100), confidence = 0.7)

        if location == None:            
            print("[{0}] Ad not found. (Press 'Ctrl + C' to quit)".format(nowTime.strftime('%H:%M:%S')))
            time.sleep(2.0)
 
            continue
 
        print('[{0}] Ad found at {1}'.format(nowTime.strftime('%H:%M:%S'), location))
        pyautogui.moveTo(location[0], location[1], 1)
        pyautogui.click(button = 'left')
        time.sleep(5.0)
    
    except KeyboardInterrupt :
        print("Thank You.")
        break