from console import *
from time import sleep
from random import randrange
from jogoConst import *
from jogoMath import solve1, solve2
import console

def instrucao():
    print("Este jogo é baseado em turnos")
    print("Os dois jogadores irão competir para ver quem acerta o inimigo primeiro")
    print("O primeiro a tirar todas as vidas do inimigo será o vencedor")
    print("Utilize 'A' e 'D' para aumentar ou diminuir a força")
    print("Pressione 'ESPAÇO' para fazer sua jogada")
    input("Boa Sorte!")

def configurar():
    input("Fase de testes... Pressione Enter para retornar")

def jogar():
    
    input("teste do prototipo - pressione enter para continuar")
    
    vidas1 = 3
    vidas2 = 3


    init(LIMITE_VERT)
    gotoxy(0, 1)
    print('-' * LIMITE, end='', flush=True)
    reset(0, 1, LIMITE_VERT, LIMITE)
    print('_' * LIMITE, end='', flush=True)
    gotoxy(0, LIMITE_VERT - 28)
    print('_' * LIMITE, end='', flush=True)
    gotoxy(0, LIMITE_VERT - 4)
    print('_' * LIMITE, end='', flush=True)
    gotoxy((LIMITE / 2) - 24, LIMITE_VERT - 3)
    print("Seu nível de força é: ", end='')
    gotoxy((LIMITE / 2) - 55, LIMITE_VERT - 2)
    print(f"Vidas P1: {vidas1}", end='')
    gotoxy((LIMITE / 2) + 45, LIMITE_VERT - 2)
    print(f"Vidas P2: {vidas2}", end='')

    gotoxy(10 + randrange(100) ,4 + randrange(8))
    print("☼", end='', flush=True)
    gotoxy(10 + randrange(100),4 + randrange(8))
    print("*", end='',flush=True)
    gotoxy(10 + randrange(100),4 + randrange(8))
    print("*", end='',flush=True)
    gotoxy(10 + randrange(100),4 + randrange(8))
    print("☼", end='',flush=True)
    gotoxy(10 + randrange(100),4 + randrange(8))
    print("☼", end='',flush=True)
    gotoxy(10 + randrange(100),4 + randrange(8))
    print("*", end='',flush=True)
    gotoxy(10 + randrange(100) ,4 + randrange(8))
    print("☼", end='',flush=True)
    gotoxy(10 + randrange(100),4 + randrange(8))
    print("*", end='',flush=True)
    gotoxy(10 + randrange(100),4 + randrange(8))
    print("*", end='',flush=True)
    gotoxy(10 + randrange(100),4 + randrange(8))
    print("*", end='',flush=True)
    gotoxy(10 + randrange(100) ,4 + randrange(8))
    print("*", end='',flush=True)
    gotoxy(10 + randrange(100) ,4 + randrange(8))
    print("*", end='',flush=True)
    gotoxy(10 + randrange(100) ,4 + randrange(8))
    print("*", end='',flush=True)
    gotoxy(10 + randrange(100),4 + randrange(8))
    print("☼", end='',flush=True)
    gotoxy(10 + randrange(100) ,4 + randrange(8))
    print("☼", end='',flush=True)
    gotoxy(10 + randrange(100) ,4 + randrange(8))
    print("*", end='',flush=True)


    #gotoxy(115,0)



    discos = [ { "img":")","x":0, "y":0, "ativo": False, "traj": {"A":0, "B": 0, "C": 0} } ]

    macacoEsq = [ {"img":"|O>", "x":0, "y":0, "ativo": True} ]

    macacoDir = [ {"img":"<O|", "x":0, "y":0, "ativo": True} ]


    
    x_gorilaDir = LIMITE - 5
    y_gorilaDir = LIMITE_VERT - 6 - randrange(10)
    x_gorilaEsq = 3
    y_gorilaEsq = LIMITE_VERT - 6 - randrange(10)
    coeflinear = 0.5

    gotoxy(1,y_gorilaEsq)
    print("_"*20,end='',flush=True)
    gotoxy(21,LIMITE_VERT-10 - randrange(5))
    print("_"*20,end='',flush=True)
    gotoxy(41,LIMITE_VERT-10 - randrange(5))
    print("_"*20,end='',flush=True)
    gotoxy(61,LIMITE_VERT- 10 - randrange(5))
    print("_"*20,end='',flush=True)
    gotoxy(81,LIMITE_VERT-10 - randrange(5))
    print("_"*20,end='',flush=True)
    gotoxy(101,y_gorilaDir)
    print("_"*20,end='',flush=True)
    
    while True:
        if(kbhit()):
            c = hitKey()  
            if(ord(c) == ord('d') or ord(c) == ord('D')):
                if(coeflinear <= 0.95 and coeflinear >= 0):
                    coeflinear += 0.05
                elif(coeflinear >= 0.90):
                    coeflinear = 1
                
            if(ord(c) == ord('a') or ord(c) == ord('A')):
                if(coeflinear <= 1 and coeflinear >= 0.05):
                    coeflinear -= 0.05
                elif(coeflinear <= 0.05):
                    coeflinear = 0

            if(ord(c) == ord(' ')):
                for disco in discos:
                    if (not disco["ativo"]):
                        disco["ativo"] = True
                        disco["x"] = x_gorilaEsq
                        disco["y"] = y_gorilaEsq
                        disco["traj"]["C"] = disco["y"]
                        disco["traj"]["A"] = (max(-15, 4 - disco["traj"]["C"])) / ((LIMITE/2) * (LIMITE/2 - LIMITE))
                        disco["traj"]["B"] = - coeflinear

            if(ord(c) == ord("""'""")):
                console.clear()
                print("Você saiu do jogo")
                exit(0)

            if(ord(c) == ord('m') or ord(c) == ord('M')):
                console.clear()
                print("Pressione Enter para ir para o Menu")
                break

        gotoxy((LIMITE / 2) , LIMITE_VERT - 3)
        if(round(coeflinear,3) == 0):
            print("0%  ")
        elif(round(coeflinear,3) == 0.05):
            print("5% ")
        elif(round(coeflinear,3) == 0.10):
            print("10% ")
        elif(round(coeflinear,3) == 0.15):
            print("15% ")
        elif(round(coeflinear,3) == 0.20):
            print("20% ")
        elif(round(coeflinear,3) == 0.25):
            print("25% ")
        elif(round(coeflinear,3) == 0.30):
            print("30% ")
        elif(round(coeflinear,3) == 0.35):
            print("35% ")
        elif(round(coeflinear,3) == 0.40):
            print("40% ")
        elif(round(coeflinear,3)== 0.45):
            print("45% ")
        elif(round(coeflinear,3) == 0.50):
            print("50%")
        elif(round(coeflinear,3) == 0.55):
            print("55% ")
        elif(round(coeflinear,3) == 0.60):
            print("60% ")
        elif(round(coeflinear,3) == 0.65):
            print("65% ")
        elif(round(coeflinear,3) == 0.70):
            print("70% ")
        elif(round(coeflinear,3) == 0.75):
            print("75% ")
        elif(round(coeflinear,3) == 0.80):
            print("80% ")
        elif(round(coeflinear,3) == 0.85):
            print("85% ")
        elif(round(coeflinear,3) == 0.90):
            print("90% ")
        elif(round(coeflinear,3) == 0.95):
            print("95% ")
        elif(round(coeflinear,3) == 1):
            print("100%")

        for disco in discos:
                
            gotoxy(disco["x"], disco["y"])
            print("  ", end='')

            
            gotoxy((LIMITE / 2) + 3, (LIMITE_VERT - 3) )
            if disco["ativo"]:
            
                disco["x"] += 1 
                disco["y"] = int(solve2(disco["traj"]["A"], disco["traj"]["B"], disco["traj"]["C"], disco["x"]))

                if disco["y"] <= LIMITE_VERT - 27:
                    disco["ativo"] = False
                    gotoxy((LIMITE / 2) - 48, LIMITE_VERT - 2)
                else:
                    gotoxy(disco["x"], disco["y"])
                    print(disco["img"], end='') 

                if disco["y"] >= LIMITE_VERT-5:
                    disco["ativo"] = False
                    gotoxy((LIMITE / 2) - 48, LIMITE_VERT - 2)
                    break
                else:
                    gotoxy(disco["x"], disco["y"])
                    print(disco["img"], end='') 

                
            else:
                print(' ' * 30, end='')


        gotoxy(x_gorilaEsq, y_gorilaEsq)
        print("|O>", end='')

        gotoxy(x_gorilaDir, y_gorilaDir)
        print("<o|", end='')
        


        
        acertouDir = 0
        acertouEsq = 0
        
        for macaco in macacoDir:
            for disco in discos:
                if (macaco["ativo"] and disco["ativo"] and round(macaco["x"]) == round(disco["x"]) and round(macaco["y"]) == round(disco["y"])):
                    acertouDir = True
                    disco["ativo"] = False
                    macaco["ativo"] = False
                    break

        for macaco in macacoEsq:
            for disco in discos:
                if (macaco["ativo"] and disco["ativo"] and round(macaco["x"]) == round(disco["x"]) and round(macaco["y"]) == round(disco["y"])):
                    acertouEsq = True
                    disco["ativo"] = False
                    macaco["ativo"] = False
                    break
        
        if (acertouDir):
            vidas2 -= 1
            gotoxy(LIMITE/2 + 3,0)
            print("%0.2f" % vidas2, end='')

        if (acertouEsq):
            vidas1 -= 1
            gotoxy(LIMITE/2 + 3,0)
            print("%0.2f" % vidas1, end='')
        
        if (vidas2 == 0):
            console.clear()
            gotoxy(0,5)
            print(" Macaco Esquerdo Wins ")
            gotoxy(LIMITE/2 - 18,LIMITE_VERT-4)
            print("Pressione Enter para voltar para o menu ")
            break

        if (vidas1 == 0):
            console.clear()
            gotoxy(0,5)
            print(" Macaco Direito Wins ")
            gotoxy(LIMITE/2 - 18,LIMITE_VERT-4)
            print("Pressione Enter para voltar para o menu ")
            break
        print(end='',flush=True)
        sleep(0.03)