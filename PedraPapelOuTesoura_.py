from tkinter import *
import tkinter as tk
from random import randint as r
from time import sleep as s


voce = 0
pc = 0

def pedra1():
    s(0.5)
    
    if r(1, 3) == 1:
        output = Label(Tela, width=18, text='Empatou!!\n Também escolhi Pedra')
        output['bg'] = 'red'

        output.place(x=140, y=80)
    elif r(1, 3) == 2:
        output = Label(Tela, width=18, text='Ganhei!!\n Eu escolhi Papel')
        output['bg'] = 'red'

        output.place(x=140, y=80)
        
        global pc
        
        pc += 1
        pc_ = Label(Tela, text='Você: {}'.format(pc))
        pc_['bg'] = 'red'
        pc_.place(x=150, y=200)
        
    else:
        output = Label(Tela, width=18, text='Perdi!!\n Eu escolhi Tesoura')
        output['bg'] = 'red'

        output.place(x=140, y=80)
        
        global voce

        voce += 1
        voce_ = Label(Tela, text='Você: {}'.format(voce))
        voce_['bg'] = 'red'
        voce_.place(x=15, y=200)




def papel1():
    s(0.5)
    
    if r(1, 3) == 1:
        output = Label(Tela, width=18, text='Perdi!!\n Eu escolhi Pedra')
        output['bg'] = 'red'

        output.place(x=140, y=80)

        global voce

        voce += 1
        voce_ = Label(Tela, text='Você: {}'.format(voce))
        voce_['bg'] = 'red'
        voce_.place(x=15, y=200)
        
    elif r(1, 3) == 2:
        output = Label(Tela, width=18, text='Empatou!!\n Também escolhi Papel')
        output['bg'] = 'red'

        output.place(x=140, y=80)
    else:
        output = Label(Tela, width=18, text='Ganhei!!\n Eu escolhi Tesoura')
        output['bg'] = 'red'

        output.place(x=140, y=80)
                
        global pc
        
        pc += 1
        pc_ = Label(Tela, text='Você: {}'.format(pc))
        pc_['bg'] = 'red'
        pc_.place(x=150, y=200)
        

        

def tesoura1():
    s(0.5)
    
    if r(1, 3) == 1:
        output = Label(Tela, width=18, text='Ganhei!!\n Eu escolhi Pedra')
        output['bg'] = 'red'

        output.place(x=140, y=80)
                
        global pc
        
        pc += 1
        pc_ = Label(Tela, text='Você: {}'.format(pc))
        pc_['bg'] = 'red'
        pc_.place(x=150, y=200)

    elif r(1, 3) == 2:
        output = Label(Tela, width=18, text='Perdi!!\n Eu escolhi Papel')
        output['bg'] = 'red'

        output.place(x=140, y=80)
        
        global voce

        voce += 1
        voce_ = Label(Tela, text='Você: {}'.format(voce))
        voce_['bg'] = 'red'
        voce_.place(x=15, y=200)
        
    else:
        output = Label(Tela, width=18, text='Empatou!!\nTambém escolhi Tesoura')
        output['bg'] = 'red'
        output.place(x=140, y=80)


Tela = Tk()
Tela.title('Pedra, Paper ou Tesoura')
Tela.geometry('300x300+150+200')


imagem = tk.PhotoImage(file='Fundo.png')
w = tk.Label(Tela, image=imagem)
w.imagem = imagem
w.pack()


a = Label(Tela, text='Vamos jogar Pedra, Papel ou Tesoura')
a['bg'] = 'red'
a.place(x=50, y=10)

pedra = Button(Tela, width=15, text='Pedra', command=pedra1)
pedra['bg'] = 'red'
pedra.place(x=20, y=30)

papel = Button(Tela, width=15, text='Papel', command=papel1)
papel['bg'] = 'red'
papel.place(x=20, y=60)


tesoura = Button(Tela, width=15, text='Tesoura', command=tesoura1)
tesoura['bg'] = 'red'
tesoura.place(x=20, y=90)

voce_ = Label(Tela, text='Você: {}'.format(voce))
voce_['bg'] = 'red'
voce_.place(x=15, y=200)

pc_ = Label(Tela, text='Você: {}'.format(pc))
pc_['bg'] = 'red'
pc_.place(x=150, y=200)


output = Label(Tela, width=17, text='')
output['bg'] = 'red'
output.place(x=140, y=30)

decoracao= '''

-=-=-=-=-=-=-=-=-=-=
____________________
____________________
____________________
-=-=-=-=-=-=-=-=-=-=
'''

deco = Label(Tela, width=18, text=decoracao)
deco['bg'] = 'red'
deco.place(x=140, y=30)

Tela.mainloop()

