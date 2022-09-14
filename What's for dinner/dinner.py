import tkinter
import time
import threading
import random
from tkinter import messagebox as tkMessageBox
import sys
 
class veryJiJang:
    def __init__(self):
        # setup
        self.root = tkinter.Tk()
        self.root.title("晚餐吃什麼啊啊啊")
        self.root.minsize(320, 360)
        self.root.maxsize(320, 360)
        # checking variables
        self.isLoop = False
        self.newLoop = False
        self.value = []
        self.setwindow()
        self.root.mainloop()
    
    def kill(self):
        """
        kill program
        """
        self.root.destroy
        sys.exit()
 
    # layout
    def setwindow(self):
        # start/stop button
        self.btn_Start = tkinter.Button(self.root, text="start/stop", command=self.newTask)
        self.btn_Start.place(x=125, y=125, width=70, height=70)
        # exit button
        self.btn_Exit = tkinter.Button(self.root, text = "Exit", command=self.kill)
        self.btn_Exit.place(x=100, y=280, width=100, height=70)

    
        self.btn1 = tkinter.Button(self.root, text="鍋燒意麵", bg="red")
        self.btn1.place(x=20, y=20, width=70, height=50)
    
        self.btn2 = tkinter.Button(self.root, text="生魚飯", bg="white")
        self.btn2.place(x=90, y=20, width=70, height=50)
    
        self.btn3 = tkinter.Button(self.root, text="丼飯", bg="white")
        self.btn3.place(x=160, y=20, width=70, height=50)
    
        self.btn4 = tkinter.Button(self.root, text="師大第一腿", bg="white")
        self.btn4.place(x=230, y=20, width=70, height=50)
    
        self.btn5 = tkinter.Button(self.root, text="飯糰", bg="white")
        self.btn5.place(x=230, y=90, width=70, height=50)
    
        self.btn6 = tkinter.Button(self.root, text="小手收", bg="white")
        self.btn6.place(x=230, y=160, width=70, height=50)
    
        self.btn7 = tkinter.Button(self.root, text="八方雲集", bg="white")
        self.btn7.place(x=230, y=230, width=70, height=50)
    
        self.btn8 = tkinter.Button(self.root, text="溫州大餛飩", bg="white")
        self.btn8.place(x=160, y=230, width=70, height=50)
    
        self.btn9 = tkinter.Button(self.root, text="師園", bg="white")
        self.btn9.place(x=90, y=230, width=70, height=50)
    
        self.btn10 = tkinter.Button(self.root, text="火鍋", bg="white")
        self.btn10.place(x=20, y=230, width=70, height=50)
    
        self.btn11 = tkinter.Button(self.root, text="冰淇淋", bg="white")
        self.btn11.place(x=20, y=160, width=70, height=50)
    
        self.btn12 = tkinter.Button(self.root, text="小木屋鬆餅", bg="white")
        self.btn12.place(x=20, y=90, width=70, height=50)
            

    # create list
        self.array = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7, self.btn8,
                        self.btn9, self.btn10, self.btn11, self.btn12]
 
 
    def rounds(self):
        if self.isLoop == True:
            return
        # initial starting index
        i = random.randint(1,len(self.array)-1)
        sleeping = 0.001

        while True:
            # wheel delay
            flag = False
            if self.isLoop == True:
                time.sleep(0.001)
            elif self.isLoop == False:
                time.sleep(sleeping)
                sleeping += sleeping/10 + 0.0001
                if sleeping >= 0.3:
                    flag = True

            if flag == True:
                flag = False
                self.newLoop = False
                self.value = self.array[i - 1]["text"]
                tkMessageBox.showinfo("","今天吃"+str(self.value))
                sleeping = 0.01
                return

            # color settings
            for x in self.array:
                x["bg"] = "white"
            self.array[i]["bg"] = "red"
            
            i += 1
            if i >= len(self.array):
                i = 0


    def newTask(self):
        if self.isLoop == False:
            # threading
            t = threading.Thread(target=self.rounds)
            t.start()
            self.isLoop = True
                
        elif self.isLoop == True:
            self.isLoop = False
            self.newLoop = True
# Roulette activate
c = veryJiJang()

