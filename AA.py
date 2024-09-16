import sys
import os

#Vai armazenar a quantidade de entradas no CMD
arquivos = sys.argv

#funçao que recebe as dicas, e retorna a grade do sudoko de acordo com as dicas
def configuraçao(dicas):
    colunas = [["A", 0,"a"], ["B", 1,"b"], ["C", 2,"c"], ["D", 3,"d"], ["E", 4,"e"], ["F", 5,"f"], ["G", 6, "g"], ["H", 7, "h"], ["I", 8,"i"]]
    sudoko= []
    #CRIANDO O 9X9
    for a in range(9):
        sudoko.append([None]*9)
    
    #ANALISANDO ONDE ESTÃO AS DICAS
    for a in range(len(dicas)):
        #TESTANDO NAS 9 COLUNAS
        for b in range(9):
            #AQUI TÁ TESTANDO ONDE A LETRA DA DICA SE ENCAIXA (ex: A,3: 5), TESTARIA A LETRA A
            if dicas[a][0]==colunas[b][0]:
                #SALVA A COLUNA MARCADA COMO UM NÚMERO              
                cm = colunas[b][1]
        #SUBTRAI-SE 1 DO NÚMERO DA LINHA POIS AQUI OS VALORES VÃO DE 0 A 8 E LÁ É DE 1 A 9, SELECIONANDO ASSIM A CÉLULA DESEJADA
        sudoko[int(dicas[a][2])-1][cm] = int(dicas[a][5])   #AQUI É O NÚMERO DA DICA QUE SERÁ SALVO NA CÉLULA
    return sudoko


# funçao de saida da grade, recebe a grade sudoko e sai de acordo com a configuraçao da tabela
def grade(x,JA):
    clear()
    if JA != "":
       print("Jogada anterior: {}".format(JA))
       print("-"*60)
    for a in range(21):
        if a==0 or a==20:
            print("    A   B   C    D   E   F    G   H   I    ")  # ESCREVE AS LETRAS DAS COLUNAS
        if a==7 or a==13:
            print(" ++===+===+===++===+===+===++===+===+===++ ")
        if a%2==0 and a!=0 and a!=20:
            print("{}|".format(int(a/2)), end="")  #ESCREVE O NÚMERO DAS LINHAS
            for b in range(9):
                if x[int((a/2)-1)][b]!=None:
                    if b==2 or b==5 or b==8:
                        print("| {} |".format(x[int((a/2)-1)][b]), end="")
                    else:
                        print("| {} ".format(x[int((a/2)-1)][b]), end="")
                if x[int((a/2)-1)][b]==None:
                    if b==2 or b==5:
                        print("|   |", end="")
                    else:
                        print("|   ", end="")
            print("||{}".format(int(a/2)))
        if a%2!=0 and a!=7 and a!=13:
            print(" ++---+---+---++---+---+---++---+---+---++ ")


def clear():
  os.system("cls")

#funçao que verifica se um certo espaço na grade e valido de acordo com as regras do jogo
def validaçao(inicial,i,j):
    #i é a linha
    #j é a coluna

    #TOMA A VALIDADE COMO VERDADEIRA ATÉ QUE MOSTRE O CONTRÁRIO
    validade = True

    #CONFERINDO SE HÁ O NÚMERO NA MESMA LINHA OU NA MESMA COLUNA
    for k in range(9):
        #Fixando a linha e conferindo se tem algum igual nas colunas
        if inicial[i][j]==inicial[i][k] and j!=k:
            validade = False
        #Fixando a coluna e verificando se tem algum igual nas linhas
        if inicial[i][j]==inicial[k][j] and k!=i:
            validade = False

    #SE A VALIDADE CONTINUAR COMO VERDADE(OU SEJA, NÃO HÁ O MESMO NÚMERO NA LINHA NEM COLUNA)
    #AQUI TESTAMOS SE NO MESMO QUADRANTE POSSUI ESSE NÚMERO
    if validade== True:
        #ESTÁ NOS QUADRANTES DE CIMA
        if i<=2:
            for l in range(3):
                #ESTÁ NO PRIMEIRO QUADRANTE
                if j<=2:
                    for m in range(3):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
                #ESTÁ NO SEGUNDO QUADRANTE
                if 5>=j>2:
                    for m in range(3,6):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
                #ESTÁ NO TERCEIRO QUADRANTE
                if j>5:
                    for m in range(6,9):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
        
        #ESTÁ NOS QUADRANTES DO MEIO
        if 5>=i>2:
            for l in range(3,6):
                #PRIMEIRO
                if j<=2:
                    for m in range(3):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
                #SEGUNDO
                if 5>=j>2:
                    for m in range(3,6):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
                #TERCEIRO
                if j>5:
                    for m in range(6,9):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
        #ESTÁ NOS QUADRANTES DE BAIXO
        if i>5:
            for l in range(6,9):
                #PRIMEIRO
                if j<=2:
                    for m in range(3):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
                #SEGUNDO
                if 5>=j>2:
                    for m in range(3,6):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
                #TERCEIRO
                if j>5:
                    for m in range(6,9):
                        if inicial[i][j]==inicial[l][m] and (l!=i or m!=j):
                            validade=False
    return validade


#funçao define as possibilidades para uma determinada casa no jogo
def possibilidades(inicial,i,j):
    possib=[1,2,3,4,5,6,7,8,9]
    naoposs=[]
    for k in range(9):
        if inicial[i][k]!=None:
            naoposs.append(inicial[i][k])
        if inicial[k][j]!=None:
            naoposs.append(inicial[k][j])
        if i<=2:
            for l in range(3):
                if j<=2:
                    for m in range(3):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
                if 5>=j>2:
                    for m in range(3,6):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
                if j>5:
                    for m in range(6,9):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
        if 5>=i>2:
            for l in range(3,6):
                if j<=2:
                    for m in range(3):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
                if 5>=j>2:
                    for m in range(3,6):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
                if j>5:
                    for m in range(6,9):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
        if i>5:
            for l in range(6,9):
                if j<=2:
                    for m in range(3):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
                if 5>=j>2:
                    for m in range(3,6):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
                if j>5:
                    for m in range(6,9):
                        if inicial[l][m]!=None:
                            naoposs.append(inicial[l][m])
    if len(naoposs)!=0:
        for k in range(len(naoposs)):
            if naoposs[k] in possib:
                possib.remove(naoposs[k])
    return possib

#Usado para descobrir qual a coluna que iremos inserir o valor dado pelo usuário
def coluna(N):
    colunas = [["A", 0,"a"], ["B", 1,"b"], ["C", 2,"c"], ["D", 3,"d"], ["E", 4,"e"], ["F", 5,"f"], ["G", 6, "g"], ["H", 7, "h"], ["I", 8,"i"]]
    j = "erro"
    for a in range(9):
        #CONFERE SE A LETRA DADA PELO USUÁRIO CORRESPONDE A ALGUMA DAS COLUNAS
        if N == colunas[a][0] or N == colunas[a][2]:
            j = a
        
    return j
        
def interativo(dicas):
  sudoku= configuraçao(dicas)
  
  #Vai armazenar a jogada anterior e apresentar na interface
  JA = ""

  if len(dicas)>80:
        print("Quantidade de dicas acima do limite!")
  else:
    erro=0
    #Vai validar todas as dicas preenchidas na grade
    for i in range(9):
        for j in range(9):
          if sudoku[i][j]!=None:
            if validaçao(sudoku,i,j) == False:
              erro=1
    if erro==1:
        print("Grade inicial invalida")
    
    else:
      grade(sudoku, JA)
      parada = 0
      for i in range(9):
            for j in range(9):
                if sudoku[i][j]!=None:
                    parada+=1
      
      #O número máximo de jogadas é 81, então, chegando nelas, para de pedir novas jogadas
      while parada<81:
        N = input("\nNova jogada: ").split()
        N = "".join(N)

        if len(N) == 5 or len(N) == 4:
            erro = 1
            JA = N

            if N[0]=="?":
                Nj = coluna(N[1])
                Ni=int(N[3])-1
                possibilidade = possibilidades(sudoku, Ni, Nj)
                print("as possibilidades para essa casa sao:")
                for i in range(len(possibilidade)):
                    print(possibilidade[i], end=" ")
                print("\n")

            elif N[0]=="!":
                Nj=coluna(N[1])
                Ni=int(N[3])-1
                if sudoku[Ni][Nj]!=None:
                    erro = 0
                    for i in range(len(dicas)):
                        if coluna(N[1])==coluna(dicas[i][0]):
                            if Ni+1==int(dicas[i][2]):
                                erro=1
                    if erro==1:
                        print("Posiçao correspodente a uma dica")
                    else:
                        sudoku[Ni][Nj]=None
                        parada-=1
                        grade(sudoku,JA)
                else:
                    print("Posiçao informada nao tem um numero!")

            else:
                N = N.split(":")
                N[0] = N[0].split(",")
                if coluna(N[0][0])=="erro":
                    print("\njogada invalida!")
                else:
                    Nj= coluna(N[0][0])
                    Ni= int(N[0][1])-1
                    Nv= int(N[1][0])
                    if Ni>8 or Ni<0:
                        print("\njogada invalida!")
                    else:
                        erro = 0
                    for i in range(len(dicas)):
                        if Nj==coluna(dicas[i][0]):
                            if Ni+1==int(dicas[i][2]):
                                erro=1
                    if erro==1:
                        print("\njogada invalida!")
                    else:
                        if sudoku[Ni][Nj]!=None:
                            print("\nEspaço preenchido! deseja sobescrever com essa entrada?")
                            print("Responda com S para sim, e N para nao")
                            R = input()
                            if R=="S":
                                K = sudoku[Ni][Nj]
                                sudoku[Ni][Nj]=Nv
                                if validaçao(sudoku, Ni, Nj)==False:
                                    print("jogada invalida!")
                                    sudoku[Ni][Nj] = K
                            else:
                                grade(sudoku,JA)
                        else:
                            sudoku[Ni][Nj]=Nv
                            if validaçao(sudoku, Ni, Nj)==False:
                                print("jogada invalida!")
                                sudoku[Ni][Nj]=None
                            if validaçao(sudoku, Ni,Nj)==True:
                                parada+=1
                                grade(sudoku,JA)
        else:
            print("\nJogada invalida!")
      grade(sudoku,JA)
      print("PARABENS!!!")


# Função principal do modo batch
def batch(dicas, jogadas):
  sudoku = configuraçao(dicas)

  #REMOVE AS JOGADAS INDENTICAS
  jogadas_unicas = list(set(jogadas))


  if len(dicas)>80:
    print("Configuracao de dicas invalida.")
  else:
    erro=0
    #Vai validar todas as dicas preenchidas na grade
    for i in range(9):
        for j in range(9):
          if sudoku[i][j]!=None:
            if validaçao(sudoku,i,j) == False:
              erro=1
    if erro==1:
      print("Configuracao de dicas invalida.")
    
    else:
      parada = 0
      for i in range(9):
        for j in range(9):
          if sudoku[i][j]!=None:
            parada+=1
      
      for jogada in jogadas_unicas:
        
        erro = 0
        jogada = jogada.split()
        jogada = "".join(jogada)
        
        #Caso a jogada tenha mais de 5
        if len(jogada) != 5:
           erro = 1
        JA = jogada
        
        jogada = jogada.split(":")
        jogada[0] = jogada[0].split(",")
        if coluna(jogada[0][0]) == "erro" or erro == 1:
            print("A jogada ({},{}) = {} eh invalida!".format(jogada[0][0], jogada[0][1], jogada[1]))
        else:
            Nj= coluna(jogada[0][0])
            Ni= int(jogada[0][1])-1
            Nv= int(jogada[1][0])
            if Ni>8 or Ni<0:
              print("A jogada ({},{}) = {} eh invalida!".format(jogada[0][0], jogada[0][1], jogada[1]))
            else:
              erro = 0
            for i in range(len(dicas)):
              if Nj==coluna(dicas[i][0]):
                if Ni+1==int(dicas[i][2]):
                  erro=1
            if erro==1:
              print("A jogada ({},{}) = {} eh invalida!".format(jogada[0][0], jogada[0][1], jogada[1]))
            else:
              if sudoku[Ni][Nj]!=None:
                print("A jogada ({},{}) = {} eh invalida!".format(jogada[0][0], jogada[0][1], jogada[1]))
              else:
                sudoku[Ni][Nj]=Nv
                if validaçao(sudoku, Ni, Nj)==False:
                  print("A jogada ({},{}) = {} eh invalida!".format(jogada[0][0], jogada[0][1], jogada[1]))
                  sudoku[Ni][Nj]=None
                if validaçao(sudoku, Ni,Nj)==True:
                  parada += 1
    if parada == 81:
        print("A grade foi preenchida com sucesso!")
    else:
        print("A grade nao foi preenchida!")

          
         

def main():
    #Vai verificar quantos arquivos vão ser lidos, caso seja 2 executa o INTERATIVO, caso seja 3, executa o BATCH
  if len(arquivos) == 2:
    #Roda o MODO INTERATIVO
    with open(arquivos[1], "r") as dicas:
      dicas = dicas.readlines()
    interativo(dicas)

  #Roda o MODO BATCH
  elif len(arquivos) == 3:
    with open(arquivos[1], "r") as dicas:
      dicas = dicas.readlines()

    with open(arquivos[2], "r") as jogadas:
      jogadas = jogadas.readlines()

    batch(dicas, jogadas)

  else:
    print("erro com o número de arquivos inseridos")

main()