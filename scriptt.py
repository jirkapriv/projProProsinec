import random
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    # Copied from stack ovfw

shopOffersList = [
    [ 0, "Emerald armor", 1, 50],
    [ 1, "Sword of Doom", 1, 50],
    [ 2, "Redbull", 5, 10],
    [ 3, "Dulezite Informace", "mnoho", 100]
    ]

hapecka = ["❤️","❤️","❤️","❤️","❤️","❤️","❤️","❤️","❤️","❤️"]

def checkPrice(cena, yourbalnce):
    if cena > yourbalnce:
        print(bcolors.FAIL + "You are too poor :(" + bcolors.ENDC)
        return False
    if yourbalnce >= cena:
        print(bcolors.OKGREEN + "Succesfull buy :) " + bcolors.ENDC)
        return True

class Game():
    def __init__(self):
        self.infoBuy = False
    
    def rozcesti(self):
        print()
        print()
        print(f"You can go to {bcolors.OKCYAN}shop{bcolors.ENDC} if you want :) If so enter number - {bcolors.OKCYAN}1{bcolors.ENDC}")
        print(f"To print your {bcolors.OKCYAN}stats{bcolors.ENDC} enter - {bcolors.OKCYAN}2{bcolors.ENDC}")
        print(f"To get your {bcolors.OKCYAN}balance - 3{bcolors.ENDC}")
        print(bcolors.FAIL + f"To get out enter {bcolors.OKCYAN}- 4"+ bcolors.ENDC)
        if self.infoBuy:
            print(bcolors.OKBLUE+ "Special information: You now know there to find mining camp where you can mine some coin. To do soo you can press *"+ bcolors.ENDC)
            
        whereToGO = input("")

        if whereToGO == "1":
            game.Shop()
            return True
            
        if whereToGO == "2":
            player1.Vypiss()
            return True
            
        if whereToGO == "3":
            player1.Balancik()
            return True
            
        if whereToGO == "4":
            return False
            
        if whereToGO == "*" and self.infoBuy:
            game.MiningCamp()
            return True
    
    def Shop(self):
        print(bcolors.OKBLUE+"--------Shop--------"+bcolors.ENDC)
        print("Welcome to Shop, what do you wish for?")
        
        print(f"{bcolors.OKGREEN}Your balance is {player1.money} coins{bcolors.ENDC}")
        print("Our offers are: ")
        
        for index, offer in enumerate(shopOffersList):
            if self.infoBuy and index == len(shopOffersList) - 1:
                self.infoBuy = True
                break
            
            print(f"{index + 1}) {bcolors.OKBLUE}{offer[1]}{bcolors.ENDC}: {bcolors.OKGREEN}Price is {offer[3]}{bcolors.ENDC}")
            print(f"\t It adds {offer[2]} to your ", end="")
            
            if offer[0] == 0:
                print("armor")
            elif offer[0] == 1:
                print("attack")
            elif offer[0] == 2:
                print("stamina")

            if self.infoBuy:
                continue
        
            if offer[0] == 3:
                print("knowlidge and unlock mining camp")
        print("Do you want something? ")
        inputicek = input()
        if inputicek == "no":
            return
        try:
            inputicek = int(inputicek)
        except:
            print("Enter valid input....")
        if inputicek == 1:
            if checkPrice(shopOffersList[0][3], player1.money):
                player1.money -= shopOffersList[0][3]
                shopOffersList[0][3] += 15
                player1.hp += 1
                hapecka.append("❤️")

            print(f"Your balance is {player1.money} coins")
            
        if inputicek == 2:
            if checkPrice(shopOffersList[1][3], player1.money):
                player1.money -= shopOffersList[1][3]
                shopOffersList[1][3] += 15
                player1.attack += shopOffersList[1][2]

            print(f"Your balance is {player1.money} coins")

        if inputicek == 3:
            if checkPrice(shopOffersList[2][3], player1.money):
                player1.money -= shopOffersList[2][3]
                shopOffersList[2][3] += 15
                player1.stamina += shopOffersList[2][2]
                
            print(f"Your balance is {player1.money} coins")
            
        if inputicek == 4 and self.infoBuy == False:
            if checkPrice(shopOffersList[3][3], player1.money):
                player1.money -= shopOffersList[3][3]
                self.infoBuy = True
                print("Now you have special ability to acces special information.... ")
                
            else:
                print(offer[3], player1.money)
            print(f"Your balance is {player1.money} coins")
            
        if inputicek == "ex":
            return
    
    def MiningCamp(self):
        if self.infoBuy == True:
            print(bcolors.OKBLUE+"You are in mining Camp" + bcolors.ENDC)
            while True:
                print("Press 1 to dig to some place")
                print("if you ant to escape enter 2")
                i = input()
                try:
                    i = int(i)
                except:
                    print("Enter valid input....")
                if i == 1:
                    ranCislo = random.randint(1,5)
                    if ranCislo == 4:
                        print("You mined the right way :)")
                        player1.money += 5
                    else :
                        print("You mined the wrong way :(")   
                if i == 2:
                    break
        else:
            print("Your not allowed")

class Player():
    def __init__(self, name, hp, attack, stamina, money=100, infoBuy=False, fightsWon=0):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.stamina = stamina
        self.money = money
        self.infoBuy = infoBuy
        self.fightsWon = fightsWon

    def Vypiss(self):
        
        print(f"Name - {self.name},\nAttack: {self.attack},\nStamina: {self.stamina},")
        print(bcolors.OKGREEN + "HP:" + bcolors.ENDC, end="")
        for x in hapecka:
            print(x, end=" ")
   
    def Balancik(self):
        print(f" {bcolors.OKGREEN}currently you have { self.money} coins {bcolors.ENDC}")

class Enemy():
    def __init__(self, name, hp, attack, stamina):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.stamina = stamina

    def Vypiss(self):
        print(f"Name = {self.name}, HP: {self.hp}, Attack: {self.attack}, Durab: {self.stamina}")

    def fight(self):
        
        print(bcolors.OKBLUE+"Boss aproched you if you want to run press 0 if you want to fight press 1"+bcolors.ENDC)
        c = input()

        if c == "0":
            print(bcolors.FAIL +"While you were running you tripped and broke your neck.... :( ")
            print("Game Over" + bcolors.FAIL)
            sys.exit()
        if c == "1":
            print(bcolors.OKCYAN + "You chose to fight... Very well... ")
            print("Do you even have a chance we will see")
            print(f"Your enemy is {self.name}" + bcolors.ENDC)
            self.Vypiss()
            
            while player1.stamina > 0:
                print("Attack - press 1")
                inputikAtt = input()
                if inputikAtt == "1":
                    self.hp -= player1.attack
                    player1.hp -= self.attack
                    for x in range(self.attack):
                        hapecka.pop()
                    if self.hp < 0:
                        self.hp = 0
                    print(f"{bcolors.FAIL}Enemy HP: {self.hp}{bcolors.ENDC}")
                    print(bcolors.OKGREEN+"Your HP: " + bcolors.ENDC, end="")
                    for x in hapecka:
                        print(x, end="  ")
                player1.stamina -= 1
                print()
                print(f"Your stamina: {player1.stamina}")
                if self.hp <= 0:
                    print(bcolors.OKGREEN + "You won!!!")
                    player1.money += 50
                    player1.fightsWon += 1
                    print("You gained 50 coins"+ bcolors.OKGREEN)
                    return
            if self.hp >= 0:
                print(bcolors.FAIL + "You lost" + bcolors.ENDC)
                sys.exit()

print("""\
 __      __       .__  .__                                  __             __  .__                                           
/  \    /  \ ____ |  | |  |   ____  ____   _____   ____   _/  |_  ____   _/  |_|  |__   ____      _________    _____   ____  
\   \/\/   // __ \|  | |  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \  \   __\  |  \_/ __ \    / ___\__  \  /     \_/ __ \ 
 \        /\  ___/|  |_|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )  |  | |   Y  \  ___/   / /_/  > __ \|  Y Y  \  ___/ 
  \__/\  /  \___  >____/____/\___  >____/|__|_|  /\___  >  |__|  \____/   |__| |___|  /\___  >  \___  (____  /__|_|  /\___  >
       \/       \/               \/            \/     \/                            \/     \/  /_____/     \/      \/     \/ 

                    """)

inpuJmeno = input(bcolors.BOLD + bcolors.OKBLUE+ "What is your name? " + bcolors.ENDC)
print(f"Hi {inpuJmeno}")

"""                                         GAME INIT                                         """

enemy1 = Enemy("Charizard", 5, 1, 5)
enemy2 = Enemy("Blastoise", 10, 2, 6)
enemy3 = Enemy("Vepinbell", 50, 3, 7)
player1 = Player(inpuJmeno, len(hapecka) + 1, 2, 5, 100, False, 0)
game = Game()
run = True

"""                                         GAME INIT                                         """

while run:
    while game.rozcesti() == True:
        if game.rozcesti() == False:
            break
        game.rozcesti()
    if player1.fightsWon == 0:
        enemy1.fight()
    game.rozcesti()
    if player1.fightsWon == 1:
        enemy2.fight()
    game.rozcesti()
    if player1.fightsWon == 2:
        enemy3.fight()
    print(f"{bcolors.OKGREEN}You won the game {player1.name}. Congrats!!!!!!{bcolors.ENDC}")
