from threading import Thread
import time
from datetime import datetime
import json
import os
import pyautogui
import win32gui
import win32api
import win32con
import win32process
import win32com.client
from user import User
# from cnocr import CnOcr
SPACE = 32
ENTER = 13
RAD_COLOR = "ff0000-000000"

ANGLE_NUM = {
    0: "1|1|1,1|2|1,1|3|1,1|3|1,1|4|1,1|5|1,1|6|1,1|7|1,0|8|1,-1|7|1,-1|6|1,-1|5|1,-1|4|1,-1|3|1,-1|2|1,-1|1|1,-5|-1|1,-4|-2|1,-4|-3|1,-3|-3|1,0|-3|1,3|-3|1,4|-2|1,5|-1|1,6|0|1,6|1|1,6|2|1,6|3|1,6|4|1,6|5|1,6|6|1,6|8|1,6|9|1,5|9|1,4|10|1,3|11|1,2|11|1,1|11|1,0|11|1,-1|11|1,-2|11|1,-3|11|1,-4|11|1,-4|10|1,-5|9|1,-6|8|1,-6|7|1,-6|6|1,-6|5|1,-6|4|1,-6|3|1,-6|2|1,-6|1|1",
    1: "-1|0|1,-2|0|1,-3|0|1,-3|-1|1,-3|-2|1,-1|-3|1,-2|-3|1,0|-4|1,1|-5|1,3|-5|1,5|-5|1,5|-4|1,5|-2|1,5|0|1,5|1|1,5|2|1,5|3|1,5|4|1,5|5|1,5|6|1,6|6|1,7|6|1,8|6|1,8|7|1,8|8|1,8|9|1,7|9|1,6|9|1,5|9|1,4|9|1,3|9|1,2|9|1,1|9|1,0|9|1,-1|9|1,-2|9|1,-3|9|1,-3|8|1,-3|7|1,-3|6|1,-2|6|1,-1|6|1,0|6|1,0|5|1,0|4|1,0|3|1,0|2|1,0|1|1" ,
    2: "1|0|1,2|1|1,2|2|1,1|2|1,1|3|1,0|4|1,-1|5|1,-2|6|1,-3|7|1,-4|8|1,-5|9|1,-5|10|1,-5|11|1,-4|11|1,-3|11|1,-1|11|1,0|11|1,1|11|1,2|11|1,3|11|1,4|11|1,5|11|1,6|11|1,7|11|1,7|10|1,7|9|1,7|8|1,6|8|1,5|8|1,4|8|1,3|8|1,2|8|1,4|7|1,5|6|1,5|5|1,6|4|1,7|3|1,7|2|1,7|1|1,7|0|1,6|-1|1,5|-2|1,5|-3|1,4|-3|1,3|-3|1,2|-3|1,1|-3|1,0|-3|1,-1|-3|1,-2|-3|1,-3|-3|1,-4|-2|1,-4|-1|1",
    3: "-1|-1|1,-2|-1|1,-3|0|1,-4|0|1,-5|1|1,-6|1|1,-7|0|1,-7|-1|1,-7|-2|1,-6|-3|1,-5|-4|1,-4|-4|1,-3|-4|1,-2|-4|1,-1|-4|1,0|-4|1,1|-4|1,2|-4|1,3|-4|1,3|-3|1,4|-2|1,5|-1|1,5|0|1,4|1|1,3|2|1,4|3|1,5|4|1,5|6|1,4|8|1,3|9|1,1|10|1,0|10|1,-4|10|1,-6|10|1,-7|8|1,-7|6|1,-6|5|1,-4|6|1,-3|7|1,-2|7|1,-1|7|1,0|6|1,0|5|1,-1|4|1,-2|4|1,-3|4|1,-4|3|1,-4|2|1,-3|1|1,-2|1|1,-1|1|1",
    4: "0|1|1,0|2|1,0|3|1,-1|3|1,-2|3|1,-1|2|1,-6|2|1,-5|1|1,-4|0|1,-3|-1|1,-2|-2|1,-2|-3|1,-1|-4|1,-1|-5|1,0|-5|1,1|-5|1,2|-5|1,3|-5|1,4|-5|1,5|-5|1,5|-4|1,5|-3|1,5|-2|1,5|-1|1,5|0|1,5|1|1,5|2|1,5|3|1,6|3|1,6|6|1,5|6|1,5|7|1,5|8|1,5|9|1,4|9|1,3|9|1,2|9|1,1|9|1,1|9|1,0|9|1,0|8|1,0|7|1,0|6|1,-1|6|1,-2|6|1,-3|6|1,-4|6|1,-5|6|1",
    5: "0|-1|1,1|-1|1,2|-1|1,3|-1|1,4|-1|1,5|-1|1,6|-2|1,6|-3|1,6|-3|1,5|-4|1,4|-4|1,3|-4|1,2|-4|1,1|-4|1,0|-4|1,-1|-4|1,-2|-4|1,-3|-4|1,-4|-4|1,-5|-4|1,-5|-3|1,-5|-2|1,-5|-1|1,-5|0|1,-5|1|1,-5|2|1,-5|3|1,-4|3|1,-3|3|1,-2|3|1,-1|3|1,0|3|1,1|4|1,1|5|1,1|6|1,0|7|1,-1|7|1,-2|6|1,-3|6|1,-4|5|1,-5|5|1,-5|10|1,-4|10|1,-3|10|1,-2|10|1,-1|10|1,0|10|1,1|10|1,2|10|1,3|10|1,4|9|1,5|8|1,6|7|1,6|6|1,6|5|1,6|4|1,6|3|1,6|2|1,5|2|1,4|1|1,3|0|1,2|0|1,1|0|1",
    6: "-1|0|1,-1|1|1,-1|2|1,-1|3|1,0|4|1,1|3|1,1|2|1,1|1|1,-3|7|1,-4|6|1,-5|6|1,-5|5|1,-5|4|1,-6|4|1,-6|3|1,-6|1|1,-6|-1|1,-6|-2|1,-6|-3|1,-5|-3|1,-5|-4|1,-4|-5|1,-3|-6|1,-2|-7|1,0|-7|1,2|-7|1,5|-7|1,5|-6|1,5|-5|1,4|-4|1,2|-4|1,1|-4|1,0|-3|1,2|-3|1,3|-3|1,4|-3|1,5|-2|1,6|-2|1,6|-1|1,6|0|1,6|1|1,6|3|1,6|5|1,5|5|1,4|6|1,4|7|1,3|7|1,1|7|1,0|7|1,-1|7|1,-2|7|1,-3|7|1,-4|6|1,-5|5|1,-5|4|1,-6|3|1",
    7: "-1|0|1,-2|0|1,-3|0|1,-5|0|1,-6|0|1,-6|-1|1,-6|-2|1,-6|-3|1,-4|-3|1,-2|-3|1,0|-3|1,2|-3|1,4|-3|1,6|-3|1,6|-2|1,6|-1|1,6|0|1,5|1|1,5|2|1,5|3|1,4|3|1,4|4|1,3|5|1,3|6|1,2|7|1,2|8|1,1|9|1,1|10|1,0|11|1,-1|11|1,-2|11|1,-3|11|1,-4|11|1,-5|11|1,-5|10|1,-5|9|1,-4|8|1,-3|7|1,-3|6|1,-2|5|1,-2|4|1,-1|3|1,-1|2|1,0|1|1,0|0|1",
    8: "-1|1|1,0|1|1,1|1|1,1|2|1,1|6|1,0|6|1,-1|6|1,-1|7|1,0|8|1,1|8|1,-1|7|1,6|9|1,5|10|1,4|10|1,3|11|1,2|11|1,1|11|1,0|11|1,-1|11|1,-2|11|1,-3|11|1,-4|11|1,-5|11|1,-5|10|1,-6|9|1,-6|8|1,-6|7|1,-6|6|1,-6|5|1,-5|4|1,-5|3|1,-6|2|1,-6|1|1,-6|0|1,-5|-1|1,-4|-2|1,-3|-3|1,-2|-3|1,-1|-3|1,0|-3|1,1|-3|1,2|-3|1,3|-3|1,4|-3|1,5|-2|1,6|-1|1,6|0|1,6|1|1,6|2|1,6|3|1,5|3|1,5|4|1,6|4|1,6|5|1",
    9: "1|1|1,1|2|1,1|3|1,1|4|1,0|4|1,-1|3|1,-1|2|1,-1|1|1,-1|-3|1,0|-3|1,1|-3|1,2|-3|1,3|-3|1,4|-2|1,5|-1|1,6|0|1,6|1|1,6|3|1,6|5|1,6|6|1,5|7|1,5|8|1,4|9|1,3|10|1,2|11|1,1|11|1,0|11|1,-1|11|1,-2|11|1,-3|11|1,-4|11|1,-5|10|1,-5|9|1,-4|8|1,-3|8|1,-2|8|1,-1|8|1,0|7|1,-1|7|1,-2|7|1,-3|7|1,-4|7|1,-5|6|1,-6|6|1,-6|5|1,-6|4|1,-6|3|1,-6|2|1,-6|1|1,-6|0|1",
    '-':"-1|0|1,-2|0|1,-3|0|1,-3|0|1,-4|0|1,-5|0|1,-6|0|1,-6|0|1,-7|0|1,-7|-1|1,-7|-2|1,-6|-3|1,-5|-3|1,-4|-3|1,-3|-3|1,-2|-3|1,-1|-3|1,0|-3|1,1|-2|1,1|-1|1"
}

MOVEABLED_WINDOW = {
    "left_down" : "0|-1|1,0|-2|1,0|-3|1,0|-4|1,0|-5|1,0|-6|1,0|-7|1,0|-8|1,0|-9|1,0|-10|1,0|-11|1,0|-12|1,0|-13|1,0|-14|1,0|-15|1,0|-16|1,0|-17|1,0|-18|1,0|-19|1,1|1|1,2|1|1,3|1|1,4|1|1,5|1|1,6|1|1,7|1|1,8|1|1,9|1|1,10|1|1,11|1|1,12|1|1,13|1|1,14|1|1,15|1|1,16|1|1,17|1|1,18|1|1,19|1|1,20|1|1",
    "left_up": "0|1|1,0|2|1,0|3|1,0|4|1,0|5|1,0|6|1,0|7|1,0|8|1,0|9|1,0|10|1,0|11|1,0|12|1,0|13|1,0|14|1,0|15|1,0|16|1,0|17|1,0|18|1,0|19|1,1|-1|1,2|-1|1,3|-1|1,4|-1|1,5|-1|1,6|-1|1,7|-1|1,8|-1|1,9|-1|1,10|-1|1,11|-1|1,12|-1|1,13|-1|1,14|-1|1,15|-1|1,16|-1|1,17|-1|1,18|-1|1,19|-1|1,20|-1|1",
    "right_up": "-1|0|1,-2|0|1,-3|0|1,-4|0|1,-5|0|1,-6|0|1,-7|0|1,-8|0|1,-9|0|1,-10|0|1,-11|0|1,-12|0|1,-13|0|1,-14|0|1,-15|0|1,-16|0|1,-17|0|1,-18|0|1,-19|0|1,1|1|1,1|2|1,1|3|1,1|4|1,1|5|1,1|6|1,1|7|1,1|8|1,1|9|1,1|10|1,1|11|1,1|12|1,1|13|1,1|14|1,1|15|1,1|16|1,1|17|1,1|18|1,1|19|1,1|20|1",
    "right_down": "0|-1|1,0|-2|1,0|-3|1,0|-4|1,0|-5|1,0|-6|1,0|-7|1,0|-8|1,0|-9|1,0|-10|1,0|-11|1,0|-12|1,0|-13|1,0|-14|1,0|-15|1,0|-16|1,0|-17|1,0|-18|1,0|-19|1,0|-20|1,-1|1|1,-2|1|1,-3|1|1,-4|1|1,-5|1|1,-6|1|1,-7|1|1,-8|1|1,-9|1|1,-10|1|1,-11|1|1,-12|1|1,-13|1|1,-14|1|1,-15|1|1,-16|1|1,-17|1|1,-18|1|1,-20|1|1,-21|1|1"


}

STABLED_WINDOW = {
    "A8A8A8": "0|1|9A9A9A,0|2|A8A8A8,0|3|999999,0|4|9F9F9F,0|5|A0A0A0,0|6|A2A2A2,0|7|A1A1A1,0|8|9F9F9F,0|9|9F9F9F,0|10|A2A2A2,0|11|A2A2A2,0|12|A1A1A1,0|13|A3A3A3,0|14|A0A0A0,0|15|A2A2A2,0|16|9D9D9D,0|17|A3A3A3,0|18|A6A6A6,0|19|9C9C9C",
    "6C6C6C": "0|1|686868,0|2|636363,0|3|636363,0|4|5E5E5E,0|5|5D5D5D,0|6|585858,0|7|565656,0|8|545454,0|9|525252,0|10|484848,0|11|484848,0|12|484848,0|13|494949,0|14|494949,0|15|484848,0|16|4A4A4A,0|17|4D4D4D,0|18|555555,0|19|4E4E4E"
}

class MyThread(Thread):
    
    def __init__(self, func, args, ):
        Thread.__init__(self)
        self.func = func
        self.args = args
    
    def run(self):
        # for i in range(10):
            # print(str(i) + " i am" + self.name)
        print(self.name)
        self.func(*self.args)
       

class mWindow:
    
    def __init__(self):
        self.pid = None
        self.create_time = None
        self.cpu = None
        self.memory = None
        self.hwnd = None
        self.hwnd_content = None
        self.width = 1000
        self.height = 600
        self.display = "gdi" # normal gdi gdi2 dx2 dx3 dx
        # windows3
        self.mouse = "windows3" # normal windows windows2 windows3 dx dx2
        # windows
        self.keypad = "windows" # normal windows dx
        self.public = ""
        # 101
        self.mode = 101
        self.dm = None
        # self.lock = None

        self.user = User()

        self.sort_num = 0

          
    def init_process(self, proc):
        self.pid = proc.pid
        self.name = proc.name()
        self.create_time =proc.create_time()
        self.cpu = proc.cpu_percent()
        self.memory = proc.memory_info()
     
       

    # init dm and user
    def init_dm_user(self, hwnd, hwnd_title): 
        self.dm = win32com.client.Dispatch("dm.dmsoft")

        if(self.dm.ver() != "3.1233"):
            # print("error")
            ret = self.dm.Reg("lumiku2fdc744d96597f65888674a63fb3489a", "yk65792928")
            if ret == 0:
                print("Reg error:" )        
            print("dm.ver:", self.dm.ver())
        else:
            print(self.dm.ver())
        
        self.dm.SetPath("D:\\Document\\programming\\MicrosoftVSCode\\java\\ddt\\asset")
        self.dm.SetDict(0, "D:\\Document\\programming\\MicrosoftVSCode\\java\\ddt\\asset\\dm_soft.txt")
        if len(hwnd_title) == 6:
            self.user.username = hwnd_title[2]
            self.hwnd = hwnd_title[3]

            f = open('account.json', 'r', encoding='utf-8')
            content = f.read()
            json_data = json.loads(content)
            self.user.second_password = json_data[hwnd_title[2]][0]['second_password']

           

        # self.dm.SetPath("D:\\Document\\programming\\MicrosoftVSCode\\java\\ddt\\asset")

        # self.set_window_state(1)
        self.bind_window()
        self.click_xy(1, 627)
        # self.dm.SetKeypadDelay("windows", 70)
        # self.dm.SetKeypadDelay("dx", 70)
        print(self.user.username, self.hwnd, self.pid)
        # x, y= 0,0
        # ret= self.dm.GetClientSize(self.hwnd, x,y)
        # print(ret)
        # print(self.d)
      
    def kill(self, proc):
        proc.kill()

    def bind_window(self, mode=1):
        if mode == 0:
            ret = self.dm.BindWindow(self.hwnd, self.display, self.mouse, self.keypad, self.mode)
            if ret == 0:
                print("bind error")
                print("bind get error:", self.dm.GetLastError())
        else:
            # print(type(self.hwnd),type(self.display),type(self.mouse),type(self.keypad),type(self.public),type(self.mode))
            ret = self.dm.BindWindowEx(self.hwnd, self.display, self.mouse, self.keypad, self.public, self.mode)
            if ret == 0:
                print("bind error")
                print(self.dm.GetLastError())
        time.sleep(2)
    
    def _get_client_rect(self):
        x1, y1, x2, y2 = 0, 0, 0, 0
        return self.dm.GetClientRect(self.hwnd, x1, y1, x2, y2)

    def click_xy_front(self, x, y, lock, delay = 0.05):
        lock.acquire()
        ret_set = self.set_window_state(8)
        ret_get = self.get_window_state(5)

        wait_time = 0
        while ret_set == 0 and wait_time < 5:
            print(self.user.username +"set window state front error")
            ret_set = self.set_window_state(8)
            time.sleep(1)
            wait_time += 1

        if ret_get == 0:
            print(self.user.username +"get window state front error")
        
        wait_time = 0
        while ret_get == 0 and wait_time < 10:
            ret_get = self.get_window_state(5)
            time.sleep(1)
            wait_time += 1


        ret = self._get_client_rect()
        if(ret[0] == 1):
            x += ret[1]
            y += ret[2]
            pyautogui.moveTo(x ,y)
            pyautogui.click(x, y)
        else:
            print("get_client_rect error: ret=" + str(ret[0]))
            
      
       
        # self._move_to(x, y)
        # self._click(delay=delay)
        # print(self.user.username + ": cick:" + str(x) + " " + str(y))
        lock.release()
    
    def click_xy(self, x, y, delay = 0.05):
        self._move_to(x, y)
        self._click(delay=delay)
       
    
    def _get_cursor_pos(self):
        x, y = 0, 0
        ret = self.dm.GetCursorPos(x,y)
        return ret
    
    def _left_click(self):
        return self.dm.LeftClick()
        
    def _left_up(self):
        return self.dm.LeftUp()
        
    def _click(self, delay = 0.05):
        self._left_click()
        time.sleep(delay)
        self._left_up()
        time.sleep(0.5)
       
    def click_pic(self, pic_name):
        is_find, x, y = self._find_pic(pic_name)
        re_find = 3
        
        for i in range(re_find):
            time.sleep(0.5)
            is_find, x, y = self._find_pic(pic_name)
            if is_find == 0:
                break

        self.click_xy(x, y)

    def _capture_jpg(self, x1=0, y1=0, x2=1004, y2=600):
        self.dm.CaptureJpg(x1, y1, x2, y2, "test.jpg", 80)

    # def move_to(self, x=190, y=130):
    def _move_to(self, x, y):
        print(self.user.username + ": ready move to:" + str(x) + " " + str(y))
        self.dm.MoveTo(x, y)
        # print(self.user.username + ": modify move to:" + str(x) + " " + str(y+485))
        x, y = 0, 0
        ret = self.dm.GetCursorPos(x,y)
        print(self.user.username + ": actually move to:" + str(ret))
        # time.sleep(0.02)

    # 通过图片找到角度是多少
    def _ocr_angle(self): 
        # self.dm.CaptureJpg(36, 554, 51, 574, "test.jpg", 80)
        # ret = self.dm.Ocr(36, 554, 51, 574, "#0-0", 0.9)
        # print(ret)
        # self.dm.CaptureJpg(50, 554, 66, 574, "test2.jpg", 80)
        # ret = self.dm.Ocr(50, 554, 66, 574, "#0-0", 0.8)
        # print(ret)

        # ret = self.dm.CaptureJpg(36,554, 66, 574, "test3.jpg", 80)
        
        # ret = self.dm.Ocr(36,554, 66, 574, "#0-0", 0.8)
        # return int(ret)
        # print(type(ret), ret)
        # return int(ret)

        angle_dict = {} # x坐标：力度值，通过左边判断 找到的数的顺序
        x, y= 0, 0
        for key in ANGLE_NUM.keys():
            value = ANGLE_NUM[key]
            dm_ret = self.dm.FindShapeEx(25, 554, 75, 574, value, 1, 3)
            count = self.dm.GetResultCount(dm_ret)
            if count == 0:
                continue
            ret = self.dm.GetResultPos(dm_ret, 0, x, y)
            angle_dict[ret[1]] = key
            
            if count == 2:
                ret = self.dm.GetResultPos(dm_ret, 1, x, y)
                angle_dict[ret[1]] = key

        angle = ''
        negatiave_flag = False #
        for i in sorted(angle_dict):
            if angle_dict[i] == '-':
                negatiave_flag = True
                continue
            angle += str(angle_dict[i])
        if angle == '':
            print(0)

        if negatiave_flag:
            return -(int(angle))
        return int(angle)


    def send_str(self, str):
        self.set_window_state(1)
        ret = self.dm.SendString(self.hwnd, str)
        print("send ret:", ret)

    def _excute_key(self, key):
        if key.isdigit():
                key = ord(key)
        elif key.isalpha():
            key = ord(key.upper())
        self.dm.KeyDown(key)
        self.dm.KeyUp(key)

    def key_input(self, key):
        if len(key) == 1: # 单个字符（字母或者数字）
            self._excute_key(key)
        elif key == "enter":
            # 需要两次press 不知道为什么
            self.dm.KeyPress(ENTER)
            self.dm.KeyPress(ENTER)
        else: #字母和数字混合
            for i in key:
                self._excute_key(i)


    def shoot(self, angle, shoot, buff):
        # time.sleep(2)
        # 毫米级检测是否达到目标力度
        # s = 0
        # for i in range(160, 650):
        # if window.cmp_color(i, 610) == 0:
        #     s = (i-150) * 0.2
        # 4秒可以100力， 每力0.04s
        # pyautogui.keyDown('space')
       
        # time.sleep((vigour - 2) * 0.04)
        
        # while True: # 不匹配
        #     # 正负1力误差
        #     for i in range(150 + (vigour-1) * 5, 150 + (vigour+1) * 5):
        #         if self.cmp_color(i, 610) == 0:
        #             pyautogui.keyUp('space')
        #             print(time.time())
        #             return 

        # 暴力按照时间估计 达到了预计的力度
        # pyautogui.keyDown('space')
        # time.sleep((shoot - 2) * 0.04)
        # pyautogui.keyUp('space')
        self._set_angle(angle)
        self._set_buff(buff)
        self._set_shoot(shoot)
        
       
    
    def _set_angle(self, target_angle):
        if self.user.angle != None:
            angle = self.user.angle
        else:
            angle = self._ocr_angle()
            
        diff_angle = int(target_angle) - int(angle)
        print(angle, diff_angle)
        if diff_angle < 0:
            self._agjust_angle(diff_angle, 0)
        else:
            self._agjust_angle(diff_angle, 1)

    def _agjust_angle(self, diff_angle, mode):
        # 0 : down ; 1 : up
        if mode == 0:
            for i in range(diff_angle):
                self.key_input("s")
            
        else:
            for i in range(diff_angle):
                self.key_input("w")
    
    def _set_shoot(self, shoot):
        delay = (shoot+1) * 40 # ms
        self.dm.SetKeypadDelay(self.keypad, delay)
        self.dm.KeyPress(SPACE)

    def _set_buff(self, buff):
        self.key_input(buff)

    def _key_space(self):
        self.key_press(32, mode=0)
        time.sleep(1)
        self.key_up(32, mode=0)
    
    # 按下一个键
    def _key_down(self, key, mode=0, method=1):
        if method == 0:
            if mode == 0:
                ret = self.dm.KeyDown(key)
                print("key down ret " + str(ret) + " 1 is suc")
            elif mode == 1:
                ret = self.dm.KeyDownChar(key)
                # print("key press char ret " + str(ret) + " 1 is suc")
        else:
            win32api.SendMessage(self.hwnd, win32con.WM_KEYDOWN, key, 0)
            win32api.SendMessage(self.hwnd, win32con.WM_KEYUP, key, 0)
        time.sleep(0.02)
       

    def _key_up(self, key, mode=1):
        if mode == 0:
            ret = self.dm.KeyUp(key)
            print("key down ret " + str(ret) + " 1 is suc")
        elif mode == 1:
            ret = self.dm.KeyUpChar(key)

    
    def _key_press(self, key, mode=0):
        # mode 0: 数字直接转字符集，mode 1: 字母 这样才和dm对齐
        if mode == 0:
            ret = self.dm.KeyPress(key)
            print("key: " +str(key) +" down ret " + str(ret) + "。 1 is suc")
        elif mode == 1:
            ret = self.dm.KeyPressChar(key)
            print("key: " +str(key) +" down ret " + str(ret) + "。 1 is suc")
       
        time.sleep(0.02)
    
    def set_window_state(self, flag):

        ret = self.dm.SetWindowState(self.hwnd, flag)
        print("set window state :", flag, str(ret))
        time.sleep(0.2)
        return ret #1 suc

    def get_window_state(self, flag):
        ret = self.dm.GetWindowState(self.hwnd, flag)
        time.sleep(0.2)
        return ret
    
    def _write_zero_file(self, file_addr):
         with open('zero.txt', 'a', encoding='utf-8') as f:
            f.write(file_addr)
            f.write('\n')
            f.close() 

    def cmp_color(self, x, y, sim=0.9):
        return self.dm.CmpColor(x, y, "db6d22-000000|bd7d23-000000|df9148-000000", sim)
    # # 筛选后的 获取数据，需要提供不需要读的文件名信息
    # def read_data_ex(self):
    #     not_read_list = []
    #     filename_1 = "not_same.txt"
    #     filename_2 = "zero_same.txt"

    #     f1 = open(filename_1, 'r')
    #     line = f1.readline()
    #     while True:
    #         line = f1.readline()[0:-1]
    #         if not line:
    #             break
    #         not_read_list.append(line)

    #     f2 = open(filename_2)
    #     line = f2.readline()
    #     while line:
    #         line = f2.readline()[0:-1]
    #         if not line:
    #             break
    #         not_read_list.append(line)
        
    #     not_read_list.sort()
    #     print(type(not_read_list))


    #     addr = "00000000"
    #     len = "1000"  #10000
    
    #     over = "FFFFFFFF" 
    #     ten_len  = int(len, 16)
    #     not_read_index = 0

    #     while int(addr, 16) + int(len, 16) <= int(over, 16):
    #         if not os.path.exists(self.user.username):
    #             os.makedirs(self.user.username)
    #         file_addr = str(addr).zfill(8) + "_" + hex((int(addr, 16) + int(len, 16)))[2:].zfill(8)
    #         if file_addr == not_read_list[not_read_index]:
    #             not_read_index += 1
    #         else:
    #             filename = self.user.username  +"3\\" + file_addr + ".txt"
    #             ret = self.dm.ReadData(self.hwnd, addr, ten_len)
    #             if ret != "":
    #                 with open(filename, 'a', encoding='utf-8') as f:
    #                     f.write(ret)
    #                 f.close()
                
            
    #         ten_addr = int(addr, 16) + int(len, 16)
    #         addr = hex(ten_addr)[2:]   

    # # 整个内存数据 全部读取
    # def read_data(self):
    #     addr = "00000000"
    #     len = "1000"  #10000
    
    #     over = "FFFFFFFF" 
    #     ten_len  = int(len, 16)
        

    #     # zero_file_name = []
    #     while int(addr, 16) + int(len, 16) <= int(over, 16):
    #         if not os.path.exists(self.user.username):
    #             os.makedirs(self.user.username)
    #         file_addr = str(addr).zfill(8) + "_" + hex((int(addr, 16) + int(len, 16)))[2:].zfill(8)
    #         filename = self.user.username  +"4\\" + file_addr + ".txt"

    #         ret = self.dm.ReadData(self.hwnd, addr, ten_len)
    #         if ret != "":
    #             with open(filename, 'a', encoding='utf-8') as f:
    #                     f.write(ret)
    #             f.close()
            
           
    #         ten_addr = int(addr, 16) + int(len, 16)
    #         addr = hex(ten_addr)[2:]
    
    # # 比较两次运行（两个目录的文件名都一样） 不一样的数据，保存文件名
    # def cmp(self):
    #     addr = "00000000"
    #     len = "1000"
    #     over = "FFFFFFFF" 
    #     file_addr = str(addr).zfill(8) + "_" + hex((int(addr, 16) + int(len, 16)))[2:].zfill(8)

    #     filename_1 = self.user.username  +"\\" + file_addr + ".txt"
    #     filename_2 = self.user.username  +"2\\" + file_addr + ".txt"
    #     filename_3 = "not_same.txt"
    #     if os.path.exists(filename_3):
    #         print(filename_3 + "is exist")
    #         return

    #     while int(addr, 16) + int(len, 16) <= int(over, 16):
    #         # print(filename_1, filename_2)
    #         if os.path.exists(filename_1) and os.path.exists(filename_2):
    #             print(filename_1, filename_2)
    #             txt_1 = ""
    #             txt_2 = ""
    #             with open(filename_1, 'r', encoding='utf-8') as f:
    #                 txt_1 = f.read()
    #                 f.close()
    #             with open(filename_2, 'r', encoding='utf-8') as f:
    #                 txt_2 = f.read()
    #                 f.close()

    #             if txt_1 != txt_2:
    #                 print(file_addr)
    #                 with open(filename_3, 'a', encoding='utf-8') as f:
    #                     f.write(file_addr)
    #                     f.write('\n')
    #                     f.close()

    #         ten_addr = int(addr, 16) + int(len, 16)
    #         addr = hex(ten_addr)[2:]

    #         file_addr = str(addr).zfill(8) + "_" + hex((int(addr, 16) + int(len, 16)))[2:].zfill(8)
    #         filename_1 = self.user.username  +"\\" + file_addr + ".txt"
    #         filename_2 = self.user.username  +"2\\" + file_addr + ".txt"
    
    # # 比较两次运行（两个目录的文件名包含的关系） 不一样的数据，保存文件名
    # def cmp_ex(self):
    #     addr = "00000000"
    #     len = "1000"
    #     over = "FFFFFFFF" 
    #     file_addr = str(addr).zfill(8) + "_" + hex((int(addr, 16) + int(len, 16)))[2:].zfill(8)

    #     filename_1 = self.user.username  +"3\\" + file_addr + ".txt"
    #     filename_2 = self.user.username  +"4\\" + file_addr + ".txt"
    #     filename_3 = "second_not_same.txt"
    #     # if os.path.exists(filename_3):
    #     #     print(filename_3 + "is exist")
    #     #     return

    #     while int(addr, 16) + int(len, 16) <= int(over, 16):
    #         # print(filename_1, filename_2)
    #         # 如果filename_1存在，在进行比较
            
    #         if os.path.exists(filename_1) and os.path.exists(filename_2):
    #             print(filename_1, filename_2)
    #             txt_1 = ""
    #             txt_2 = ""
    #             with open(filename_1, 'r', encoding='utf-8') as f:
    #                 txt_1 = f.read()
    #                 f.close()
    #             with open(filename_2, 'r', encoding='utf-8') as f:
    #                 txt_2 = f.read()
    #                 f.close()

    #             if txt_1 != txt_2:
    #                 print(file_addr)
    #                 with open(filename_3, 'a', encoding='utf-8') as f:
    #                     f.write(file_addr)
    #                     f.write('\n')
    #                     f.close()

    #         ten_addr = int(addr, 16) + int(len, 16)
    #         addr = hex(ten_addr)[2:]

    #         file_addr = str(addr).zfill(8) + "_" + hex((int(addr, 16) + int(len, 16)))[2:].zfill(8)
    #         filename_1 = self.user.username  +"3\\" + file_addr + ".txt"
    #         filename_2 = self.user.username  +"4\\" + file_addr + ".txt"

    # # 比较两次运行（两个目录的文件名都一样） 数据为0，保存文件名
    # def cmp_zero(self):
    #     addr = "00000000"
    #     len = "1000"
    #     over = "FFFFFFFF" 
    #     file_addr = str(addr).zfill(8) + "_" + hex((int(addr, 16) + int(len, 16)))[2:].zfill(8)

    #     filename_1 = self.user.username  +"\\" + file_addr + ".txt"
    #     filename_2 = self.user.username  +"2\\" + file_addr + ".txt"
    #     filename_3 = "zero_same.txt"
    #     if os.path.exists(filename_3):
    #         print(filename_3 + "is exist")
    #         return
        
    #     temp_ret = ""
    #     with open("sample.txt", 'r', encoding='utf-8') as f:
    #         temp_ret = f.read()
    #         f.close()

    #     while int(addr, 16) + int(len, 16) <= int(over, 16):
    #         if os.path.exists(filename_1) and os.path.exists(filename_2):
    #             print(filename_1, filename_2)
    #             txt_1 = ""
    #             txt_2 = ""
    #             with open(filename_1, 'r', encoding='utf-8') as f:
    #                 txt_1 = f.read()
    #                 f.close()
    #             with open(filename_2, 'r', encoding='utf-8') as f:
    #                 txt_2 = f.read()
    #                 f.close()

    #             if txt_1 == txt_2 and txt_1 == temp_ret:
    #                 print(file_addr)
    #                 with open(filename_3, 'a', encoding='utf-8') as f:
    #                     f.write(file_addr)
    #                     f.write('\n')
    #                     f.close()

    #         ten_addr = int(addr, 16) + int(len, 16)
    #         addr = hex(ten_addr)[2:]

    #         file_addr = str(addr).zfill(8) + "_" + hex((int(addr, 16) + int(len, 16)))[2:].zfill(8)
    #         filename_1 = self.user.username  +"\\" + file_addr + ".txt"
    #         filename_2 = self.user.username  +"2\\" + file_addr + ".txt"

    # Picutre
    def _find_pic(self, pic_name):
        x, y =0, 0
        ret = self.dm.FindPic(0, 0, 1004, 628, pic_name + ".bmp", "000000", 0.9, 0, x, y)
        if ret[0] == -1:
            return -1, 0, 0
        # print("find", ret[1], ret[2])
        return ret[0], ret[1], ret[2]
    

    def is_time_to_shoot(self):
        is_find, _, _ = self._find_pic("pass")
        if is_find == 0:
            return True
        return False

    # 获取 怪物 坐标
    # 1.获取 怪物红点的左边
    # 2.获取 移动框的大小
    # 3.获取 地图的大小
    # 4.计算位置
    def get_monster_position(self):
        
        new_monster_position_list = self._get_red_pos()
        
        moveabled_window_list     = self._get_moveabled_window_size()
        stabled_window_list       = self._get_stabled_window_size()


        print("monster", new_monster_position_list)
        print("moved", moveabled_window_list)
        print("stabled",stabled_window_list)

        # 将左上角坐标 转 中心左边            
        # for i, pos in enumerate(new_monster_position_list):
        #     new_monster_position_list[0] = pos[0] + int(wigth / 2) # tuple不可变
        #     new_monster_position_list[1] = pos[1] + int(height / 2)

        # return new_monster_position_list

    def _get_red_pos(self):
        color = RAD_COLOR
        count = 28
        wigth = 7
        height = 7
        x, y = 0, 0
        # 获取红色（怪物）色块区域
        monster_position_list = []
        self._capture_jpg(x1=790, y1=0, x2=1004, y2=125)
        ret = self.dm.FindColorBlockEx(790, 0, 1004, 125, color,  0.9,  count, wigth, height)
        count = self.dm.GetResultCount(ret)
        for  i in range(count):
            dm_ret = self.dm.GetResultPos(ret, i, x, y)
            # print(dm_ret[1], dm_ret[2])
            monster_position_list.append((dm_ret[1], dm_ret[2]))
        monster_position_list.sort()

        new_monster_position_list = []

        step = 1
        index = 0

        # 细分，上一步会出现两个结果只相差1像素，不合理
        while True:
            if index + step < len(monster_position_list):
                if monster_position_list[index + step][0] <= monster_position_list[index][0] + 1:
                    step += 1
                else:
                    new_monster_position_list.append(monster_position_list[index])
                    index += step
                    step = 1
            else:
                new_monster_position_list.append(monster_position_list[index])
                break
        return new_monster_position_list

    def _get_moveabled_window_size(self):
        moveabled_window_list = [] # x坐标：力度值，通过左边判断 找到的数的顺序
        x, y= 0, 0
        for key in MOVEABLED_WINDOW.keys():
            value = MOVEABLED_WINDOW[key]
            dm_ret = self.dm.FindShapeEx(750, 25, 1000, 300, value, 0.9, 0)
            count = self.dm.GetResultCount(dm_ret)
            if count == 0:
                print(key)
            elif count > 1:  
                print(key, "count > 1")
                ret = self.dm.GetResultPos(dm_ret, 0, x, y)
                for i in range(count):
                    a = self.dm.GetResultPos(dm_ret, i, x, y)
                    print(a)
            elif count == 1:
                ret = self.dm.GetResultPos(dm_ret, 0, x, y)
                moveabled_window_list.append((ret[1], ret[2]))
         
        moveabled_window_list.sort()
        return moveabled_window_list
    
    def _get_stabled_window_size(self):
        stabled_window_list = [] # x坐标：力度值，通过左边判断 找到的数的顺序
        for key in STABLED_WINDOW.keys():
            value = STABLED_WINDOW[key]
            ret = self.dm.FindMultiColorE(750, 0, 1000, 25, key, value, 1, 0)
            stabled_window_list.append(ret)
        return stabled_window_list
         
    def get_self_position(self):
        pass
    