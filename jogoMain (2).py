from jogoConst import LIMITE
from console import *
import jogo
import console

def Menu():
    print("Menu provisorio")
    print("1 - JOGAR")
    print("2 - CONFIGURACOES (a fazer)")
    print("3 - INSTRUÇÕES")
    print("4 - SAIR")

def main():
    print("Pressione Enter para começar")
    while True:
        if(kbhit()):
            c = hitKey()
            while (ord(c) != ord('1') and ord(c) != ord('2') and ord(c) != ord('3') != ord(c) != ord('4')):
                console.clear()
                Menu()

                try: 
                    c = hitKey()
                except:
                    c = "0"

            if (ord(c) == ord('1')):
                console.clear()
                jogo.jogar()
            if(ord(c) == ord('2')):
                console.clear()
                jogo.configurar()
            if(ord(c) == ord('3')):
                console.clear()
                jogo.instrucao()
            if(ord(c) == ord('4')):
                console.clear()
                exit(0)              
main()