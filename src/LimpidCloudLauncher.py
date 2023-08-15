import json
import os
import threading
import requests
import psutil

import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Style

MainWind = Style(theme='cyborg').master
# Game Par
Ram = psutil.virtual_memory()
Rams = float(Ram.total) / 1024 / 1024 / 1024
MinecraftVersionsGet = requests.get('https://bmclapi2.bangbang93.com/mc/game/version_manifest.json').text
MinecraftVersions = json.loads(MinecraftVersionsGet)

# Games & Participation
GetGameVersions = ttk.Combobox(MainWind, state="readonly", )
GetGameVersions['values'] = ("请选择版本")
GetGameVersions.current(0)
GetJava = ttk.Combobox(MainWind, state="readonly", )
GetJava['values'] = ("请选择Java")
GetJava.current(0)
Settings = ttk.Button(MainWind, text="设置", takefocus=False,)
Downloads = ttk.Button(MainWind, text="下载", takefocus=False)
Content = ttk.LabelFrame(MainWind,text="提示",)
GetGameAllFile = ttk.Checkbutton(MainWind,text="检查游戏完整性",)
DownAllGameFile = ttk.Checkbutton(MainWind,text="尝试替换本地库文件",)
VersionsSetting = ttk.Button(MainWind, text="版本设置", takefocus=False,)
Mods = ttk.Button(MainWind, text="模组", takefocus=False,)
SetRamLabel = ttk.Label(MainWind,text="设置内存 (GB)",anchor="center", )
SetRam = ttk.Entry(MainWind, text='4')
SetRam.insert(0,f'{str(Rams)[0:4]}')
GenuineLogin = ttk.Button(MainWind, text="正版登录", takefocus=False,)
GetNameNo = ttk.Entry(MainWind, )
GetNameNoLabel = ttk.Label(MainWind,text="设置游戏名字 (离线)",anchor="center", )
GetNameNo.insert(0,f'TEST')
LoginQY = ttk.Button(MainWind, text="登录清云账号", takefocus=False,)
GetWe = ttk.Button(MainWind, text="关于", takefocus=False,)
Agreement = ttk.Radiobutton(MainWind,text="同意遵守《清云软件使用协议》",)
QuitButton = ttk.Button(MainWind, text="X", takefocus=False,command=quit,bootstyle=DANGER)
TitleLabel = ttk.Label(MainWind,text="LimpidCloudLauncher",anchor="center", )

TabFrame_0 = tk.Frame()
TabFrame_0.place(x=130, y=310, width=343, height=92)
TabFrame_1 = tk.Frame()
TabFrame_1.place(x=130, y=310, width=343, height=92)
Label_0 = tk.Label(Content,text=f'Minecraft已经更新了{len(MinecraftVersions["versions"])}个版本',anchor="center")

TabFrame = ttk.Notebook(MainWind)
TabFrame.add(TabFrame_0, text="清云动态")
TabFrame.add(TabFrame_1, text="Minecraft动态")

# Start Game Module
StartGameButton = ttk.Button(MainWind, text="启动游戏", takefocus=False,)

# All control layouts
StartGameButton.place(x=480, y=370, width=168, height=31)
GetGameVersions.place(x=480, y=40, width=170, height=31)
Settings.place(x=10, y=371, width=108, height=29)
Downloads.place(x=10, y=333, width=108, height=30)
Content.place(x=9, y=32, width=465, height=208)
TabFrame.place(x=130, y=310, width=343, height=92)
GetGameAllFile.place(x=480, y=74, width=110, height=23)
DownAllGameFile.place(x=480, y=100, width=134, height=20)
Label_0.place(x=0, y=0)
VersionsSetting.place(x=480, y=130, width=79, height=35)
Mods.place(x=565, y=130, width=82, height=35)
GetJava.place(x=480, y=170, width=170, height=26)
SetRamLabel.place(x=480, y=200, width=167, height=24)
SetRam.place(x=480, y=230, width=168, height=25)
GenuineLogin.place(x=480, y=330, width=168, height=30)
GetNameNo.place(x=480, y=290, width=168, height=27)
GetNameNoLabel.place(x=480, y=260, width=167, height=24)
LoginQY.place(x=10, y=292, width=109, height=32)
GetWe.place(x=10, y=247, width=463, height=37)
Agreement.place(x=280, y=285, width=192, height=32)
QuitButton.place(x=620, y=0, width=31, height=31)
TitleLabel.place(x=0, y=0, width=149, height=28)

# Window
MainWind.overrideredirect (True) 
MainWind.geometry("653x410+374+182")
MainWind.resizable(False,False)
MainWind.mainloop()
