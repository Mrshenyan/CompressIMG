import tkinter
import os


def CheckHasFileOrNot(path):
    if os.path.exists(path):
        print("文件夹存在")
    else:
        print("文件夹不存在")


def CheckkeyAndPath(key, path):
    keyStr = key.get()
    pathStr = path.get()
    key_regStr = ""
    path_regStr = ""
    if keyStr == "":
        print("密钥为空")
    else:
        print(keyStr)
    if pathStr == "":
        print("路径为空")
    else:
        CheckHasFileOrNot(path)
        print("校验路径下有没有相关文件")


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
    parentPanel.goButton = tkinter.Button(parentPanel.frame3, text="GO!", fg="red", font={"宋体", 40}, width=10,
                                          command=lambda: CheckkeyAndPath(K_entry, P_entry))
    parentPanel.goButton.pack()
    parentPanel.frame3.pack(side="top", anchor="c")

    return parentPanel.titleEntry, parentPanel.titleEntry2


def CreatePanel():
    panel = tkinter.Tk()
    panel.title("Tinify压缩")
    panel.geometry("600x300+200+500")
    K_entry = tkinter.Variable()
    P_entry = tkinter.Variable()
    entry1, entry2 = CreateCompent(panel, K_entry, P_entry)
    panel.mainloop()
    return panel, entry1, entry2


MainPanel, key_entry, path_entry = CreatePanel()
