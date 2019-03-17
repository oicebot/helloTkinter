#!/usr/bin/python3
# -*- coding:utf-8 -*-
# FileName:text.py
# From https://docs.python.org/3/library/tkinter.html#how-to-use-this-section

import tkinter as tk


def say_hi(index=0):
    print("hi there, everyone from the No."+str(index)+" button")
    
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.btnNumber = 0

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.add_more
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def add_more(self):
        btnNumber = self.btnNumber
        self.btnNumber=btnNumber+1
        self.next_button = tk.Button(self)
        self.next_button["text"]="我是第 "+str(btnNumber)+" 个按钮"
        self.next_button["command"] = lambda: say_hi(btnNumber)
        self.next_button.pack(side="top")




root = tk.Tk()
app = Application(master=root)
app.mainloop()
