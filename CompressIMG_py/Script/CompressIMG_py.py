import tkinter
import tkinter.messagebox
import os
import tinify


def CompressIMG(img, path):
    print("压缩开始")
    # source = tinify.from_file(path+"/"+img)
    # source.to_file(path+"/"+img)


def getError(msg):
    tkinter.messagebox.showerror(title="Error", message=msg)


def CheckHasFileOrNot(key, path, panel):
    initTinifyKey(key)
    if os.path.exists(path):
        print("文件夹存在")
        Files = os.listdir(path)
        if Files:
            print("文件夹中有东西")
            i = 0
            for k in Files:
                i += 1
                if k.endswith(".png") | k.endswith(".jpg"):
                    print("压缩图片~")
                    CompressIMG(k, path)
                else:
                    print("没有图片")
            if i == len(Files):
                tkinter.messagebox.showinfo(title="tinify压缩", message="搞定~")
    else:
        getError("指定路径不存在")


def initTinifyKey(key):
    tinify.key = key


def CheckkeyAndPath(key, path, panel):
    if key == "":
        getError("密钥为空")
    else:
        if path == "":
            getError("路径为空")
        else:
            print("the key is :  ", key)
            CheckHasFileOrNot(key, path, panel)


def CreateCompent(parentPanel, K_entry, P_entry):
    parentPanel.frame1 = tkinter.Frame(parentPanel)
    parentPanel.titleLabel = tkinter.Label(parentPanel.frame1, text="Tinify密钥：", font={"宋体", 20}, anchor="c")
    parentPanel.titleLabel.pack(side="left", anchor="w")
    parentPanel.titleEntry = tkinter.Entry(parentPanel.frame1, font={"宋体", 20}, textvariable=K_entry)
    parentPanel.titleEntry.pack(side="left", anchor="w")
    parentPanel.frame1.pack(side="top", anchor="nw")

    parentPanel.frame2 = tkinter.Frame(parentPanel)
    parentPanel.titleLabel2 = tkinter.Label(parentPanel.frame2, text="文件  路径：", font={"宋体", 20}, anchor="c")
    parentPanel.titleLabel2.pack(side="left", anchor="w")
    parentPanel.titleEntry2 = tkinter.Entry(parentPanel.frame2, font={"宋体", 20}, textvariable=P_entry)
    parentPanel.titleEntry2.pack(side="left", anchor="w")
    parentPanel.frame2.pack(side="top", anchor="nw")

    parentPanel.frame3 = tkinter.Frame(parentPanel)
    parentPanel.goButton = tkinter.Button(parentPanel.frame3, text="GO!", fg="red", font={"宋体", 40}, width=10, command=lambda: CheckkeyAndPath(parentPanel.titleEntry.get(), parentPanel.titleEntry2.get(),parentPanel))
    parentPanel.goButton.pack()
    parentPanel.frame3.pack(side="top", anchor="c")
    # protext = tkinter.StringVar
    # parentPanel.frame4 = tkinter.Frame(parentPanel)
    # parentPanel.proLabel = tkinter.Label(parentPanel.frame4, textvariable=protext, fg="red", font={"宋体", 20}, anchor="c")
    # parentPanel.proLabel.pack(side="left", anchor="w")
    # parentPanel.frame4.pack(side="top", anchor="c")

    return parentPanel.titleEntry, parentPanel.titleEntry2


def CreatePanel():
    panel = tkinter.Tk()
    height = 300
    width = 600
    screenWidth = panel.winfo_screenwidth()
    screenHeight = panel.winfo_screenheight()
    print(screenHeight,screenWidth)
    aligner = '%dx%d+%d+%d' % (width, height, (screenWidth - width) / 2, (screenHeight - height) / 2)
    panel.geometry(aligner)
    panel.title("Tinify压缩")
    K_entry = tkinter.Variable()
    P_entry = tkinter.Variable()
    entry1, entry2 = CreateCompent(panel, K_entry, P_entry)
    panel.mainloop()
    return panel, entry1, entry2


MainPanel, key_entry, path_entry = CreatePanel()
