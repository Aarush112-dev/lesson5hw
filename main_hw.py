from tkinter import *
import tkinter.messagebox
import random

window = Tk()
window.title("Guess the product")
window.geometry("300x200")

number = random.randint(1,100)
number2 = random.randint(1,100)
product = number*number2


def check_number():
    guess = enter_guess.get()
    if int(guess) > product:
        tkinter.messagebox.showinfo("high", "Too high")
    elif int(guess) < product:
        tkinter.messagebox.showinfo("low", "Too low")
    else:
        tkinter.messagebox.showinfo("correct", "You got the correct answer!!!")

def con_button():
    name2 = enter_name.get()
    tkinter.messagebox.showinfo("welcome","Welcome {}".format(name2))
    tkinter.messagebox.showinfo("guess","Guess the product of {} and {}".format(number,number2))

def reset():
    global number,number2
    tkinter.messagebox.askquestion("askquestion", "Are you sure you want to reset the game?")
    number = random.randint(1,100)
    number2 = random.randint(1,100)
    tkinter.messagebox.showinfo("guess","Guess the product of {} and {}".format(number,number2))



welcome = Label(window,text="Welcome to our game",font=("aerial",10))
welcome.pack()

name = Label(window,text="What's your name?",font=("aerial",10))
name.place(x=10,y=50)

enter_name = Entry(window,width=20)
enter_name.place(x=10,y=75,height=25)

ok = Button(window,text="OK",bg="light grey",width=5,height=1,command=con_button)
ok.place(x=150,y=74)

guess = Label(window,text="Take a guess:",font=("aerial",10))
guess.place(x=10,y=125)

enter_guess = Entry(window,width=20)
enter_guess.place(x=110,y=125,height=25)

guess2 = Button(window,text="guess",bg="light grey",width=5,height=1,command=check_number)
guess2.place(x=240,y=125)

reset = Button(window,text="reset",bg="green",fg="white",width=5,height=1,command=reset)
reset.place(x=125,y=165)

window.mainloop()