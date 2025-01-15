# 5 dados - 1 a 6

# jogar os dados
# ai comparar

# 20p S (sequência de 1 a 5 ou sequência de 2 a 6)
# 30p F 3 dados IGUAIS + 2 dados IGUAIS
# 40p P 4 dados IGUAIS
# 50p G 5 dados IGUAIS

import random

dados = []
sortearNovo = []
sortearNovo_2 = []
n = 5
tentativas = ["",""]





# sorteando os NÚMEROS
def sortear():
  print()
  dados.clear()
  for i in range(n):
    d = random.randrange(1,7)
    dados.append(d)
    dados.sort()

  print()
  for dado in dados:
    print(f"🎲 = {dado}\n ")
  print()

##########################################################

def escolha():
  
  while True:  
    if len(tentativas) == 0:
      #resultado()
      break
    else:  
     print(f"TENTATIVAS RESTANTES {len(tentativas)} \n")
     resultado() 
     y = input("DESEJA SORTEAR ALGUM NÚMERO (S para continuar) ? ").upper()
     if y != "S":
       break
     elif y == "S":
        while True:   
            w = int(input("QUAL NÚMERO DEJESA SORTEAR NOVAMENTE (0 para SORTEAR e PARAR) ?"))
            if w in dados :
                dados.remove(w)
                sortearNovo.append(w)

            elif w == 0 : 
                tentativas.pop()
                sortearDadosEspecificos()
                resultado()
                break
              
 
##########################################################

def sortearDadosEspecificos():

  n = len(sortearNovo)
  #print(f"quantidade de itens dentro da lista sortearNovo == {n}")
  for i in range(n):
    sortearNovo.clear()
    d = random.randrange(1,7)
    dados.append(d)
    dados.sort()

  print()
  for dado in dados:
    print(f"🎲 = {dado}\n ")
  print(tentativas)
  #sortearNovo.clear()
  escolha()
##########################################################

def resultado():
 d1 = dados[0]
 d2 = dados[1]
 d3 = dados[2]
 d4 = dados[3]
 d5 = dados[4]


 if d1 == d5:
  print("🪖💥 GENERAL 💥🪖\n")
 
 elif d1 == d3 and d4 == d5:
  print("🎉 FULLAN 🎉\n")
 
 elif d1 == d2 and d3 == d5:
  print("🎉 FULLAN 🎉\n")
 
 elif d1 == d4 or d2 == d5:
  print("🂡 POKER 🂡\n")
 
 elif d1 == 1 and d2 == 2 and d3 == 3 and d4 == 4 and d5 == 5:
  print("🔢 SEQUÊNCIA 🔢\n")

 elif d1 == 2 and d2 == 3 and d3 == 4 and d4 == 5 and d5 == 6:
  print("🔢 SEQUÊNCIA 🔢\n")

 else:
  print("😔 SEUS DADOS NÃO DERAM EM NADA 😔\n") 




##########################################################


while True:  
    print("\n")
    print("-"*31)
    print("BEM VINDO AO JOGO DO GENERAL 🪖")
    print("-"*31)

    print("1 - JOGAR")
    print("2 - SAIR\n")
    a = input("ESCOLHA SUA OPÇÃO: ")

    if a == "1":
     tentativas = ["",""] 
     print()
     sortear()
     escolha()

    else:
      break


  



