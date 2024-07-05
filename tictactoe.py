import os
#-----------------------------------------VARIÁVEIS--------------------------------------#
p1 = 'a'
p2 = 'b'
p3 = 'c'
p4 = 'd'
p5 = 'e'
p6 = 'f'
p7 = 'g'
p8 = 'h'
p9 = 'i'
x = '\033[2;32mX\033[m'
bola = '\033[2;35mO\033[m'
permitido = [p1, p2, p3, p4, p5, p6, p7, p8, p9]                                                         
campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
verdade = True
turno = 0
#----------------------------------------EXECUÇÃO------------------------------------------------#
#-------------#FUNÇÕES#---------#
def muda_turno():
    global turno
    turno = turno + 1  
#-------------------------------#

#substituir posição escolhida por X se j1 por O se j2
def limpeza():
     os.system('cls') or None
def substituir1():
        global p1, p2, p3, p4, p5, p6, p7, p8, p9, campo
        if j1 == p1:
             permitido[0] = 0
             p1 = '\033[2;32mX\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
        elif j1 == p2:
             permitido[1] = 0
             p2 = '\033[2;32mX\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
        elif j1 == p3:
             permitido[2] = 0
             p3 = '\033[2;32mX\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
        elif j1 == p4:
             permitido[3] = 0
             p4 = '\033[2;32mX\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
        elif j1 == p5:
             permitido[4] = 0
             p5 = '\033[2;32mX\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
        elif j1 == p6:
             permitido[5] = 0
             p6 = '\033[2;32mX\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
        elif j1 == p7:
             permitido[6] = 0
             p7 = '\033[2;32mX\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
        elif j1 == p8:
             permitido[7] = 0
             p8 = '\033[2;32mX\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
        elif j1 == p9:
             permitido[8] = 0
             p9 = '\033[2;32mX\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'

#----------------------------#
def substituir2():
        global p1, p2, p3, p4, p5, p6, p7, p8, p9, campo
        if j2 == p1:
             permitido[0] = 0
             p1 = '\033[2;35mO\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
        elif j2 == p2:
             permitido[1] = 0
             p2 = '\033[2;35mO\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
        elif j2 == p3:
             permitido[2] = 0
             p3 = '\033[2;35mO\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
        elif j2 == p4:
             permitido[3] = 0
             p4 = '\033[2;35mO\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
        elif j2 == p5:
             permitido[4] = 0
             p5 = '\033[2;35mO\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
        elif j2 == p6:
             permitido[5] = 0
             p6 = '\033[2;35mO\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
        elif j2 == p7:
             permitido[6] = 0
             p7 = '\033[2;35mO\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
        elif j2 == p8:
             permitido[7] = 0
             p8 = '\033[2;35mO\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'
        elif j2 == p9:
             permitido[8] = 0
             p9 = '\033[2;35mO\033[m'
             campo = f' {p1} |  {p2}  |  {p3}\n___|_____|___\n {p4} |  {p5}  |  {p6}\n___|_____|___\n {p7} |  {p8}  |  {p9}\n   |     |'

#---------------------------------------------------------------------------------------------#
def vitoria():
     global verdade
     #final em horizontal
     if x == p1 == p2 == p3 or bola == p1 == p2 == p3:
          print(campo)
          print(f'\n\033[1;3;4;41;mJOGADOR\033[m {jogador} GANHOU!!')
          verdade = False
          
     elif x == p4 == p5 == p6 or bola == p4 == p5 == p6:
          print(campo)
          print(f'\n\033[1;3;4;40;mJOGADOR {jogador} GANHOU!!\033[m')
          verdade = False
          
     elif x == p7 == p8 == p9 or bola == p7 == p8 == p9:
          print(campo)
          print(f'\n\033[1;3;4;40;mJOGADOR {jogador} GANHOU!!\033[m')
          verdade = False
          
          #final em vertical
     elif x == p1 == p4 == p7 or bola == p1 == p4 == p7:
          print(campo)
          print(f'\n\033[1;3;4;40;mJOGADOR {jogador} GANHOU!!\033[m')
          verdade = False
          
     elif x == p2 == p5 == p8 or bola == p2 == p5 == p8:
          print(campo)
          print(f'\n\033[1;3;4;40;mJOGADOR {jogador} GANHOU!!\033[m')
          verdade = False
          
     elif x == p3 == p6 == p9 or bola == p3 == p6 == p9:
          print(campo)
          print(f'\n\033[1;3;4;40;mJOGADOR {jogador} GANHOU!!\033[m')
          verdade = False
          
     #final em diagonal
     elif x == p1 == p5 == p9 or bola == p1 == p5 == p9:
          print(campo)
          print(f'\n\033[1;3;4;40;mJOGADOR {jogador} GANHOU!!\033[m')
          verdade = False
          
     elif x == p3 == p5 == p7 or bola == p3 == p4 == p7:
          print(campo)
          print(f'\n\033[1;3;4;40;mJOGADOR {jogador} GANHOU!!\033[m')
          verdade = False
          
#---------------------------#
while verdade:
    limpeza()
    print(campo)
    muda_turno()
        #jogador 1
    if turno % 2 == 1:
        jogador = '\033[1;3;4;32m1\033[m'
        j1 = input('\033[1;4;32mJOGADOR 1\033[m: DIGITE UMA OPÇÃO VÁLIDA: ')
        if j1 in permitido:
             substituir1()
        else:
             print('DÍGITO INVÁLIDO')
             print('PERDEU A VEZ!')
        #jogador 2
    elif turno % 2 == 0:
        jogador = '\033[1;3;4;35m2\033[m'
        #j2 escolhe uma posiçao que NAO tenha sido escolhida
        j2 = input('\033[1;4;35mJOGADOR 2\033[m: DIGITE UMA OPÇÃO VÁLIDA: ')
        if j2 in permitido:
             substituir2()
        else:
             print('DÍGITO INVÁLIDO')
             print('PERDEU A VEZ')
    if turno == 9:
         print('\033[1;4;31;47mEMPATE\033[m')
         break
    vitoria()
#--------------------------------------------------------------------------------------------------#

