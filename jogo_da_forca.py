import random



def main():
    
    print(25* "\n")
    global cont
    cont=0
    palavra,dica=gerarPalavra();
    print("                 DICA:",dica.upper(),"\n\n\n")
    print(cenarioForca(cont))
    controlarJogo(palavra,dica)
   

def gerarPalavra():
    lista_palavra=["vasco","barco","ventilador","acre","feijoada","espanha","golfinho","girassol"]
    lista_dica=["time","transporte","eletrodomestico","estado brasileiro","comida","pais","animal marinho","planta"]
    num_aleatorio=random.randint(0,len(lista_palavra)-1)
    return lista_palavra[num_aleatorio],lista_dica[num_aleatorio]

def cenarioForca(cont1):
    lista_cenario=(
         "+---+\n|\n|\n|\n|\n",
         "+---+\n|   O\n|\n|\n|\n|",
         "+---+\n|   O\n|   |\n|   |\n|\n|",
         "+---+\n|   O\n|  /|\n|   |\n|\n|",
         "+---+\n|   O\n|  /|\\\n|   |\n|\n|",
         "+---+\n|   O\n|  /|\\\n|   |\n|  /\n|",
         "+---+\n|   O\n|  /|\\\n|   |\n|  / \\\n|",
         

)
    if cont1==0:
     return lista_cenario[cont1]
    if cont1==1:
     return lista_cenario[cont1]
    if cont1==2:
     return lista_cenario[cont1]
    if cont1==3:
     return lista_cenario[cont1]
    if cont1==4:
     return lista_cenario[cont1]
    if cont1==5:
     return lista_cenario[cont1]
    if cont1==6:
     return lista_cenario[cont1]
    
                          

def controlarJogo(palavra,dica):
   palavra=palavra.upper()
   dica=dica.upper()
   global cont
   fim=0
   achei=False
   palavra_lista=[]
   letra_lista=[]
   for j in range(len(palavra)):
       print(" __ ",end=' ')
       palavra_lista.append(" __ ")
       
     
   while fim<6:
       
      
       letra=str(input("\n\n  digite2 letra do alfabeto:\n").upper())       
       print(22* "\n")
       letra_lista.append(letra)
       print("          DICA:",dica.upper(),"\n")
       print("          letras: "+"-".join(letra_lista),"\n""\n")
       for i in range(len(palavra)):
         
         if palavra[i]==letra:
           palavra_lista[i]=letra
           achei=True
           

       if achei:
            achei=False
       else:
          cont+=1
          fim+=1      
       
       print(cenarioForca(cont))      
       print(" ".join(palavra_lista))
       if "".join(palavra_lista)==palavra:
            print("        \n\nVOCE GANHOU.PARABENS!!!")
            novoJogo()
            break
       if fim==6:
            print("\n\n\n\t\tA PALAVRA ERA :",palavra)
            print("\t\t\tGAME OVER")
            novoJogo()

   
  
def novoJogo():
    global cont
    cont=0
    novaPartida=int(input("\n\n"+"DESEJA CONTINUAR.\n CASO DESEJA CONTINUAR DIGITE 1.\n DIGITE QUALQUER NUMERO DIFERENTE DE 1 SE VOCE NAO QUISER CONTINUAR A JOGAR.\n"))
    if (novaPartida==1):
              main()
          
           
main()
