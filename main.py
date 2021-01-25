# first clock
# hello
from tkinter import *
import time
from playsound import playsound
import datetime

root = Tk() # creating root of window
root.title("Count Down") # for title
root.geometry('500x300') # size of window
root.config(bg = "violet")
root.resizable(0,0) # or root.resizable(false,false)
Label(root,text = "Countdown and Timer",font = ("bold",30),fg = "yellow", bg = "red").pack()

# current_time
'''
strftime() method return the string representing the time in given format
after() method used to give a delay of 1000 millisecond which is 1 sec
'''
Label(root, font =("bold", 20), text = 'current time :', fg = "black", bg = 'orange').place(x = 20 ,y = 70)
def clock():
    clock_time = time.strftime('%H:%M:%S %p')
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)
curr_time =Label(root, font =("bold", 20), text = '', fg = 'gray25' ,bg ='papaya whip')
curr_time.place(x = 190 , y = 70)
clock()

# set timer
'''
sec is a string type variable that stores the seconds.
mins is a string type variable that stores the minutes.
hrs is a string type variable that stores the hours

Entry() widget is used to create an input text field.\
textvariable used to retrieve text from specific variable to entry widget
place() widgets place widgets in a specific position in the parent widget.
'''
sec = StringVar()
Entry(root, textvariable = sec, width = 2, font = 'arial 12').place(x=250, y=155)
sec.set('00')
mins= StringVar()
Entry(root, textvariable = mins, width =2, font = 'arial 12').place(x=225, y=155)
mins.set('00')
hrs= StringVar()
Entry(root, textvariable = hrs, width =2, font = 'arial 12').place(x=200, y=155)
hrs.set('00')

# countdown
def countdown():
    times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    while times > -1:
        minute, second = (times // 60, times % 60)

        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)

        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)
        # bif times > 0:
            # playsound("Savior - Bassjackers.mp3")
        if times == 0:
            playsound("Savior - Bassjackers.mp3")
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        times -= 1


# create start button
'''
Button() widget used to display a button on window

bd sets the size of the border
command calls the function when we click on button
'''

Label(root, font='arial 15 bold', text='set the time', bg='papaya whip').place(x=40, y=150)
Button(root, text='START', bd='5', command=countdown, bg='antique white', font='arial 10 bold').place(x=150, y=210)
root.mainloop() # for displaying