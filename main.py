import sys,time
import random
from colorama import Fore




RPS = ["R","P","S"]
RPS1 =["R","P","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S","S"]
RPS2 = ["R","S","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P","P"]
RPS3 = ["P","S","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R","R"]



def sprint(str):
    for c in str + '\n':
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(6./110)
y = (sprint(Fore.LIGHTYELLOW_EX + 'Hello my name is RPSbot whats your name? '))
i = input("--> ")
print("                                                    ")
sprint(Fore.LIGHTYELLOW_EX + "Here are the basic rules of RPS, Rock beats scissors and scissorsbeates paper and paper beats rock and if you choses the same thi-ng its a tie!!!")
print("                                                    ")
(sprint(Fore.LIGHTGREEN_EX + "Hello " +  i  + " your in the world of Rock, paper, scissors now lets begin."))
print("                                                    ")
sprint("Now "+ i + " what mode would you like;E(easy) - N(normal) - H(Hard)")
print("                                                    ")
PL = input("--> ")
print("                                                    ")







  
def N(): 
  X = True
  while (X == True):
    print("                                                    ")
    sprint("Pick (R)Rock (P)Paper (S)Scizzors")
    print("                                                    ")
    sprint("Now " + i + " please enter you option")
    ba = input("--> ")
    print("                                                    ")
    sprint("Now RPSbot please enter you option")
    print("                                                    ")
    sprint(". . . . . . . . . . . .")

    dk = random.choice(RPS)

    if (dk == "R" and ba == "P"):
      print("                                                    ")
      sprint('Congrats you won that one ' + i)
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        X = True
      elif(PA == "S"):
        X = False

    if (dk == "S" and ba == "R"):
      print("                                                    ")
      sprint('Congrats you won that one ' + i)
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        X = True
      elif(PA == "S"):
        X = False

    if (dk == "R" and ba == "S"):
      print("                                                    ")
      sprint('Rps bot wins')
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        X = True
      elif(PA == "S"):
        X = False
    if (dk == "P" and ba == "R"):
      print("                                                    ")
      sprint('Rps bot wins')
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        X = True
      elif(PA == "S"):
        X = False
    if (dk == "P" and ba == "S"):
      print("                                                    ")
      sprint('Congrats you won that one ' + i)
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        X = True
      elif(PA == "S"):
        X = False

    if (dk == "S" and ba == "P"):
      print("                                                    ")
      sprint('Rps bot wins')
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        X = True
      elif(PA == "S"):
        X = False
  
    if (ba == dk):
      print("                                                    ")
      sprint("The resunts are in and it is a Tie!!!!!!!!")
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        X = True
      elif(PA == "S"):
        X = False



def E(): 
  Z = True
  while (Z == True):
    print("                                                    ")
    sprint("Pick (R)Rock (P)Paper (S)Scizzors")
    print("                                                    ")
    sprint("Now " + i + " please enter you option")
    PS = input("--> ")
    print("                                                    ")
    sprint("Now RPSbot please enter you option")
    print("                                                    ")
    sprint(". . . . . . . . . . . .")

    
    if PS == "R":
      MK1 = random.choice(RPS1)

    if PS == "S":
      MK2 = random.choice(RPS2) 
      
    if PS == "P":
      MK3 = random.choice(RPS3)

    if (PS == "R" and MK1 == "P"):
      print("                                                    ")
      sprint('Rps bot wins') 
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Z = True
      elif(PA == "S"):
        Z = False
    
    if (PS == "R" and MK1 == "R"):
      print("                                                    ")
      sprint("The resunts are in and it is a Tie!!!!!!!!")
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Z = True
      elif(PA == "S"):
        Z = False
    if (PS == "R" and MK1 == "S"):
      print("                                                    ")
      sprint('Congrats you won that one ' + i)
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Z = True
      elif(PA == "S"):
        Z = False
     
        
      
    if (PS == "P" and MK3 == "P"):
      print("                                                    ")
      sprint("The resunts are in and it is a Tie!!!!!!!!")
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Z = True
      elif(PA == "S"):
        Z = False
    
    if (PS == "P" and MK3 == "R"):
      print("                                                    ")
      sprint('Congrats you won that one ' + i)
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Z = True
      elif(PA == "S"):
        Z = False
    if (PS == "P" and MK3 == "S"):
      print("                                                    ")
      sprint('Rps bot wins')
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Z = True
      elif(PA == "S"):
        Z = False
    if (PS == "S" and MK2 == "P"):
      print("                                                    ")
      sprint('Congrats you won that one ' + i)
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Z = True
      elif(PA == "S"):
        Z = False
          
    
    if (PS == "S" and MK2 == "R"):
      print("                                                    ")
      sprint('Rps bot wins')
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Z = True
      elif(PA == "S"):
        Z = False
    if (PS == "S" and MK2 == "S"):
      print("                                                    ")
      sprint("The resunts are in and it is a Tie!!!!!!!!")
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Z = True
      elif(PA == "S"):
        Z = False











  
def H():
  Y = True
  while (Y == True):
    print("                                                    ")
    sprint("Pick (R)Rock (P)Paper (S)Scizzors")
    print("                                                    ")
    sprint("Now " + i + " please enter you option")
    PS = input("--> ")
    print("                                                    ")
    sprint("Now RPSbot please enter you option")
    print("                                                    ")
    sprint(". . . . . . . . . . . .")

    
    if PS == "P":
      MK1 = random.choice(RPS1)

    if PS == "R":
      MK2 = random.choice(RPS2) 
      
    if PS == "S":
      MK3 = random.choice(RPS3)

    if (PS == "R" and MK2 == "P"):
      print("                                                    ")
      sprint('Rps bot wins')
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Y = True
      elif(PA == "S"):
        Y = False
    
    if (PS == "R" and MK2 == "R"):
      print("                                                    ")
      sprint("The resunts are in and it is a Tie!!!!!!!!")
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Y = True
      elif(PA == "S"):
        Y = False
    if (PS == "R" and MK2 == "S"):
      print("                                                    ")
      sprint('Congrats you won that one ' + i)
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Y = True
      elif(PA == "S"):
        Y = False
      
    if (PS == "P" and MK1 == "P"):
      print("                                                    ")
      sprint("The resunts are in and it is a Tie!!!!!!!!")
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Y = True
      elif(PA == "S"):
        Y = False
    
    if (PS == "P" and MK1 == "R"):
      print("                                                    ")
      sprint('Congrats you won that one ' + i)
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Y = True
      elif(PA == "S"):
        Y = False
    if (PS == "P" and MK1 == "S"):
      print("                                                    ")
      sprint('Rps bot wins') 
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Y = True
      elif(PA == "S"):
        Y = False
    if (PS == "S" and MK3 == "P"):
      print("                                                    ")
      sprint('Congrats you won that one ' + i)
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Y = True
      elif(PA == "S"):
        Y = False
          
    
    if (PS == "S" and MK3 == "R"):
      print("                                                    ")
      sprint('Rps bot wins')
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Y = True
      elif(PA == "S"):
        Y = False
    if (PS == "S" and MK3 == "S"):
      print("                                                    ")
      sprint("The resunts are in and it is a Tie!!!!!!!!")
      print("                                                    ")
      sprint("Try again? Type (Any number/letter Exept S) to proceed and (S) tostop the game.")
      print("                                                    ")
      PA = input("--> ")
      if (PA == "P"):
        Y = True
      elif(PA == "S"):
        Y = False




if (PL == "N"):
  N()
  
if (PL == "E"):
  E()
  
if (PL == "H"):
  H()









