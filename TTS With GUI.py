from gtts import gTTS
from tkinter import *
from tkinter import messagebox,filedialog
from tkinter.ttk import * # ttk for look and feel

import os

def textToSpeech(file, lang):
    print(file, lang)
    try:
        #https://github.com/gokul1630/Text_to_Speech/blob/master/TTS.py
        a =lang
        f = open(file, encoding="utf8")
        m = f.read()
        c=gTTS(lang=a, text=m, slow=False)
        c.save("Output.mp3")

        
        playOption = messagebox.askyesno("Task Completed","The Given file has been converted into speech.\n Do you want to open ?")
       
        if playOption == True:
            os.startfile('Output.mp3')
            
    except:
        messagebox.showerror("Error","An Error occured..!\nTry Checking the filename or network connection.")
        


def About():
    messagebox.showinfo("About","Text to Speech, Version 1.0\n\nMain Source Developed by Gokul Prasanth(https://github.com/gokul1630)\n\nGUI Developed by Siva Rajendran(https://github.com/siva222r")

def helpIndex():
    messagebox.showinfo("Help Index","1. Open the file \n2. Choose the language \n3. Click on Generate Speech \n4. Play the .mp3 file")

def openFile():
    filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Text files","*.txt"),("All files","*.*")))
    fileName.set(filename)
def playOutput():
    os.startfile('Output.mp3')
    


# Main GUI Part
window = Tk()
window.title("Text to Speech")
window.geometry("400x200+450+200")
window.resizable(width=False, height=False)

#Add Menubar with file and help options.
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=window.destroy)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=helpIndex)
helpmenu.add_command(label="About...", command=About)
menubar.add_cascade(label="Help", menu=helpmenu)
window.config(menu=menubar)

#Labels for displaying the file name & other contents
openedFile = Label(window, text="Opened File", width=25).place(x=50, y=25)

# String Variable for displaying the file Name
fileName = StringVar()
fileName.set("kural.txt")

openedFileName = Entry(window, textvariable=fileName, width=30)
openedFileName.place(x=150, y=25)
Button(window, text="Open", width=5, command=openFile).place(x=340, y=25)

language = StringVar()
language.set("Ta")

Label(window, text="Select Language", width=25).place(x=30, y=60)

rb1 = Radiobutton(window, text = "Tamil", variable=language,value = "Ta")
rb1.place(x=150, y=60)
rb2 = Radiobutton(window, text = "English", variable=language,value = "En")
rb2.place(x=250, y=60)

generateSpeech =Button(window, text="Generate Speech", width=20,command=lambda:textToSpeech(openedFileName.get(), str(language.get()))).place(x=50, y=100)
playOutput = Button(window, text="Play Output", width=20,command=playOutput).place(x=200, y=100)


#About Text to Speech & Developer Info
versionInfo = Label(window, text="© Text to Speech, Version 1.0\nDeveloped by Gokul Prasanth & Siva Rajendran, 2020", width=100).place(x=5, y=160)

#Mainloop for Window
window.mainloop()
