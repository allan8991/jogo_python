import random
contVitoria1=0
contVitoria2=0

listaLetras=[]
dicInserir=[]
def main():
    rodada=0
    dic={}
    numLista=[]
    for i in range(20):
        numLista.append(-1)    
    for k in range(65,86):        
         if chr(k)!='K':
            dic.setdefault(chr(k),chr(k))
    print("\t\t\t \t JOGO DA MEMORIA")
    print("\t O JOGO TEM NUMERO DE 1 A 10. VOCE TEM ACHAR OS PARES DE UM 1 A 10.")
    gerarNum(numLista)
    cenario(dic,numLista,0,"","")
    controleJogo(rodada,dic,numLista)    
def gerarNum(numLista):    
    for i in range(20):
        valor=random.randint(1,10)                
        while numLista.count(valor)>=2:
                valor=random.randint(1,10)         
        numLista[i]=valor        
    return numLista     
def cenario(dic,numLista,JOGADOR,letra1,letra2):
    global listaLetras
    listaLetras.append(letra1)
    listaLetras.append(letra2) 
    cont=0   
    for key in dic:            
        if cont%4==0:
           print("\n")
        dic[key]=numLista[cont]
               
        if key in listaLetras:
            print("\t","[",dic[key],"]",end="")
        else:
            print("\t","[",key,"]",end="")
        
        cont+=1
    #print(dic)
    analisarResultadoJogo(JOGADOR,numLista,letra1,letra2,dic,dicInserir)             
    print("\n") 
def controleJogo(rodada,dic,numLista):
    global contVitoria1
    global contVitoria2
    tam=0    
    while tam!=len(dic):
        print(27*"\n")
        tam=len(dicInserir)
        if rodada%2==0:
            JOGADOR=1            
            print("\n\n\t\tJOGADOR 1\n")        
        if rodada%2==1:
            JOGADOR=2
            print("\n\n\t\tJOGADOR 2\n")
        letra1=input("ESCOLHA UMA LETRA ENTRE A ATE U\n").upper()       
        cenario(dic,numLista,JOGADOR,letra1,"")
        letra2=input("ESCOLHA UMA LETRA ENTRE A ATE U\n").upper()       
        cenario(dic,numLista,JOGADOR,letra1,letra2)
        rodada+=1
       # print(len(dicInserir))
        tam=len(dicInserir)
    if  contVitoria1>contVitoria2      :
        print("O JOGADOR1 FOI O VENCEDOR COM:",contVitoria1, "ACERTOS")
        print("O JOGADOR2 PERDEU TEVE:",contVitoria2, "ACERTOS")
    elif contVitoria1<contVitoria2:
        print("O JOGADOR2 FOI O VENCEDOR COM:",contVitoria2, "ACERTOS")
        print("O JOGADOR1 PERDEU TEVE:",contVitoria1, "ACERTOS")
    else:
        print("OS JOGADORES EMPATARAM TIVERAM:",contVitoria1,"ACERTOS")

def analisarResultadoJogo(JOGADOR,numLista,letra1,letra2,dic,dicInserir):
    global listaLetras
    global contVitoria1
    global contVitoria2
    if JOGADOR!=0:
       if letra2!="" and letra1!="" and listaLetras.count(letra1)==2:
           if dic.get(letra1)==dic.get(letra2):
               dicInserir.append(letra1)
               dicInserir.append(letra2)               
               print("\t\t\t\n\nVOCE ACERTOU JOGADOR "+str(JOGADOR))
              # print(dicInserir)
               if JOGADOR==1:
                    contVitoria1+=1
               else:
                    contVitoria2+=1
                
           else:
              while letra1 in listaLetras:
                  listaLetras.pop(listaLetras.index(letra1))
              while letra2 in listaLetras:


                  listaLetras.pop(listaLetras.index(letra2))
              print("\t\t\t\n\nVOCE ERROU JOGADOR "+str(JOGADOR))
              cenario(dic,numLista,0,"","")
              
main()