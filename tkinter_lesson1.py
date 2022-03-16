import _tkinter 
import tkinter
from turtle import width 

from debugpy import listen

#window

window = tkinter.Tk()

window.title("My First GUI")
window.minsize(width=500,height=300)

#Label

my_label = tkinter.Label(text = "I am a Label", font = ("Arial", 24, "italic"))
my_label.place(x=200,y=0)

#Button

def button_clicked():
    print("I got clicked")
    new_twxt = input.get()
    my_label.config(text=new_twxt)

button = tkinter.Button(text="Click me", command=button_clicked)

input = tkinter.Entry(width=10)

button.grid(column=0,row=0)
print(input.get())


#Entry
#Text
#Spinbox
#Scale
#CheckBox
#Radiobutton
#Listbox

#https://replit.com/@appbrewery/tkinter-widget-demo










window.mainloop()