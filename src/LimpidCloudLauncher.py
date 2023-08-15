import json
import os
import threading
import requests
import psutil

import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Style

def CreatFile():
    UserGetUUID = requests.get("https://www.uuidtools.com/api/generate/timestamp-first").text
    UserUUID = UserGetUUID[3:-3]

    MinecraftVersionsGet = requests.get('https://bmclapi2.bangbang93.com/mc/game/version_manifest.json').text
    MinecraftVersions = json.loads(MinecraftVersionsGet)

    if os.path.isdir('.minecraft/') == False:
        os.makedirs('.minecraft')
    if os.path.isdir('.minecraft/assets') == False:
        os.makedirs('.minecraft/assets')
    if os.path.isdir('.minecraft/resourcepacks') == False:
        os.makedirs('.minecraft/resourcepacks')
    if os.path.isdir('.minecraft/saves') == False:
        os.makedirs('.minecraft/saves')
    if os.path.isdir('.minecraft/mods') == False:
        os.makedirs('.minecraft/mods')
    if os.path.isdir('.minecraft/logs') == False:
        os.makedirs('.minecraft/logs')
    if os.path.isdir('.minecraft/libraries') == False:
        os.makedirs('.minecraft/libraries')
    if os.path.isdir('.minecraft/versions') == False:
        os.makedirs('.minecraft/versions')
    if os.path.isdir('.mtl') == False:
        os.makedirs('.mtl')
    if os.path.isfile('.mtl/config.json') == False:
        Test = {"mojang":False,"alpha":0.95,"source":"bmcl","Java":{"versions":"8","path":""},"hints":["MTL是用py写的","MTL历史上重构过3次哦!"],"Game":{"Code":"eyJ0eXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXQv-VA","JavaPath":"","Xmx":2,"G1GC":True,"username":"test","version":"","gameDir":"","assetsDir":"","assetIndex":"","uuid":UserUUID,"accessToken":"","userType":"","versionType":"release","width":"854","height":"480"},"author":"陆御"}
        with open('.mtl/config.json','w',encoding='utf-8') as f:
            fe = json.dumps(Test,sort_keys=True, indent=4, separators=(',', ':'))
            f.write(fe)
            f.close()
    if os.path.isfile('.mtl/config.txt') == False:
        with open('.mtl/config.txt','w',encoding='utf-8') as f:
            f.write('"<JavawPath>" -XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe.heapdump"\n\
 -Dos.name=Windows 10"\n\
 -Dos.version=10.0 -Xms1M\n\
 -Djava.library.path=<nativespath> \n\
 -Dminecraft.launcher.brand=MinecraftTechLauncher\n\
 -Dminecraft.launcher.version=4.0.1\n\
 -cp <CpLib>\n\
 -Xmx<XmxPy>\n\
 -XX:+UnlockExperimentalVMOptions\n\
 -XX:+UseG1GC\n\
 -XX:G1NewSizePercent=20\n\
 -XX:G1ReservePercent=20\n\
 -XX:MaxGCPauseMillis=50\n\
 -XX:G1HeapRegionSize=32M\n\
 -Dlog4j.configurationFile=<log4jFile> <mainClass>\n\
 --username <UserNamePy>\n\
 --version <VersionPy>\n\
 --gameDir <GameDirPy>\n\
 --assetsDir <assetsDirPy>\n\
 --assetIndex <assetIndexPy>\n\
 --uuid <uuidPy>\n\
 --accessToken <accessTokenPy>\n\
 --userType <userTypePy>\n\
 --versionType <versionTypePy>\n\
 --width <widthPy>\n\
 --height <heightPy>')
            f.close()

MainWind = Style(theme='cyborg').master
# Game Par
Ram = psutil.virtual_memory()
Rams = float(Ram.total) / 1024 / 1024 / 1024
MinecraftVersionsGet = requests.get('https://bmclapi2.bangbang93.com/mc/game/version_manifest.json').text
MinecraftVersions = json.loads(MinecraftVersionsGet)
MinecraftVersionsList = ["请选择版本"]
MinecraftVersionsListOS = os.listdir('.minecraft/versions')
MinecraftVersionsList.append(MinecraftVersionsListOS)
MinecraftVersionsTuple = tuple(MinecraftVersionsList)

# Games & Participation
GetGameAllFileVar = tk.StringVar()
DownAllGameFileVar = tk.StringVar()

GetGameVersions = ttk.Combobox(MainWind, state="readonly", )
GetGameVersions['values'] = MinecraftVersionsTuple
GetGameVersions.current(0)
GetJava = ttk.Combobox(MainWind, state="readonly", )
GetJava['values'] = ("请选择Java")
GetJava.current(0)
Settings = ttk.Button(MainWind, text="设置", takefocus=False,)
Downloads = ttk.Button(MainWind, text="下载", takefocus=False)
Content = ttk.LabelFrame(MainWind,text="提示",)
GetGameAllFile = ttk.Checkbutton(MainWind,text="检查游戏完整性",variable=GetGameAllFileVar,)
DownAllGameFile = ttk.Checkbutton(MainWind,text="尝试替换本地库文件",variable=DownAllGameFileVar)
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

thread = threading.Thread(CreatFile())
thread.start()

# Window
MainWind.overrideredirect (True) 
MainWind.geometry("653x410+374+182")
MainWind.resizable(False,False)
MainWind.mainloop()
