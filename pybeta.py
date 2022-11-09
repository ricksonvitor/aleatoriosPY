from tkinter import *
import random

global vitorias
global derrotas
global running
global lab7


choice = 0
comp = 0
vitorias = 0
derrotas = 0

j = Tk()
j.title("JoKenPython 0.2a")

b = Entry(j)
b.pack()
lab7 = Label(j, text="Faça sua jogada")
def maincore():
    global vitorias
    global derrotas
    global lab7
    choice = str(b.get()).lower()
    comp = random.randint(1,3)
    if choice == 'pedra':
        if comp == 1:
            lab7["text"] = "Pedra vs Pedra -- Empate"
        elif comp == 2:
            lab7["text"] = "Pedra vs Papel -- Derrota"
            derrotas = derrotas + 1
        elif comp == 3:
            lab7["text"] = "Pedra vs Tesoura -- Vitória"
            vitorias = vitorias + 1
    elif choice == 'papel':
        if comp == 1:
            lab7["text"] = "Papel vs Pedra -- Vitória"
            vitorias = vitorias + 1
        elif comp == 2:
            lab7["text"] = "Papel vs Papel -- Empate"
        elif comp == 3:
            lab7["text"] = "Papel vs Tesoura -- Derrota"
            derrotas = derrotas + 1
    elif choice == 'tesoura':
        if comp == 1:
            lab7["text"] = "Tesoura vs Pedra -- Derrota"
            derrotas = derrotas + 1
        elif comp == 2:
            lab7["text"] = "Tesoura vs Papel -- Vitória"
            vitorias = vitorias + 1
        elif comp == 3:
            lab7["text"] = "Tesoura vs Tesoura -- Empate"


a = Button(j, text="Realizar Jogada!", command=maincore)
a.pack()



def f():
    global A
    global lb2
    lab10 = Label(j, text=" ")
    lab10.pack()
    lab1 = Label(j, text="JoKenPython!")
    lab1.pack()
    lab2 = Label(j, text="=====================")
    lab2.pack()
    lab3 = Label(j, text="|      Opções de jogadas abaixo       |")
    lab3.pack()
    lab4 = Label(j, text="|                       Pedra                         |")
    lab4.pack()
    lab5 = Label(j, text="|                       Papel                          |")
    lab5.pack()
    lab6 = Label(j, text="|                     Tesoura                       |")
    lab6.pack()
    lab8 = Label(j, text="=====================")
    lab8.pack()

f()
lab7.pack()

j.geometry("400x400")
j.mainloop()
