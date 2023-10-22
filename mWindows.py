class mWindows:
    
    def __init__(self):
        self.all_windows = dict() # map： pid -> window
        self.username_windows = dict() # username -> window
        self.windows_create_time = dict() # pid -> create_time    
    
    def print_mWindows(self):
        for process, window in self.all_windows.items():
            print(process, window.hwnd, window.hwnd_content)

    # 根据名字 获取 窗口
    def get_window_by_name(self, username):
        if username not in self.username_windows.keys():
            for _, window in self.all_windows.items():
                if window.user.username == username:
                    self.username_windows[username] = window
           
        return self.username_windows[username]

    def sort_windows_create_time(self):
        
        windows_create_time_list = sorted(self.windows_create_time.items(), key=lambda x:x[1])
        num = 1
        for (k, v) in windows_create_time_list:
            self.all_windows[k].sort_num = num
            # print(kv)
            num += 1
       
        # for key in self.windows_create_time.keys():
        #     self.all_windows[key].sort_num = num
            
        
        # for v in self.all_windows.values():
        #     print(v.user.username, v.create_time, v.pid, v.sort_num)
        
       


