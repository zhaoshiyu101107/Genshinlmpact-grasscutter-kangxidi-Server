import os
import time
import psutil
import webbrowser
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#版本：5.3.0 beta
#作者：昭诗雨
# 创建主窗口
root = tk.Tk()
root.title("康熙启动器(服务端)-5.3.0")
root.geometry("1200x600")  # 设置窗口大小
root.configure(bg="gray")
#root.iconbitmap(r'Example/favicon.ico')  # 设置主窗口图标
root.iconphoto(True, tk.PhotoImage(file='data/Example/favicon.ico'))
# 加载背景图片
background_image = Image.open(r"data/Example/a.jpg")  # 替换为你的图片路径
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.geometry(f"{background_image.width}x{background_image.height}")


# 帮助菜单内容
#设置
#帮助
def show_help():
    help_window = tk.Toplevel(root)
    help_window.title("帮助")
    help_window.geometry("350x500")  # 设置弹窗大小
    root.iconphoto(True, tk.PhotoImage(file='data/Example/favicon.ico'))
    help_text = """
    欢迎使用康熙服务端启动器！
    -在“设置”菜单中选择你需要的版本
    -直接点击主页“一键启动按键”

    如果您有任何问题，请联系我们的客服团队。
    """
    label = tk.Label(help_window, text=help_text, justify="left", padx=10, pady=10)
    label.pack(fill="both", expand=True)

#官网
# 官网
def open_guanwang():
    webbrowser.open("https://zhan.kangxidi.shop/")
#康熙盘
def open_pan():
    webbrowser.open("https://pan.kangxidi.shop/")
#github
def open_github():
    webbrowser.open("https://github.com/woailulu/GenshinImpact-PrivateService-zuizhong")
#百度
def open_baidu():
    webbrowser.open("https://www.baidu.com")

#启动服务器
def open_fuwu():
    os.startfile(r"data\data.exe")
    time.sleep(6)
    messagebox.showinfo("提示", "原神私服开启成功", icon="info")
def close_fuwu():
    os.startfile(r"data\MongoDB\close.exe")
    os.startfile(r"data\grasscutter\close.exe")
    messagebox.showinfo("提示", "原神私服成功关闭", icon="info")



# 创建菜单栏
menubar = tk.Menu(root)
# 添加“设置”菜单
settings_menu = tk.Menu(menubar, tearoff=0)
settings_menu.add_command(label="查看帮助", command=show_help)
settings_menu.add_separator()  # 添加分隔线
settings_menu.add_command(label="退出", command=root.quit)
# 添加“官网”菜单
guanwang_menu = tk.Menu(menubar, tearoff=0)
guanwang_menu.add_command(label="官网", command=open_guanwang)
guanwang_menu.add_command(label="康熙盘", command=open_pan)
guanwang_menu.add_command(label="github", command=open_github)
guanwang_menu.add_command(label="百度", command=open_baidu)
# 将菜单添加到菜单栏
menubar.add_cascade(label="设置", menu=settings_menu)
menubar.add_cascade(label="官网", menu=guanwang_menu)

# 创建按钮
#私服
yuansifu = tk.Button(root, text="服务器启动", command=open_fuwu, bg="gray", fg="white", width=10, height=2)
yuansifu.place(relx=0.5, rely=0.7, anchor="center")
yuansifu = tk.Button(root, text="服务器关闭", command=close_fuwu, bg="gray", fg="white", width=10, height=2)
yuansifu.place(relx=0.5, rely=0.9, anchor="center")


# 配置主窗口使用菜单栏
root.config(menu=menubar)
# 运行主循环
root.mainloop()