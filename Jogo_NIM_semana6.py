def computador_escolhe_jogada(n,m):
    t=True
    i=1
    while(t):
        if(i==m):
            resultado=i
            t=False
            return resultado
        elif((n-i) % (m+1)==0):
            resultado=i
            t=False
            return resultado
        i=i+1

def usuario_escolhe_jogada(n,m):
    n=int(input("Quantas peças você vai tirar?\n "))
    while(n>m or n<=0 ):
        print("Oops! Jogada inválida! Tente de novo.\n")
        n=int(input("Quantas peças você vai tirar?\n"))
    return n

def partida():
    n=int(input("Quantas peças? "))
    m=int(input("Limite de peças por jogada?"))
    print("\n")
    while(m>n):
        print("O limite de peças nao pode ser maior q o total delas.")
        m=int(input("Limite de peças por jogada? "))
    if(n % (m+1)==0):
        print("Você começa!\n")
        while(n>0):
            pecas=usuario_escolhe_jogada(n,m)
            print("Você tirou", pecas,"peças.")
            n=n-pecas
            if(n==1):
                print("Agora resta apenas uma peça no tabuleiro.")
            elif(n==0):
                None
            else:
                print("Agora restam",n,"peças.")
            resultado=computador_escolhe_jogada(n,m)
            n=n-resultado
            print("O computador tirou",resultado,"peças.")
            if(n==1):
                print("Agora resta apenas uma peça no tabuleiro.")
            elif(n==0):
                None
            else:
                print("Agora restam",n,"peças.")
            if(n==0):
                break
        print('Fim do Jogo! O computador ganhou!\n')    
        
    else:
        print("Computador começa\n")
        while(n>0):
            resultado=computador_escolhe_jogada(n,m)
            n=n-resultado
            if(n==1):
                print("Agora resta apenas uma peça no tabuleiro.")
            elif(n==0):
                None
            else:
                print("O computador tirou",resultado,"peças.")
                print("Agora restam",n,"peças.\n")
            if(n==0):
                break
            pecas=usuario_escolhe_jogada(n,m)
            n=n-pecas
            if(n==1 ):
                print("Agora resta apenas uma peça no tabuleiro.")
            elif(n==0):
                None
            else:
                print("Você tirou", pecas,"peças.")
                print("Agora restam",n,"peças.\n")
        print('Fim do Jogo! O computador ganhou!\n')
                
def campeonato():
    print("Bem-vindo ao jogo do NIM! Escolha: ","\n")
    print("1 - para jogar uma partida isolada\n2 - para jogar um campeonato")
    r=int(input(""))
    while(r!=1 and r!=2):
        print("Bem-vindo ao jogo do NIM! Escolha: ","\n")
        print("1 - para jogar uma partida isolada\n2- para jogar um campeonato")
        r=int(input(""))
    if(r==2):
        b=1
        print("Voce escolheu um campeonato!","\n")
        while(b<=3):
            print("**** Rodada",b,"****","\n")
            partida()
            b=b+1
        print("Placar: Você 0 X 3 Computador")
    else:
        print("Voce escolheu uma partida isolada")
        partida()





campeonato()
