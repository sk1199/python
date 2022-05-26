import time
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox,filedialog
from playsound import playsound
import pygame
from pygame import mixer
import sv_ttk

mixer.init()


root = Tk()

#creating display window
root.geometry("300x300")
root.resizable(0,0)
sv_ttk.set_theme('light')

#configure the background
root.title("Made by - Shantanu Kute")
#Label(root, text = "made by me ", font = "arial 10 italic" , bg = "yellow").pack()

#declaring variable
hour=StringVar()
minute=StringVar()
second=StringVar()

#setting the default value as 0

hour.set("00")
minute.set("00")
second.set("00")

# Use of Entry class to take input from the user
hourEntry= Entry(root, width=3, font=("Arial",18,""),
                 textvariable=hour)
hourEntry.place(x=80,y=120)
  
minuteEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=130,y=120)
  
secondEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.place(x=180,y=120)

def playsongs():
    song = filedialog.askopenfilename(initialdir = 'desktop',
                                          title ="select an audio file ",
                                          filetypes = (("Audio files", "*.mp3*"), ("All files", "*.*")))
   
    
    mixer.music.load(song)


    
#button to select sound
btn2 = Button(root,text = 'Select sound',command = playsongs)
btn2.place(x = 190 ,y = 190)

  
  
def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        root.update()
        time.sleep(1)
  
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            mixer.music.play()
            messagebox.showinfo("Time Countdown", "Time's up ")            
         
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1

        
btn0 = Label(root,text='Set timer')
btn0.place(x = 110,y = 70)
 
# button widget
btn = Button(root, text='Start',command= submit)
btn.place(x = 30,y = 190)



#current time
btn3 = Label(root,text='Current time')
btn3.place(x = 10,y = 20)

def clock():
    clock_time = time. strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)
curr_time =Label(root, font ='arial 15 bold',text ="")
curr_time.place(x = 100 , y = 20)
clock()



#create stopwatch
root=Tk()
root.title('stopwatch')
root.geometry('300x200')
root.resizable(0,0)


sc=0;mn=0;hr=0;stp=0

def start():
    global sc,mn,hr
    sc=sc+1
    if(sc==60):
        mn=mn+1
        sc=0
    if(mn==60):
        hr=hr+1
        mn=0
    if(stp==0):
        label=Label(root,text='%i:%i:%i'%(hr,mn,sc),font=('arial',30,'bold'))
        label.after(300,start)
        label.place(x=100,y=60)
def stop():
    global stp
    stp=1

def cancel():
    quit()




#start button

button1=Button(root,text="Start",command=start).place(x=00,y=10)
button2=Button(root,text="Stop",command=stop).place(x=100,y=10)
button3=Button(root,text="Cancel",command=cancel).place(x=200,y=10)




#to run the loop infinitly
root.mainloop()
