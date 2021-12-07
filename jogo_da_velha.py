tabLista=[["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"]]
def main():
    print("JOGO DA VELHA")
    print("O PRIMEIRO A JOGAR FICARÁ COM x E O SEGUNDO JOGADOR FICARA COM o\n")
    cenario(0,0," ")
    controleJogo()


def cenario(posx,posy,peca):   
    tabLista[posx][posy]="["+peca+"]"
        
    for i in range(3):
         
         print("\n")
         for j in range(3):
           
           print(tabLista[i][j],end=' ')        
def controleJogo():
    listaPosJogadas=[[-1,-1]]
    num_rodadas=0
    contJog=0
    
    while num_rodadas<9:
         
        
        if num_rodadas%2==0:
            print("\njoga o jogador 1")
            peca="x"
        else:
            print("\njoga o jogador 2")
            peca="o"
        i=int(input("escolha uma linha de 0 ate 2\n"))
        j=int(input("escolha uma coluna de 0 ate 2\n"))
        print(60*"\n")
        while i>2 or j>2 or i<0 or j<0:
             print(" a linha e a coluna tem que esta entre 0 e 2.\n Voce escolheu um numero diferente para linha ou coluna\n")
             i=int(input("escolha uma linha de 0 ate 2\n"))
             j=int(input("escolha uma coluna de 0 ate 2\n"))
             
        while [i,j] in listaPosJogadas :
            print(" a linha e a coluna tem que esta entre 0 e 2.\n Voce tem que escolher um numero diferente para linha ou coluna,pois, ja foi escolhido:","linha:",i,"e","coluna:",j,"\n")
            i=int(input("escolha uma linha de 0 ate 2\n"))
            j=int(input("escolha uma coluna de 0 ate 2\n"))
            while i>2 or j>2 or i<0 or j<0:
              print(" a linha e a coluna tem que esta entre 0 e 2.\n Voce escolheu um numero diferente para linha ou coluna\n")
              i=int(input("escolha uma linha de 0 ate 2\n"))
              j=int(input("escolha uma coluna de 0 ate 2\n"))
       
        listaPosJogadas.append([i,j])
        cenario(i,j,peca)
        analise=analisarResultado()
        if analise==1:
            print("\n\nPARABENS PELA VITORIA DO JOGADOR 1.")
            break
        if analise==2:
            print("\n\nPARABENS PELA VITORIA DO JOGADOR 2.")
            break
        num_rodadas+=1
        if num_rodadas==9:
           print("\n\nDEU VELHA.OS JOGADORES EMPATARAM")
      
    
        
def analisarResultado():    
    if (tabLista[0][0]=="[o]" and tabLista[0][1]=="[o]" and tabLista[0][2]=="[o]") or (tabLista[1][0]=="[o]" and tabLista[1][1]=="[o]" and tabLista[1][2]=="[o]") or (tabLista[2][0]=="[o]" and tabLista[2][1]=="[o]" and tabLista[2][2]=="[o]")or (tabLista[0][0]=="[o]" and tabLista[1][0]=="[o]" and tabLista[2][0]=="[o]")or (tabLista[0][1]=="[o]" and tabLista[1][1]=="[o]" and tabLista[2][1]=="[o]")or (tabLista[0][2]=="[o]" and tabLista[1][2]=="[o]" and tabLista[2][2]=="[o]")or (tabLista[0][0]=="[o]" and tabLista[1][1]=="[o]" and tabLista[2][2]=="[o]")or (tabLista[0][2]=="[o]" and tabLista[1][1]=="[o]" and tabLista[2][0]=="[o]"):
        return 2
    if (tabLista[0][0]=="[x]" and tabLista[0][1]=="[x]" and tabLista[0][2]=="[x]") or (tabLista[1][0]=="[x]" and tabLista[1][1]=="[x]" and tabLista[1][2]=="[x]") or (tabLista[2][0]=="[x]" and tabLista[2][1]=="[x]" and tabLista[2][2]=="[x]")or (tabLista[0][0]=="[x]" and tabLista[1][0]=="[x]" and tabLista[2][0]=="[x]")or (tabLista[0][1]=="[x]" and tabLista[1][1]=="[x]" and tabLista[2][1]=="[x]")or (tabLista[0][2]=="[x]" and tabLista[1][2]=="[x]" and tabLista[2][2]=="[x]")or (tabLista[0][0]=="[x]" and tabLista[1][1]=="[x]" and tabLista[2][2]=="[x]")or (tabLista[0][2]=="[x]" and tabLista[1][1]=="[x]" and tabLista[2][0]=="[x]"):
        return 1
main()

