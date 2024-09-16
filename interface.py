from tkinter import *

janela = Tk()

def escrever_numero(jogada):
    num1 = Label(janela.frame_1, text= jogada, bg='white' )
    num1.place(relx=0.13, rely=0.12)




#Tamanho inicial
janela.geometry("1200x800")
janela.title("Sudoku")

#Modificações da janela
janela.configure(background = "#1e3743")

#janela.resizable(False, False) #Não permite mudar o tamanho da janela

#Criando um frame para a grade do sudoku
janela.frame_1 = Frame(janela, bd=4, bg='white', highlightbackground='#000000', highlightthickness=5)
janela.frame_1.place(relx= 0.1, rely=0.05, relwidth= 0.8, relheight=0.7)

#Criando um frame pra deixar a caixa de resposta
janela.frame_2 = Frame(janela, bd=4, bg='white', highlightbackground='#000000', highlightthickness=5)
janela.frame_2.place(relx= 0.1, rely=0.78, relwidth= 0.8, relheight=0.1)

#Função do botão nova jogada, vai obter a nova jogada
def nvjg_botão():
    #Vai passar a Nova jogada para a tela
    escrever_numero(jogada.get())

    Nova_jogada = jogada.get()
    limpa_tela()
    return Nova_jogada

def limpa_tela():
    jogada.delete(0, END)

#Nome Sudoku na tela
Nome_s = Label(janela, text="Sudoku", background="#1e3743", fg='white', font=('verdana', 15, 'bold'))
Nome_s.place(relx=0.46, rely=0)


#BOTÕES
botao_iniciar = Button(janela.frame_2, text="Nova jogada", height=2, width=15, bd=2, bg='#107db2', fg='white', font=('verdana', 10, 'bold'), command=nvjg_botão)
botao_iniciar.place(relx=0.6, rely=0.08)


#Texto "Insira sua jogada"
Nvjg = Label(janela.frame_2, text="Insira sua jogada: ", bg="#d3d3d3")
Nvjg.place(relx=0.47, rely=0)


#Onde será digitado a nova jogada
jogada = Entry(janela.frame_2, bg='lightgray')
jogada.place(relx=0.47, rely=0.36, relwidth=0.11)


#limpa a área da jogada
bt_limpar = Button(janela.frame_2, text="limpar", height=1, width=7, bd=2, bg='#107db2', fg='white', font=('verdana', 7, 'bold'), command=limpa_tela)
bt_limpar.place(relx=0.03, rely=0.08)

#Desenhando a grade
grade1 = Label(janela.frame_1, text="|", bg='black')
grade1.place(relx=0.35, rely=0.05, relheight=0.9, relwidth=0.01)
grade1 = Label(janela.frame_1, text="|", bg='black')
grade1.place(relx=0.65, rely=0.05, relheight=0.9, relwidth=0.01)

grade2 = Label(janela.frame_1, text="-", bg='black')
grade2.place(relx=0.1, rely=0.35, relheight=0.01, relwidth=0.8)
grade2 = Label(janela.frame_1, text="-", bg='black')
grade2.place(relx=0.1, rely=0.65, relheight=0.01, relwidth=0.8)

#linhas verticais
grade1 = Label(janela.frame_1, text="|", bg='black')
grade1.place(relx=0.18, rely=0.05, relheight=0.9, relwidth=0.001)
grade1 = Label(janela.frame_1, text="|", bg='black')
grade1.place(relx=0.28, rely=0.05, relheight=0.9, relwidth=0.001)

grade1 = Label(janela.frame_1, text="|", bg='black')
grade1.place(relx=0.45, rely=0.05, relheight=0.9, relwidth=0.001)
grade1 = Label(janela.frame_1, text="|", bg='black')
grade1.place(relx=0.55, rely=0.05, relheight=0.9, relwidth=0.001)

grade1 = Label(janela.frame_1, text="|", bg='black')
grade1.place(relx=0.74, rely=0.05, relheight=0.9, relwidth=0.001)
grade1 = Label(janela.frame_1, text="|", bg='black')
grade1.place(relx=0.82, rely=0.05, relheight=0.9, relwidth=0.001)

#linhas horizontais
grade2 = Label(janela.frame_1, text="-", bg='black')
grade2.place(relx=0.1, rely=0.15, relheight=0.001, relwidth=0.8)
grade2 = Label(janela.frame_1, text="-", bg='black')
grade2.place(relx=0.1, rely=0.25, relheight=0.001, relwidth=0.8)

grade2 = Label(janela.frame_1, text="-", bg='black')
grade2.place(relx=0.1, rely=0.45, relheight=0.001, relwidth=0.8)
grade2 = Label(janela.frame_1, text="-", bg='black')
grade2.place(relx=0.1, rely=0.55, relheight=0.001, relwidth=0.8)

grade2 = Label(janela.frame_1, text="-", bg='black')
grade2.place(relx=0.1, rely=0.75, relheight=0.001, relwidth=0.8)
grade2 = Label(janela.frame_1, text="-", bg='black')
grade2.place(relx=0.1, rely=0.85, relheight=0.001, relwidth=0.8)

grade_ext = Label(janela.frame_1, text="-", bg='black')
grade_ext.place(relx=0.1, rely=0.05, relheight=0.01, relwidth=0.8)
grade_ext = Label(janela.frame_1, text="-", bg='black')
grade_ext.place(relx=0.1, rely=0.95, relheight=0.01, relwidth=0.8)

grade_ext = Label(janela.frame_1, text="|", bg='black')
grade_ext.place(relx=0.1, rely=0.05, relheight=0.9, relwidth=0.01)
grade_ext = Label(janela.frame_1, text="|", bg='black')
grade_ext.place(relx=0.9, rely=0.05, relheight=0.91, relwidth=0.01)

for i in range(9):
    num1 = Label(janela.frame_1, text= input(), bg='white' )
    num1.place(relx=0.13, rely=0.12)


janela.mainloop()