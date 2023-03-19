print()
print()

print("---------------------------------------------------------WELCOME TO THE GAME CASINO-------------------------------------------------------------")

import winsound

filename = 'speech'
winsound.PlaySound(filename, winsound.SND_FILENAME)

filename = 'game'
winsound.PlaySound(filename, winsound.SND_FILENAME)

print()

#Login form
nam_value=input("Enter your name = ")
pass_value=input("Enter your password = ")
age_value=int(input("Enter your age = "))
acc_bal=1000
print("Enter amount for account =",acc_bal)

print()

w1=1
while w1>0 :
    if age_value>=18:
        print("Your are Eligible for this game ")
        break
    else:
        age_value=int(input("Re-Enter your age = "))
        if age_value<18:
            w1=5
        else:
            w1=-5
            break

        
#Random Value
        print()
import random
while acc_bal>200:
    rdn_value=random.randint(0,10)
    usr_entrd_value=int(input("Enter a random value b/w 0 to 10 = "))
    bet=float(input("Enter amt for bet = "))
    
    con_bet=1
    while con_bet>0 :
        if bet>0 and bet<=acc_bal:
            break
        else:
            bet=int(input("Re-Enter your bet amt = "))
            if bet<=0:
                con_bet=5
            else:
                con_bet=-5
                break



    
    
    if usr_entrd_value>=0 and usr_entrd_value<=10:
            if rdn_value==usr_entrd_value:
                print()
                print("You win")
                acc_bal+=bet
                print("Your Account Balance",acc_bal)
                print("Correct value is =", rdn_value)
                print()
                Exit=input("If you want to exit please type 'Y' else type anything = ")
                if Exit=='y' or Exit=='Y':
                    exit()
                else:
                    print()
                    continue
            else:
                print()
                print("Sorry you Loose!")
                acc_bal-=bet
                print("Your Account Balance",acc_bal)
                print("Correct value is =", rdn_value)
                print()
                Exit=input("If you want to exit please type 'Y' else type anything = ")
                if Exit=='y' or Exit=='Y':
                    exit()
                else:
                    print()
                    continue


            
    else:
        usr_entrd_value=int(input("Re-Enter a random value b/w 0 to 10 = "))
        if usr_entrd_value>=0 and usr_entrd_value<=10:
            print()
            print("Entered",usr_entrd_value)
            if rdn_value==usr_entrd_value:
                print("You win")
                acc_bal+=bet
                print("Your Account Balance",acc_bal)
                print()
                Exit=input("If you want to exit please type 'Y' else type anything = ")
                if Exit=='y' or Exit=='Y':
                    exit()
                else:
                    print()
                    continue
            else:
                print()
                print("Sorry you Loose!")
                acc_bal-=bet
                print("Your Account Balance",acc_bal)
                print("Correct value is =", rdn_value)
                print()
                Exit=input("If you want to exit please type 'Y' else type anything = ")
                if Exit=='y' or Exit=='Y':
                    exit()
                else:
                    print()
                    continue
                w2=5
        else:
            print()
            print("Wrongly Entered Value")
            print("Correct value is =", rdn_value)
            w2=-5
            break

#Loan  
else:
    print()
    print("                                                                  -:LOAN:-                                                                                             ")

    print("                                                 Now you are going to opt for Loan                                                                       ")


print()

print("                                                     There are 3 categories  for loan                                                                           ")
print("                                    1. Platinum with an amount 520 and interest 11%                                                                 ")
print("                                    2. Gold with an amount 400 and interest 9%                                                                         ")
print("                                    3. Silver with an amount 250 and interest 4%                                                                        ")

print()

choice=int(input("Enter the number for these categories b/w 1 to 3 = "))
if choice==1:
    print("You have opted for 'PLATINUM' loan")
    acc_bal+=520
elif choice==2:
    print("You have opted for 'GOLD' loan")
    acc_bal+=400
else:
    print("You have opted for 'SILVER' loan")
    acc_bal+=250

print()

print("                                    You are only having  3 chances Left, get the more out of it                                                       ")

print()

chance=0
while chance<3:
    rdn_value=random.randint(0,10)
    usr_entrd_value=int(input("Enter a random value b/w 0 to 10 = "))
    bet=float(input("Enter amt for bet = "))
    con_bet=1
    while con_bet>0 :
              if bet>0:
                  break
              else:
                    bet=int(input("Re-Enter your bet amt = "))
                    if bet<=0:
                        con_bet=5
                    else:
                            con_bet=-5
                            break
    if rdn_value==usr_entrd_value:
                print()
                print("You win")
                acc_bal+=bet
                print("Your Account Balance",acc_bal)
                print("Correct value is =", rdn_value)
                print()
                chance+=1
    else:
                print()
                print("Sorry you Loose!")
                acc_bal-=bet
                print("Your Account Balance",acc_bal)
                print("Correct value is =", rdn_value)
                print()
                chance+=1

#Final Result                
if choice==1:
    r=(520*11*1)/100
    result=acc_bal-r
    print("Your current acount balance = ",acc_bal)
    print("Your current acount balance after the compensation of loan for 11% = ",result)

elif choice==2:
      r=(400*9*1)/100
      result=acc_bal-r
      print("Your current acount balance = ",acc_bal)
      print("Your current acount balance after the compensation of loan for 9% = ",result)
else:
     r=(250*4*1)/100
     result=acc_bal-r
     print("Your current acount balance = ",acc_bal)
     print("Your current acount balance after the compensation of loan for 4% = ",result)






















