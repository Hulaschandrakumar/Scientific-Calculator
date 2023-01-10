# Import Tkinter Module
import tkinter as tk
from tkinter import *
# Import Sympy to evaluate advanced equations
from sympy import symbols, solve
# Import OS to trigger action beofre exiting the app.
import os
# Import webbrowser to open websites to rate the calculator
import webbrowser

# Create Window
window = tk.Tk()
# Title of the window
window.title('Scientific calculator')
# Dimension of Window
window.geometry('405x610')
# Stop resizing the window
window.resizable(False,False)

# First calculator label
label1=tk.Label(window,text="CALCULATOR",relief=RIDGE,borderwidth=9,width=39,fg="blue",bg="#FF69B4")
label1.config(font=('Arial bold', 13))
label1.place(x=0,y=0)
# Last line Label
label1=tk.Label(window,text="~ Designed by Hulas Chandra kumar ",relief=RIDGE,borderwidth=5,width=49,fg="blue",bg="#FFD700")
label1.config(font=('Arial bold', 10))
label1.place(x=0,y=582)

# First Entry Box
text1 = tk.Entry(master=window, width=27,relief=SUNKEN,borderwidth=16,bg="#FF7F50")
text1.config(font=('Arial bold', 19))
text1.place(x=0, y=70)
# Second Entry Box
text2 = tk.Entry(master=window, width=27,relief=RIDGE,borderwidth=16,bg="#C0C0C0")
text2.config(font=('Arial bold', 19))
text2.place(x=0, y=135)

# Frame to design Keys
frame = Frame(master=window,width=400,height=400,bg="grey")
frame.place(x=0,y=200)

# Frame to design above five Options
frame1 = Frame(master=window,width=405,height=30)
frame1.place(x=0,y=40)

# Function to remove the content of histort.txt file
def remhist():
    # Location of history.txt file
    # Change it according to your file location
    f = open('C:/Users/Public/Documents/history.txt', 'w')
    f.write("")
    f.close()
# Calling remhist() when we manually closes the window using exit button of window
# and OS module used here
window.protocol(remhist())
# Function to open feedback website
def rating():
    # Default browser path
    # Change it according to your own
    #path2 = '"C://Program Files/Mozilla Firefox/firefox.exe" %s'
    #webbrowser.get(path2).open('vashishthahari.weebly.com/feedback')
    webbrowser.open('vashishthahari.weebly.com/feedback') 
    close()
# Function to open personal website
def website():
    #path1 = '"C://Program Files/Mozilla Firefox/firefox.exe" %s'
    #webbrowser.get(path1).open('https://github.com/Hulaschandrakumar/Job-Application')
    webbrowser.open('https://github.com/Hulaschandrakumar/Job-Application') 
# Function to reset text boxes and history.txt
def reset():
    remhist()
    text1.delete(0, tk.END)
    text2.delete(0, tk.END)
# Function to evaluate result
def result():
    #just give a symbol x to equation, to solve the value for x
    # Defining 'x' as a symbol in expression
    x = symbols('x')
    # getting expression from text box 2
    problem=text2.get()
    # exporting to history.txt
    w = "Que.:- "+str(problem)+"\n"
    res2=problem+"+ x"
    c=solve(res2)
    # Final result
    result1=str(c[0]*-1)
    z =  "Ans.:- "+str(result1)+"\n\n"

    #Creating a .txt file to store History
    f = open('C:/Users/Public/Documents/history.txt', 'a+')
    # Exporting problem and result to .txt file
    f.write(w)
    f.write(z)
    f.close()
    # deleting the content of both boxes
    text1.delete(0, tk.END)
    text2.delete(0, tk.END)
    # Now showing only result value in textbox 1
    text1.insert(0,result1)

# Function to quit the calculator,after deleting all the history.
def close():
    f = open('C:/Users/Public/Documents/history.txt', 'w')
    f.write("")
    f.close()
    exit()
# Function to show history.txt file in notepad
def history():
    f = open('C:/Users/Public/Documents/history.txt', 'a+')
    f.close()
    os.system("C:/Users/Public/Documents/history.txt")
# Function to clear only 1 last character from expression(textbox 2)
def clr1():
    len1=len(text2.get())
    text2.delete(len1-1)
# Function to clear all (AC) Everything
def delall():
    text2.delete(0, tk.END)
    text1.delete(0, tk.END)

# Function to insert respective values to thee expression(textbox 2)

def bt3():
    a = str("%")
    text2.insert(tk.END, a)
def bt4():
    a=str("/")
    text2.insert(tk.END, a)
def bt5():
    a=str("(")
    text2.insert(tk.END, a)
def bt6():
    a=str(7)
    text2.insert(tk.END,a)
def bt7():
    a=str(8)
    text2.insert(tk.END, a)
def bt8():
    a=str(9)
    text2.insert(tk.END, a)
def bt9():
    a=str("*")
    text2.insert(tk.END,a)
def bt10():
    a=str(")")
    text2.insert(tk.END, a)
def bt11():
    a=str(4)
    text2.insert(tk.END, a)
def bt12():
    a=str(5)
    text2.insert(tk.END,a)
def bt13():
    a=str(6)
    text2.insert(tk.END, a)
def bt14():
    a=str("-")
    text2.insert(tk.END, a)
def bt15():
    a = str("^(1/2)")
    text2.insert(tk.END, a)
def bt16():
    a=str(1)
    text2.insert(tk.END, a)
def bt17():
    a=str(2)
    text2.insert(tk.END, a)
def bt18():
    a=str(3)
    text2.insert(tk.END,a)
def bt19():
    a=str("+")
    text2.insert(tk.END, a)
def bt20():
    a = str("^")
    text2.insert(tk.END, a)
def bt21():
    a=str(00)
    text2.insert(tk.END,a)
def bt22():
    a=str(0)
    text2.insert(tk.END,a)
def bt23():
    a=str(".")
    text2.insert(tk.END, a)

# All the BUTTONS of CALCULATOR
   # Top 5 buttons
but26 = tk.Button(frame1, text="Website",width=8,height=1,borderwidth=5, relief=tk.RAISED, fg="black", bg="#ADFF2F",command=website)
but26.config(font=('Arial bold',8))
but26.grid(row = 0, column = 0,padx=4)
but27 = tk.Button(frame1, text="Rate Us",width=8,height=1,borderwidth=5, relief=tk.RAISED, fg="black", bg="#00BFFF",command=rating)
but27.config(font=('Arial bold',8))
but27.grid(row = 0, column = 1,padx=5)
but28 = tk.Button(frame1, text="Reset",width=8,height=1,borderwidth=5, relief=tk.RAISED, fg="black", bg="#CD853F",command=reset)
but28.config(font=('Arial bold',8))
but28.grid(row = 0, column = 2,padx=5)
but29 = tk.Button(frame1, text="History(H)",width=8,height=1,borderwidth=5, relief=tk.RAISED, fg="black", bg="lime green",command=history)
but29.config(font=('Arial bold', 8))
but29.grid(row = 0, column = 3,padx=5)
but30 = tk.Button(frame1, text="Close(X)",width=8,height=1,borderwidth=5, relief=tk.RAISED, fg="black", bg="red",command=close)
but30.config(font=('Arial bold', 8))
but30.grid(row = 0, column = 4,padx=5)

    # All the calculator button
#ROW 1
but1 = tk.Button(frame, text="AC",width=3,height=1,borderwidth=12, relief=tk.RAISED, fg="black", bg="#00CED1",command=delall)
but1.config(font=('Arial bold', 20))
but1.grid(row = 0, column = 0)

but2 = tk.Button(frame, text="C",width=3,height=1,borderwidth=12, relief=tk.RAISED, fg="black", bg="#00CED1",command=clr1)
but2.config(font=('Arial bold', 20))
but2.grid(row = 0, column = 1)

but3 = tk.Button(frame, text="%",width=3,height=1,borderwidth=12, relief=tk.RAISED, fg="black", bg="#00CED1")
but3.config(font=('Arial bold', 20))
but3.grid(row = 0, column = 2)

but4 = tk.Button(frame, text="/", width=3,height=1,borderwidth=12,relief=tk.RAISED, fg="black", bg="#7B68EE",command=bt4)
but4.config(font=('Arial bold', 20))
but4.grid(row = 0, column = 3)

but5 = tk.Button(frame, text="(", width=3,height=1,borderwidth=12,relief=tk.RAISED, fg="black", bg="#7FFFD4",command=bt5)
but5.config(font=('Arial bold', 20))
but5.grid(row = 0, column = 4)

#ROW 2
but6 = tk.Button(frame, text="7",width=3,height=1,borderwidth=12, relief=tk.RAISED, fg="black", bg="#1E90FF",command=bt6)
but6.config(font=('Arial bold', 20))
but6.grid(row = 1, column = 0)

but7 = tk.Button(frame, text="8",width=3,height=1,borderwidth=12, relief=tk.RAISED, fg="black", bg="#1E90FF",command=bt7)
but7.config(font=('Arial bold', 20))
but7.grid(row = 1, column = 1)

but8 = tk.Button(frame, text="9",width=3,height=1,borderwidth=12, relief=tk.RAISED, fg="black", bg="#1E90FF",command=bt8)
but8.config(font=('Arial bold', 20))
but8.grid(row = 1, column = 2)

but9 = tk.Button(frame, text="*", width=3,height=1,borderwidth=12,relief=tk.RAISED, fg="black", bg="#7B68EE",command=bt9)
but9.config(font=('Arial bold', 20))
but9.grid(row = 1, column = 3)

but10 = tk.Button(frame, text=")", width=3,height=1,borderwidth=12,relief=tk.RAISED, fg="black", bg="#7FFFD4",command=bt10)
but10.config(font=('Arial bold', 20))
but10.grid(row = 1, column = 4)

#ROW 3
but11 = tk.Button(frame, text="4",width=3,height=1,borderwidth=12, relief=tk.RAISED, fg="black", bg="#1E90FF",command=bt11)
but11.config(font=('Arial bold', 20))
but11.grid(row = 2, column = 0)

but12 = tk.Button(frame, text="5",width=3,height=1,borderwidth=12, relief=tk.RAISED, fg="black", bg="#1E90FF",command=bt12)
but12.config(font=('Arial bold', 20))
but12.grid(row = 2, column = 1)

but13 = tk.Button(frame, text="6",width=3,height=1,borderwidth=12, relief=tk.RAISED, fg="black", bg="#1E90FF",command=bt13)
but13.config(font=('Arial bold', 20))
but13.grid(row = 2, column = 2)

but14 = tk.Button(frame, text="-", width=3,height=1,borderwidth=12,relief=tk.RAISED, fg="black", bg="#7B68EE",command=bt14)
but14.config(font=('Arial bold', 20))
but14.grid(row = 2, column = 3)

but15 = tk.Button(frame, text="√", width=3,height=1,borderwidth=12,relief=tk.RAISED, fg="black", bg="#7FFFD4",command=bt15)
but15.config(font=('Arial bold', 20))
but15.grid(row = 2, column = 4)

#ROW 4
but16 = tk.Button(frame, text="1",width=3,height=1,borderwidth=12, relief=tk.RAISED, fg="black", bg="#1E90FF",command=bt16)
but16.config(font=('Arial bold', 20))
but16.grid(row = 3, column = 0)

but17 = tk.Button(frame, text="2",width=3,height=1,borderwidth=12, relief=tk.RAISED, fg="black", bg="#1E90FF",command=bt17)
but17.config(font=('Arial bold', 20))
but17.grid(row = 3, column = 1)

but18 = tk.Button(frame, text="3",width=3,height=1,borderwidth=12, relief=tk.RAISED, fg="black", bg="#1E90FF",command=bt18)
but18.config(font=('Arial bold', 20))
but18.grid(row = 3, column = 2)

but19 = tk.Button(frame, text="+", width=3,height=1,borderwidth=12,relief=tk.RAISED, fg="black", bg="#7B68EE",command=bt19)
but19.config(font=('Arial bold', 20))
but19.grid(row = 3, column = 3)

but20 = tk.Button(frame, text="^", width=3,height=1,borderwidth=12,relief=tk.RAISED, fg="black", bg="#7FFFD4",command=bt20)
but20.config(font=('Arial bold', 20))
but20.grid(row = 3, column = 4)

#ROW 5
but21 = tk.Button(frame, text="00",width=3,height=1,borderwidth=12, relief=tk.RAISED, fg="black", bg="#1E90FF",command=bt21)
but21.config(font=('Arial bold', 20))
but21.grid(row = 4, column = 0)

but22 = tk.Button(frame, text="0",width=3,height=1,borderwidth=12, relief=tk.RAISED, fg="black", bg="#1E90FF",command=bt22)
but22.config(font=('Arial bold', 20))
but22.grid(row = 4, column = 1)

but23 = tk.Button(frame, text=".",width=3,height=1,borderwidth=12, relief=tk.RAISED, fg="black", bg="#1E90FF",command=bt23)
but23.config(font=('Arial bold', 20))
but23.grid(row = 4, column = 2)

but24 = tk.Button(window, text="=", width=8,height= 0,borderwidth=12,relief=tk.RAISED, fg="black", bg="#4169E1",command=result)
but24.config(font=('Arial bold', 20))
but24.place(x=243,y=503)

# Exiting Loop
window.mainloop()
