import random



shopOffersList = [
    [ 0, "Emerald armor", 45, 50],
    [ 1, "Sword of Doom", 60, 50],
    [ 2, "Redbull", 5, 10],
    [ 3, "Dulezite Informace", "mnoho", 100]
    ]

def checkPrice(cena, yourbalnce):
    if cena > yourbalnce:
        print("You are too poor :(")
        return False
    if yourbalnce >= cena:
        print("Succesfull buy :) ")
        return True
    
class Player():
    def __init__(self, name, hp, attack, stamina, money=100, infoBuy=False):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.stamina = stamina
        self.money = money
        self.infoBuy = infoBuy
        
    def MiningCamp(self):
        if self.infoBuy == True:
            print("You are in mining Camp")
            while True:
                print("Press 1 to dig to some place")
                print("if you ant to escape enter 2")
                i = input()
                i = int(i)
                if i == 1:
                    ranCislo = random.randint(1,5)
                    if ranCislo == 4:
                        print("You mined the right way :)")
                        self.money += 20
                    else :
                        print("You mined the wrong way :(")   
                if i == 2:
                    break
        else:
            print("Your not allowed")
            
    def Vypiss(self):
        print(f"Name = {self.name}, HP: {self.hp}, Attack: {self.attack}, Durab: {self.stamina}")
        
    def Balacik(self):
        print(f"currently you have { self.money} coins")
        
    def Shop(self):
        print("--------Shop--------")
        print("Welcome to Shop what do you wish for?")
        
        print(f"Your balance is {self.money} coins")
        
        print("Our offers are: ")
        for x in shopOffersList:
            print(f"{x[0] + 1}) {x[1]}: Price is {x[3]}")       
            print(f"\t It adds {x[2]} to your ", end="" )
            if x[0] == 0:
                print("armor")
            if x[0] == 1:
                print("attack")
            if x[0] == 2: 
                print("stamina")
            if x[0] == 3:
                print("knowlidge")
        print("Do you want something? ")
        inputicek = input()
        inputicek = int(inputicek)
        
        if inputicek == 1:
            if checkPrice(shopOffersList[0][3], player1.money):
                player1.money -= shopOffersList[0][3]
                player1.hp += shopOffersList[0][2]

            print(f"Your balance is {self.money} coins")
            
        if inputicek == 2:
            if checkPrice(shopOffersList[1][3], player1.money):
                player1.money -= shopOffersList[1][3]
                player1.attack += shopOffersList[1][2]
                
            print(f"Your balance is {self.money} coins")

        if inputicek == 3:
            if checkPrice(shopOffersList[2][3], player1.money):
                player1.money -= shopOffersList[2][3]
                player1.attack += shopOffersList[2][2]
                
            print(f"Your balance is {self.money} coins")
            
        if inputicek == 4:
            if checkPrice(shopOffersList[3][3], player1.money):
                player1.money -= shopOffersList[3][3]
                self.infoBuy = True
                print("Now you have special ability to acces special information.... ")
                
            else:
                print(x[3], player1.money)
            print(f"Your balance is {self.money} coins")
            
            
                    
class Enemy():
    def __init__(self, name, hp, attack, stamina):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.stamina = stamina

    def Vypiss(self):
        print(f"Name = {self.name}, HP: {self.hp}, Attack: {self.attack}, Durab: {self.stamina}")

    
    
enemy1 = Enemy("Charizard", 100, 20, 5)
enemy2 = Enemy("Blastoise", 250, 25, 6)
enemy3 = Enemy("Vepinbell", 1000, 30, 7)



inpuJmeno = input("What is your name? ")

player1 = Player(inpuJmeno, 100, 20, 5, 100, False)

while True:

    print("You can go to shop if you want :) If so enter number 1")
    print("To print your stats eneter 2")
    print("To get your balance 3")
    print("To get out enter 4")
    if player1.infoBuy:
        print("Special information: You now know there to find mining camp where you can mine some coin. To do soo you can press *")


    whereToGO = input("")



    if whereToGO == "1":
        player1.Shop()
    if whereToGO == "2":
        player1.Vypiss()
    if whereToGO == "3":
        player1.Balacik()
        
    if whereToGO == "4":
        break
        
    if whereToGO == "*" and player1.infoBuy:
        player1.MiningCamp()
        
        


print("First boss aproched you if you want to run press 0 if you want to fight press 1")
c = input()


if c == "0":
    print("While you were running you tripped and broke your neck.... :( ")
    print("Game Over")
if c == "1":
    print("You chose to fight... Very well... ")
    print("Do you even have a chance we will see")
    print(f"Your first enemy is {enemy1.name}")
    enemy1.Vypiss()
    
    print("You attack first - press 1")
    
    
    
    if player1.stamina > 0:
        
        inputikAtt = input()
        if inputikAtt == 1:
            enemy1.hp -= player1.attack
        player1.stamina -= 1
    
    
    
    
    
    
