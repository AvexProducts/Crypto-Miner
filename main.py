companies = []
money = 0
import os
import time
import colorama
from colorama import Fore
cryptomined = 0
cryptobasicminerpower = 1
cryptobasic = "Crypto Basic Miner"
cryptoadvancedminerpower = 2
cryptoadvanced = "Crypto Advanced Miner"
cryptolegendaryminerpower = 3
cryptolegendary = "Crypto Legendary Miner"
cryptominers = []
print(Fore.RED + '''
        /-------------------\
       /    CRYPTO CRYPTO    \
       | CRYPTO CYPTO CRYPTO | $$$$ $$$$$$$$$$$$$$$$$$$$$$$$$
       | MINER MINER MINER   | $  $  $  $$$$$$$$$ $$$$$$$$$$$$$
       |_____________________|

                                    ''')
print("Made by Arthur Keller [VERSION 1.5]!!!")
cryptominers = ["Crypto Basic Miner"]
companies = []
print(Fore.RED + "WELCOME TO CRYPTO MINER!!!! Type 'start' to start!")
enter = input("Enter :")
if enter == "start":
    while True:
        os.system('clear')
        print(Fore.RED)
        print("YOUR MINED CRYPTO: ",cryptomined)
        print("YOUR MONEY $$$: ",money)
        print("YOUR MINERS: ",cryptominers)
        print("YOUR COMPANIES: ",companies)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("ORDER OF GETTING THINGS: ADVANCED CRYPTO MINER, LEGENDARY CRYPTO MINER, COMANY")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("You can buy a 'advanced crypto miner' for 501 crypto just type 'advanced crypto miner' and a 'legendary crypto miner' for 1001 crypto just type 'legendary'. You can also sell your crypto for money, which you can flex on your friends! Just type 'money'! PLEASE GET A ADVANCED, THEN LEGENDARY CRYPTO MINER OR THE GAME WILL CRASH.")
        print("There are also companies that you can but with money! Type 'company' to take the first crypto company! The price is $10001!!!")
        print("Click 'ENTER' to start mining!")
        crypto = input("PRESS ENTER: ")
        if crypto == "advanced crypto miner":
            if cryptomined > 500:
                print("BOUGHT!")
                cryptominers.remove('Crypto Basic Miner')
                cryptominers.append('Crypto Advanced Miner')
                cryptomined = cryptomined - 501
                time.sleep(0.1)     
                os.system('clear')
                continue
            else:
                print("NOT ENOUGH CRYPTO")
                time.sleep(4)
                os.system('clear')
                continue
        elif crypto == "legendary":
            if cryptomined > 1000:
                print("BOUGHT!")
                cryptominers.remove('Crypto Advanced Miner')
                cryptominers.append('Crypto Legendary Miner')
                cryptomined = cryptomined - 1001
                time.sleep(0.1)
                os.system('clear')
                continue
            else:
                print("NOT ENOUGH CRYPTO")
                time.sleep(4)
                os.system('clear')
                continue
        elif crypto == "money":
            print("TRANSFERRED")
            money = money + cryptomined
            cryptomined = cryptomined - cryptomined
            time.sleep(2)
            continue
        elif crypto == "company":
            if money < 10000:
                print("Not enough money.")
                time.sleep(2)
                continue
            else:
                print("BOUGHT!")
                cryptomined = cryptomined - 10001
                companies.append("Company Basic")
                cryptominers.remove("Crypto Legendary Miner")
                time.sleep(2)
                continue
        elif "Crypto Basic Miner" in cryptominers:
            cryptomined = cryptomined + 1
            time.sleep(0.2)
            os.system('clear')
            continue
        elif "Crypto Advanced Miner" in cryptominers:
            cryptomined = cryptomined + 2
            time.sleep(0.1)
            os.system('clear')
            continue
        elif "Crypto Legendary Miner" in cryptominers:
            cryptomined = cryptomined + 3
            time.sleep(0)
            os.system('clear')
            continue
        elif "Company Basic" in companies:
            cryptomined = cryptomined + 10
            time.sleep(0)
            os.system('clear')
            continue
        
            

        else:
            print("ERM, what the SIGMA?")
