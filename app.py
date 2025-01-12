# importando tkinter 
from tkinter import *
from tkinter import ttk

# cores
cor1 = "#3b3b3b" # Cinza Escuro  
cor2 = "#feffff" # branco
cor3 = "#38576b" # azul escuro 
cor4 = "#f5f5f5" # branco fumaça
cor5 = "#ffac40" # laranja 

# criação da janela

janela =Tk()
janela.title("Calculadora")
janela.geometry("240x309")
janela.config(bg=cor1)

# parte do visor/ frames

frame_tela = Frame(janela, width=240, height=52, bg=cor3)
frame_tela.grid(row=0, column=0)

# parte dos números e das operações/ frames

frame_corpo = Frame(janela, width=240, height=280)
frame_corpo.grid(row=1, column=0)

# variavel todos valores

todos_valores = ''

# criação label

valor_texto = StringVar()

# criando função

def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)
 
    # pasando vales para a tela 
    valor_texto.set(todos_valores)


# função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)


# funçãolimper tela

def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")





app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=6, relief=FLAT, anchor="e", justify=RIGHT, font=('ivy 18'), bg=cor3, fg=cor2 )
app_label.place(x=0, y=0)



# botões

# linha 1

b_1= Button(frame_corpo, command= limpar_tela, text="C", width=11, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2= Button(frame_corpo, command = lambda: entrar_valores("%"), text="%", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=121, y=0)
b_3= Button(frame_corpo, command = lambda: entrar_valores("/"), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=180, y=0)


# linha 2

b_4= Button(frame_corpo, command = lambda: entrar_valores("7"), text="7", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=-1, y=52)
b_5= Button(frame_corpo, command = lambda: entrar_valores("8"), text="8", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=60, y=52)
b_6= Button(frame_corpo, command = lambda: entrar_valores("9"), text="9", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=121, y=52)
b_7= Button(frame_corpo, command = lambda: entrar_valores("*"), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=180, y=52)

# linha 3

b_8= Button(frame_corpo, command = lambda: entrar_valores("4"), text="4", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=-1, y=103)
b_9= Button(frame_corpo, command = lambda: entrar_valores("5"), text="5", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=60, y=103)
b_10= Button(frame_corpo, command = lambda: entrar_valores("6"), text="6", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=121, y=103)
b_11= Button(frame_corpo, command = lambda: entrar_valores("-"), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=180, y=103)

# linha 4


b_12= Button(frame_corpo, command = lambda: entrar_valores("1"), text="1", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=-1, y=154)
b_13= Button(frame_corpo, command = lambda: entrar_valores("2"), text="2", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=60, y=154)
b_14= Button(frame_corpo, command = lambda: entrar_valores("3"), text="3", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=121, y=154)
b_15= Button(frame_corpo, command = lambda: entrar_valores("+"), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=180, y=154)

# linha 5

b_16= Button(frame_corpo, command = lambda: entrar_valores("0"), text="0", width=11, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=205)
b_17= Button(frame_corpo, command = lambda: entrar_valores("."), text=".", width=5, height=2, bg=cor4, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=121, y=205)
b_18= Button(frame_corpo, command = calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=180, y=205)


janela.mainloop()
