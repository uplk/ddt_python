
from multiprocessing import Process
import multiprocessing
from threading import Thread
import threading
import win32gui
import win32api
import time
import win32process
from mWindow import mWindow
from mWindows import mWindows
from mHwnd import mHwnd
import psutil

ENTER = "enter"

def init(windows_object):

    # 获取运行中的 进程id#
    # 只获取和36脚本相关的进程
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name().startswith("36脚本"):
            window = mWindow()
            window.init_process(p)
            windows_object.all_windows[pid] = window

    hwnd_title = dict()

    # 获取每个进程的 窗口信息，并对每个窗口进行dm初始化
    def get_all_hwnd(hwnd, mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({hwnd : win32gui.GetWindowText(hwnd)})
            _, process_id = win32process.GetWindowThreadProcessId(hwnd)

           
            if(windows_object.all_windows.get(process_id)):
                hwnd_content = win32gui.GetWindowText(hwnd).split('|')
                # if len(hwnd_content) < 6:
                #     windows_object.all_windows.pop(process_id)
                # else:
                ret = windows_object.all_windows[process_id].init_dm_user(hwnd, hwnd_content) 
                if ret == 0: # init失败
                    windows_object.all_windows.pop(process_id)
                # windows_object.all_windows[process_id].init_user(hwnd)
                window = windows_object.all_windows[process_id]
                windows_object.windows_create_time[process_id] = window.create_time
            else:    

                # print("error")
                pass
    
    win32gui.EnumWindows(get_all_hwnd, 0)

    windows_object.sort_windows_create_time()
    # print(hwnd_title)

    # return windows_object

def window_do_task(window, lock):
    # window._find_pic("icon17")
    ret = window.get_monster_position()
    # for r in ret:
    #     print(r)
    # window.click_pic("战斗")
    # window.click_pic("远征码头")
    # window.click_pic("创建房间")
    # window.click_pic("选择地图")
    # window.click_pic("蚂蚁")
    # window.click_pic("简单")
    # window.click_pic("确定")
    # window.click_pic("副本开始")
    # # window.click_pic("不再提示")
    # window.click_pic("确定")
    # while True:
    #     if window.is_time_to_shoot():
    #         # window.key_input("124")  
    #         angle = 30
    #         force = 50 
    #         buff = "b124"
    #         window.shoot(angle, force, buff)

    #     window.get_monster_position()
    # angle = 40
    # force = 50 
    # buff = "zb1234"
    # window.shoot(angle, force, buff)
    
   

    window_end_task(window)

def window_end_task(window):
    return window.dm.UnBindWindow()

class MyThread(Thread):
    
    def __init__(self, func, args, ):
        Thread.__init__(self)
        self.func = func
        self.args = args
    
    def run(self):
        # for i in range(10):
            # print(str(i) + " i am" + self.name)
        # print(self.name)
        self.func(*self.args)

if(__name__=="__main__"):
    windows_object = mWindows()
    init(windows_object)
    lock = threading.Lock()

    thread_list = []
    for window in windows_object.all_windows.values():
        t = MyThread(window_do_task, (window, lock,))
        thread_list.append(t)
    
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()

    # process_list = []
    # for window in windows_object.all_windows.values():
    #     p = Process(target=window_do_task, args=(window, lock,))
    #     p.start()
    #     process_list.append(p)
    #     # thread_list.append(t)
    
    # for p in process_list:
    #     p.join()
    # process_list = []
    # for window in windows_object.all_windows.values():
    #     process = multiprocessing.Process(target=window_do_task, args=(window,lock,))
    #     process_list.append(process)
    #     process.start()
    
    # for p in process_list:
    #     p.start()
