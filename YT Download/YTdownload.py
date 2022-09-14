import os
import pytube
import tkinter as tk
from tkinter import ttk

def check_percentage(chunk,size,remote):
	percent = 100.0 * chunk * size / remote
	if percent > 100.0:
		percent = 100.0
	print("Download...{:.2f}%".format(percent))

def Vid():

    m.destroy()
    m1.destroy()
    m2.destroy()


    def vidDownload(url,path):
        a3.config(text = '')
        yt = pytube.YouTube(url)
        yt.streams.first().download(path,filename = 'VidDownload.mp4')
        a3.config(text = 'Download Finish~')

    def get_data():
        global data
        data = [enUrl.get(),enPath.get()]
        vidDownload(data[0],data[1])

    def showpath():
        enPath.delete(0,tk.END)
        enPath.insert(0,comB.get())
    
    m.destroy()
    m1.destroy()
    m2.destroy()

    a1 = tk.Label(text = 'Enter Video Url Down Here',font = 'zapfino 14',bg = 'linen')
    a1.place(anchor = tk.CENTER,x = 250,y = 40)

    enUrl = tk.Entry(width = 40)
    enUrl.place(x = 65,y = 50)

    a2 = tk.Label(text = 'Enter The Path You Wanna Put The Video',bg = 'linen',font = 'zapfino 14')
    a2.place(anchor = tk.CENTER,x = 250,y = 120 )

    enPath = tk.Entry(width = 40)
    enPath.place(x = 65,y = 130)

    btn1 = tk.Button(text = 'Download ~ ',command = get_data)
    btn1.place(anchor = tk.CENTER,x = 140,y = 180)

    comB = ttk.Combobox(values = ['Select a Path','/Users/user/Desktop','/Users/user/Documents','/Users/user/Desktop/coding'])
    comB.place(anchor = tk.CENTER,x = 350,y = 180)
    comB.current(0)
    comB.bind('<<ComboboxSelected>>',showpath())
    
    btn2 = tk.Button(text = 'OK',command = showpath)
    btn2.place(anchor = tk.CENTER,x = 330,y = 200)

    a3 = tk.Label(text = '',bg = 'linen',font = 'zapfino 14')
    a3.place(anchor = tk.CENTER,x = 250,y = 220)

def Aud():
    m.destroy()
    m1.destroy()
    m2.destroy()

    def audDownload(url,path):
        a3.config(text = '')
        yt = pytube.YouTube(url)
        yt.streams.filter(only_audio = True,mime_type = 'audio/mp4').first().download(path,filename = 'AudDownload')
        os.rename('AudDownload.mp4',"AudDownload.mp3")
        a3.config(text = 'Download Finsish~')

    def get_data():
        global data
        data = [enUrl.get(),enPath.get()]
        audDownload(data[0],data[1])

    def showpath():
        enPath.delete(0,tk.END)
        enPath.insert(0,comB.get())
    
    m.destroy()
    m1.destroy()
    m2.destroy()

    a1 = tk.Label(text = 'Enter Audio Url Down Here',font = 'zapfino 14',bg = 'linen')
    a1.place(anchor = tk.CENTER,x = 250,y = 40)

    enUrl = tk.Entry(width = 40)
    enUrl.place(x = 65,y = 50)

    a2 = tk.Label(text = 'Enter The Path You Wanna Put The Audio',bg = 'linen',font = 'zapfino 14')
    a2.place(anchor = tk.CENTER,x = 250,y = 120 )

    enPath = tk.Entry(width = 40)
    enPath.place(x = 65,y = 130)

    btn1 = tk.Button(text = 'Download ~ ',command = get_data)
    btn1.place(anchor = tk.CENTER,x = 140,y = 180)

    comB = ttk.Combobox(values = ['Select a Path','/Users/user/Desktop','/Users/user/Documents','/Users/user/Desktop/coding'])
    comB.place(anchor = tk.CENTER,x = 350,y = 180)
    comB.current(0)
    comB.bind('<<ComboboxSelected>>',showpath())
    
    btn2 = tk.Button(text = 'OK',command = showpath)
    btn2.place(anchor = tk.CENTER,x = 330,y = 200)

    a3 = tk.Label(text = '',bg = 'linen',font = 'zapfino 14')
    a3.place(anchor = tk.CENTER,x = 250,y = 220)

if __name__ == "__main__":
    win = tk.Tk()
    win.title('YT Dowloader - by Patty')
    win.geometry('500x300+500+600')
    win.resizable(False,False)
    win.config(bg = 'linen')

m = tk.Label(text = 'Video or Audio ?',bg = 'linen',font = 'zapfino 14')
m.place(anchor = tk.CENTER,x = 250,y = 80)

m1 = tk.Button(text = 'Video',command = Vid,width = 15)
m1.place(anchor = tk.CENTER,x = 150,y = 150)

m2 = tk.Button(text = 'Audio',command = Aud,width = 15)
m2.place(anchor = tk.CENTER,x = 350,y = 150)

win.mainloop()