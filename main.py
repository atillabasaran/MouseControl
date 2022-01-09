import time
from tkinter import *
from tkinter import messagebox

import pyautogui


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.root = parent
        self.initUI()
        self.arr = []

    def initUI(self):
        #Bu kisimda genel olarak arayuz yapilmaktadir.
        self.grid()

        self.text = Entry(self)
        self.text.grid(columnspan=3)

        self.button1 = Button(self, text="saniye",command=self.delayAdd).grid(row=1,column=0,padx=3)
        self.button2 = Button(self, text="tıklama",command=self.clickAdd).grid(row=1,column=1)
        self.button3 = Button(self, text="yapistir",command=self.pasteAdd).grid(row=1,column=2)
        self.label = Label(self,text="dongu arasi delay").grid(row=2,column=0,columnspan=2)
        self.loopDelay = Entry(self,width=5)
        self.loopDelay.grid(row=2,column=2)
        self.label = Label(self, text="kac defa calissin").grid(row=3,column=0,columnspan=2)
        self.loop = Entry(self,width=5)
        self.loop.grid(row=3,column=2)
        self.button4 = Button(self,text="baslat",command=self.start).grid(row=4,columnspan=3,pady=5)



    def delayAdd(self):
        try:
            self.arr.append((1, int(self.text.get())))
            self.text.delete(0,END)
        except:
            messagebox.showerror(message="hatali giris yapildi")
        print(self.arr)

    def clickAdd(self):
        try:
            a, b = self.text.get().split(",")
            self.text.delete(0,END)
        except:
            messagebox.showerror(message="hatali giris yapildi")
            return
        self.arr.append((2,(int(a),int(b))))
        print(self.arr)

    def pasteAdd(self):
        try:
            a, b, c = self.text.get().split(",")
            self.text.delete(0,END)
        except:
            messagebox.showerror(message="hatali giris yapildi")
            return
        self.arr.append((3,(int(a),int(b),c)))
        print(self.arr)

    def start(self):
        delay = self.loopDelay.get()
        loop = self.loop.get()
        for _ in range(int(loop)):
            for i,j in self.arr:
                if i==1:
                    self.delay(j)
                elif i==2:
                    self.click(j[0], j[1])
                else:
                    self.paste(j[0], j[1], j[2])
            print(_)
            time.sleep(int(delay))
        exit(0)


    def delay(self,saniye):
        time.sleep(saniye)

    def click(self,x,y):
        pyautogui.click(x,y)

    def paste(self,x,y,metin):
        self.click(x,y)
        for i in metin:
            pyautogui.hotkey(i)
        # pyautogui.hotkey("ctrl","v")
        time.sleep(0.1)
        pyautogui.hotkey("enter")

def main():
    root = Tk()
    root.title("Bot")
    root.resizable(0,0)
    root.geometry("250x150+1000+500")
    App = Example(root)
    root.mainloop()

if __name__ == '__main__':
    main()

