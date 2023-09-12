from turtle import*
from tkinter import*
#Короче план просто.. рисовать или мини игра.
#game
def click():
    got_it = txt.get()
    if got_it == 'start':
        print('Добро пожаловать сюда, вобщем будет весело. Напишите "manu" и попейте водки чтобы ознакомится с меню.')
    if got_it == 'manu':
        print('Как-то так, совсем новёхенькая игра и не доработанная. В общем, собирай код и пиши в строку по пути попивая водочку. Первое задание "1"')
    if got_it == '1':
        rt(-45)
        fd(100)
        lt(135)
        fd(50)
        print('What a number?')
    if got_it == "7":
        print('Well done! First code number "6"')
def clicke():
    got_it = txt.get()
    if got_it == 'a':
        print('lol')
def clicka():
    got_it = txt.get()
    if got_it == 'a':
        print('hey')
def clicks():
    got_it = txt.get()
    if got_it == 'a':
        print('rar')
print("Напишите 'start' чтобы начать")
window = Tk()
window.title("window")
window.geometry('400x75')
txt = Entry(window,width=40)
txt.grid(column=2, row=0)
btn = Button(window, text="Vodka drink!", command=click)
btn.grid(column=3, row=0)
btn = Button(window, text="Vodka drunk!", command=clicke)
btn.grid(column=4, row=1)
btn = Button(window, text="Vodka!", command=clicka)
btn.grid(column=3, row=1)
btn = Button(window, text="Vodka end!", command=clicks)
btn.grid(column=4, row=0)
window.mainloop()
