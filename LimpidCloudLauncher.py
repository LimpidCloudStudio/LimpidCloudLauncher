import json
import os
import threading
import requests
import wget

import tkinter as tk
import tkinter.ttk as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Style

MainWind = Style(theme='cyborg').master

FabricAPIVar = tk.StringVar()
SodiumVar = tk.StringVar()
OptifineVar = tk.StringVar()
ModpacksVar = tk.StringVar()

DownLabel = ttk.Label(MainWind,text="下载游戏",anchor="center", )
QuitButton = ttk.Button(MainWind, text="X", takefocus=False,command=quit,bootstyle=DANGER)
DownFrame = ttk.LabelFrame(MainWind,text="下载",)
VersionsNameLabel = ttk.Label(DownFrame,text="版本名称:",anchor="center", )
VersionsName = ttk.Entry(DownFrame, )
VersionsGameLabel = ttk.Label(DownFrame,text="版本号：",anchor="center", )
VersionsGame = ttk.Entry(DownFrame, )
ModsLoaderLabel = ttk.Label(DownFrame,text="模组加载器:",anchor="center", )
ModsLoaderList = ttk.Combobox(DownFrame, state="readonly", )
ModsLoaderList['values'] = ("原版","Forge","NeoForge","Fabric","Quilt","LiteLoader")
ModsLoaderList.current(0)
ParticipationFrame = ttk.Frame(DownFrame,)
FabricAPI = ttk.Checkbutton(ParticipationFrame,text="Fabric API(使用Quilt或者Fabric模组加载器的情况下使用)",variable=FabricAPIVar,onvalue=True,offvalue=False,)
Sodium = ttk.Checkbutton(ParticipationFrame,text="钠(使用Quilt或者Fabric模组加载器的情况下使用,与高清修复不兼容)",variable=SodiumVar,onvalue=True,offvalue=False,)
Optifine = ttk.Checkbutton(ParticipationFrame,text="高清修复 (使用Forge或者NeoForge加载器的情况下使用，与钠不兼容)",variable=OptifineVar,onvalue=True,offvalue=False,)
AdvancedOptions = ttk.LabelFrame(DownFrame,text="高级选项(非专业人士，请不要随意更改)",)
ModPacksFrame = ttk.Frame(DownFrame,)
ModPacks = ttk.Checkbutton(ModPacksFrame,text="允许导出为整合包",variable=ModpacksVar,onvalue=True,offvalue=False,)
JavaPathLabel = ttk.Label(AdvancedOptions,text="Java路径:",anchor="center", )
JavaPath = ttk.Entry(AdvancedOptions, )
RendererLabel = ttk.Label(AdvancedOptions,text="渲染引擎:",anchor="center", )
Renderer = ttk.Combobox(AdvancedOptions, state="readonly", )
Renderer['values'] = ("OpenGL","Vulkan","DirectX12","软渲染器")
Renderer.current(0)
GetAllName = ttk.Label(AdvancedOptions,text="已使用名称:",anchor="center", )
RamSet = ttk.Scale(AdvancedOptions, orient=HORIZONTAL, )
RamSetLabel = ttk.Label(AdvancedOptions,text="内存设置",anchor="center", )
DownloadGame = ttk.Button(MainWind, text="下载并安装", takefocus=False,)
DownloadGameFile = ttk.Button(MainWind, text="下载游戏本体", takefocus=False,)


DownLabel.place(x=0, y=0, width=61, height=28)
QuitButton.place(x=620, y=0, width=31, height=31)
DownFrame.place(x=0, y=30, width=526, height=379)
VersionsNameLabel.place(x=0, y=0, width=54, height=28)
VersionsName.place(x=60, y=0, width=150, height=28)
VersionsGameLabel.place(x=0, y=30, width=54, height=28)
VersionsGame.place(x=60, y=30, width=150, height=28)
ModsLoaderLabel.place(x=220, y=0, width=67, height=28)
ModsLoaderList.place(x=290, y=0, width=150, height=28)
ParticipationFrame.place(x=0, y=270, width=521, height=84)
FabricAPI.place(x=3, y=3, width=329, height=22)
Sodium.place(x=3, y=59, width=382, height=22)
Optifine.place(x=3, y=30, width=399, height=24)
AdvancedOptions.place(x=0, y=60, width=519, height=198)
ModPacksFrame.place(x=220, y=30, width=216, height=22)
ModPacks.place(x=2, y=0, width=119, height=22)
JavaPathLabel.place(x=3, y=0, width=60, height=28)
JavaPath.place(x=70, y=0, width=150, height=28)
Renderer.place(x=290, y=0, width=150, height=28)
RendererLabel.place(x=230, y=0, width=56, height=22)
GetAllName.place(x=5, y=70, width=71, height=17)
RamSet.place(x=70, y=30, width=151, height=22)
RamSetLabel.place(x=4, y=30, width=59, height=22)
DownloadGame.place(x=540, y=370, width=103, height=30)
DownloadGameFile.place(x=540, y=330, width=103, height=30)

# Window
MainWind.overrideredirect (True) 
MainWind.geometry("653x410+374+182")
MainWind.resizable(False,False)
MainWind.mainloop()
