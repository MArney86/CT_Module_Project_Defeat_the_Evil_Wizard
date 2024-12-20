from random import randint

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self._health = health
        self.__attack_power = attack_power
        self.__max_health = health
        self.__attack_name = "Basic Attack" #name of character's basic attack
        self.__abilities = {"evasion" : "Evasion", #characters' evasion special skill
                           "attack" : "Special Attack"} #characters' special attack
        self.__evasion = False #flag for evasion skill

    def attack(self, opponent):
        opponent.damage(self.calculate_attack_damage(), self.__attack_name, self)
        
    def heal(self):
        if self._health + 20 < self.max_health:
            self._health += 20
        else:
            self._health = self.__max_health

    def damage(self, hit_damage, attack_name, opponent):
        if self.__evasion:
            print(f"\n{opponent.name} attacked {self.name} with {attack_name}. {self.name} evaded the attack using their {self.__abilities["evasion"]} ability!")
            self.display_stats()
            self.__evasion = False
        else:
            self._health = self._health - hit_damage
            print(f"{self.name} was hit by {attack_name} for {hit_damage} damage.")
            self.display_stats()

    def evade_attack(self):
        self._evasion = True
        print(f"\n{self.name} has used their {self.__abilities["evasion"]} ability")

    def special_attack(self, opponent):
        print(f"\n{self.name} has used {self.__abilities["attack"]}!!!")
        opponent.damage(self.__attack_power + randint(10, 20), self.__abilities["attack"][0], self)

    def use_abilities(self, opponent):
        while True:
            print("\n--- Special Abilities ---")
            print(f"1. Evade the next attack with your {self.__abilities["evasion"]} ability")
            print(f"2. Use your {self.__abilities{"attack"}} special attack")
            choice = input("Please input the number of your choice")
            if choice == "1":
                self.evade_attack()
                break
            elif choice == "2":
                self.special_attack(opponent)
                break
            else:
                print("That was an incorrect choice. Please try again")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self._health}/{self.__max_health}, Attack Power: {self.__attack_power}")

    def calculate_attack_damage(self):
        return randint(self.__attack_power - self.__attack_power // 5 , self.__attack_power + self.__attack_power // 5)

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        #flags for special abilities
        self._attack_name = "Sword Thrust"
        self.__abilities = {"evasion" : "Parry",
                           "attack" : "Legendary Sword"}

    def special_attack(self, opponent):
        print(f"The Warrior {self.name} has used {self.__abilities["attack"]}!!!")
        opponent.damage(self.__attack_power + randint(10, 25), self.__abilities["attack"][0], self)
        
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        #flags for special abilities
        self.__abilities = {"evasion" : "Barrier",
                           "attack" : "Fireball"}
        
    #class specific attack
    def special_attack(self, opponent):
        print(f"The Mage {self.name} has cast {self.__abilities["attack"]}!!!")
        opponent.damage(self.__attack_power + randint(10, 20), self.__abilities["attack"][0], self)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)
        self._attack_name = "Evil Magic"

    def regenerate(self):
        self.__health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)
        #special abilities
        self.__abilities = {"evasion": "Evade",
                            "attack": "Quick Shot"}
    
    #class specific attack
    def special_attack(self, opponent):
        print(f"The Archer {self.name} has used their Quick Shot ability!!!")
        opponent.damage(self.calculate_attack_damage(), self.__abilities["attack"][0], self)
        opponent.damage(self.calculate_attack_damage(), self.__abilities["attack"][0], self)

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        #flags for special abilities
        self._attack_name = "Holy Magic"
        self.__abilities = {"evasion": "Divine Shield",
                            "attack": "Holy Strike"}
        
    #class specific attack
    def special_attack(self, opponent):
        print(f"The Paladin {self.name} has cast {self.__abilities["attack"]}!!!")
        opponent.damage(self.__attack_power + randint(10, 20), self.__abilities["attack"][0], self)
