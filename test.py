# import win32com.client
# import time

# # 29008
# dm = win32com.client.Dispatch("dm.dmsoft")

# # dm = win32com.client.Dispatch("ts.tssoft")
# # dm = win32com.client.("dm.dmsoft")
# # hwnd = 135032
# # print(dm.ver())
# ret = dm.Reg("lumiku2fdc744d96597f65888674a63fb3489a", "yk65792928")
# if ret == 0:
#     print("Reg error:" )        

# # 27005396


# ret = dm.BindWindowEx(2166918, "gdi","windows3","windows","",101)
# print(ret)
# dm.SetWindowState(9831692, 1)

# # ret = dm.SetWindowState(hwnd, 1)
# # print("set ret", ret, ":1 is suc")

# # dm.SetKeypadDelay("windows", 100)
# dm.KeyPress(81)

# # dm.KeyPress(81)


# # dm.KeyUp(81)




# # for i in hwnd:
# #     print(i)



from threading import Thread
import requests
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
       
# reps = requests.get("http://cdnres.ddt.1322game.com/image/interfaceicons/icon12.png?nlv=14.9.18")
# print(reps.status_code)

# filename="./resources/test.png"
# import os
# # if not os.path.exists(filename):
# #     os.makedirs(filename)

# with open(filename, 'wb') as f:
#     f.write(reps.content)

import os
import time
# http://cdnres.ddt.1322game.com/image/equip/f/head/head124/icon_1.png?nlv=14.9.18
# hair glass cloth face eff offhand
# http://cdnres.ddt.1322game.com/image/arm/boomerang/1/icon.png?nlv=14.9.18
i = 0
# furl = "http://cdnres.ddt.1322game.com/image/petskill/"+ i +"/icon.png?nlv=14.9.18"


def download(url):
    furl  = ""
    i=0
    for i in range(0, 10000):
       
        if url == "http://cdnres.ddt.1322game.com/image/equip/f/hair/hair0/icon_1.png?nlv=14.9.18":
            furl = "http://cdnres.ddt.1322game.com/image/equip/f/hair/hair{index}/icon_1.png?nlv=14.9.18".format(index=str(i))
        elif url == "http://cdnres.ddt.1322game.com/image/equip/f/glass/glass0/icon_1.png?nlv=14.9.18":
            furl = "http://cdnres.ddt.1322game.com/image/equip/f/glass/glass{index}/icon_1.png?nlv=14.9.18".format(index=str(i))

        elif url == "http://cdnres.ddt.1322game.com/image/equip/f/cloth/cloth0/icon_1.png?nlv=14.9.18":
            furl = "http://cdnres.ddt.1322game.com/image/equip/f/cloth/cloth{index}/icon_1.png?nlv=14.9.18".format(index=str(i))

        elif url ==    "http://cdnres.ddt.1322game.com/image/equip/f/face/face0/icon_1.png?nlv=14.9.18":
            furl = "http://cdnres.ddt.1322game.com/image/equip/f/face/face{index}/icon_1.png?nlv=14.9.18".format(index=str(i))

        elif url ==    "http://cdnres.ddt.1322game.com/image/equip/f/eff/eff0/icon_1.png?nlv=14.9.18":
            furl = "http://cdnres.ddt.1322game.com/image/equip/f/eff/eff{index}/icon_1.png?nlv=14.9.18".format(index=str(i))

        elif url ==   "http://cdnres.ddt.1322game.com/image/equip/f/offhand/offhand0/icon_1.png?nlv=14.9.18":
            furl = "http://cdnres.ddt.1322game.com/image/equip/f/offhand/offhand{index}/icon_1.png?nlv=14.9.18".format(index=str(i))
            
        elif url ==   "http://cdnres.ddt.1322game.com/image/arm/boomerang/1/icon.png?nlv=14.9.18":
            furl = "http://cdnres.ddt.1322game.com/image/arm/boomerang/{index}/icon.png?nlv=14.9.18".format(index=str(i))

        elif url ==   "http://cdnres.ddt.1322game.com/image/equip/m/hair/hair0/icon_1.png?nlv=14.9.18":
            furl = "http://cdnres.ddt.1322game.com/image/equip/m/hair/hair{index}/icon_1.png?nlv=14.9.18".format(index=str(i))

        elif url ==   "http://cdnres.ddt.1322game.com/image/equip/m/glass/glass0/icon_1.png?nlv=14.9.18":
            furl = "http://cdnres.ddt.1322game.com/image/equip/m/glass/glass{index}/icon_1.png?nlv=14.9.18".format(index=str(i))

        elif url ==  "http://cdnres.ddt.1322game.com/image/equip/m/cloth/cloth0/icon_1.png?nlv=14.9.18":
            furl = "http://cdnres.ddt.1322game.com/image/equip/m/cloth/cloth{index}/icon_1.png?nlv=14.9.18".format(index=str(i))

        elif url ==  "http://cdnres.ddt.1322game.com/image/equip/m/face/face0/icon_1.png?nlv=14.9.18":
            furl = "http://cdnres.ddt.1322game.com/image/equip/m/face/face{index}/icon_1.png?nlv=14.9.18".format(index=str(i))

        elif url ==  "http://cdnres.ddt.1322game.com/image/equip/m/eff/eff0/icon_1.png?nlv=14.9.18":
            furl = "http://cdnres.ddt.1322game.com/image/equip/m/eff/eff{index}/icon_1.png?nlv=14.9.18".format(index=str(i))

        elif url ==  "http://cdnres.ddt.1322game.com/image/equip/m/offhand/offhand0/icon_1.png?nlv=14.9.18":
            furl = "http://cdnres.ddt.1322game.com/image/equip/m/offhand/offhand{index}/icon_1.png?nlv=14.9.18".format(index=str(i))

    
        # furl = "http://cdnres.ddt.1322game.com/image/map/{index}/dead.png?nlv=14.9.18".format(index=str(i))
        reps = requests.get(furl)
        code = reps.status_code 
        
        if code == 200:
            # pass
            os.system(r' "D:\Install\utils\Thunder-Network\\Thunder\\Program\\ThunderStart.exe" {url}'.format(url=furl))
            time.sleep(0.01)
            # time.sleep(1)
        else:
            print(url, i, code)

# urls = ["http://cdnres.ddt.1322game.com/image/equip/f/hair/hair0/icon_1.png?nlv=14.9.18",
#         "http://cdnres.ddt.1322game.com/image/equip/f/glass/glass0/icon_1.png?nlv=14.9.18",
#         "http://cdnres.ddt.1322game.com/image/equip/f/cloth/cloth0/icon_1.png?nlv=14.9.18",
#         "http://cdnres.ddt.1322game.com/image/equip/f/face/face0/icon_1.png?nlv=14.9.18",
#         "http://cdnres.ddt.1322game.com/image/equip/f/eff/eff0/icon_1.png?nlv=14.9.18",
#         "http://cdnres.ddt.1322game.com/image/equip/f/offhand/offhand0/icon_1.png?nlv=14.9.18",
        
#         "http://cdnres.ddt.1322game.com/image/arm/boomerang/1/icon.png?nlv=14.9.18",

#         "http://cdnres.ddt.1322game.com/image/equip/m/hair/hair0/icon_1.png?nlv=14.9.18",
#         "http://cdnres.ddt.1322game.com/image/equip/m/glass/glass0/icon_1.png?nlv=14.9.18",
#         "http://cdnres.ddt.1322game.com/image/equip/m/cloth/cloth0/icon_1.png?nlv=14.9.18",
#         "http://cdnres.ddt.1322game.com/image/equip/m/face/face0/icon_1.png?nlv=14.9.18",
#         "http://cdnres.ddt.1322game.com/image/equip/m/eff/eff0/icon_1.png?nlv=14.9.18",
#         "http://cdnres.ddt.1322game.com/image/equip/m/offhand/offhand0/icon_1.png?nlv=14.9.18"]


# thread_list = []
# for url in urls:
#     t = MyThread(download, (url,))
#     thread_list.append(t)

# for t in thread_list:
#     t.start()
# for t in thread_list:
#     t.join()

# E:\电视剧
# dir_path = "E:/电视剧"
# file_list = os.listdir(dir_path)
# from PIL import Image
# l = []
# for file in file_list:
#     if file.startswith("dead"):
#         try:
#             file = os.path.join(dir_path, file)
#             im = Image.open(file)
#             l.append(( im.size[0], im.size[1],file))
#         except IOError:
#             print(file, "filed")

# l.sort()
# for i in l:
#     print(i)

furl  = ""
i=0
for i in range(0, 20000):
    furl = "http://cdnres.ddt.1322game.com/image/map/{index}/show1.jpg?nlv=14.9.18".format(index=str(i))
    reps = requests.get(furl)
    code = reps.status_code 
    print(furl, code)
    if code == 200:
        # pass

        os.system(r'"D:/Install/utils/Thunder-Network/Thunder/Program/ThunderStart.exe" {url}'.format(url=furl))
        time.sleep(0.01)
        # time.sleep(1)
    else:
        print(furl, i, code)