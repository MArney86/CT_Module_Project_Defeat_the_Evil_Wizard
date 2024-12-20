from random import randint

# Base Character class
class Character:
    def __init__(self, name, health, attack_power, attack_name, evasion, sp_attack):
        self.name = name
        self.health = health
        self.__attack_power = attack_power
        self._max_health = health
        self._attack_name = attack_name #name of character's basic attack
        self._abilities = {"evasion" : evasion, #characters' evasion special skill
                           "attack" : sp_attack} #characters' special attack
        self.__evasion = False #flag for evasion skill

    def attack(self, opponent):
        opponent.damage(self.calculate_attack_damage(), self._attack_name, self)
        
    def heal(self):
        if self.health + 20 < self._max_health:
            self.health += 20
        else:
            self.health = self._max_health

        print(f"\n{self.name} healed themself. Current health: {self.health}")

    #making taking damage part of the character itself to help implement evasion
    def damage(self, hit_damage, attack_name, opponent):
        if self.__evasion:
            print(f"\n{opponent.name} attacked {self.name} with {attack_name}. {self.name} evaded the attack using their {self._abilities["evasion"]} ability!")
            self.display_stats()
            self.__evasion = False
        else:
            self.health = self.health - hit_damage
            print(f"\n{self.name} was hit by {attack_name} for {hit_damage} damage.")
            self.display_stats()

    #function to enable the evasion special ability
    def evade_attack(self):
        self.__evasion = True
        print(f"\n{self.name} has used their {self._abilities["evasion"]} ability")

    #special attack function for characters
    def special_attack(self, opponent):
        print(f"\n{self.name} has used their {self._abilities["attack"]} attack !!!")
        #randomize extra damage from the special attack and add it to the base attack power
        opponent.damage(self.__attack_power + randint(10, 20), self._abilities["attack"], self)

    #function to access the character's special abilities
    def use_abilities(self, opponent):
        while True:
            print("\n--- Special Abilities ---")
            print(f"1. Evade the next attack with your {self._abilities["evasion"]} ability")
            print(f"2. Use your {self._abilities["attack"]} special attack")
            choice = input("Please input the number of your choice: ")
            if choice == "1":
                self.evade_attack()
                break
            elif choice == "2":
                self.special_attack(opponent)
                break
            else:
                print("That was an incorrect choice. Please try again")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health if self.health > 0 else 0}/{self._max_health}, Attack Power: {self.__attack_power}\n")

    #function to quickly calculate randomized attack damage within a standardized range based on character attack power
    def calculate_attack_damage(self): 
        return randint(self.__attack_power - self.__attack_power // 5 , self.__attack_power + self.__attack_power // 5)

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, attack_name="Sword Thrust", evasion="Parry", sp_attack="Legendary Sword")
        
# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, attack_name="Attack Magic", evasion="Barrier", sp_attack="Fireball")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, attack_name="Evil Magic", evasion="Devils' Sheild", sp_attack="Dark Lightning")

    def regenerate(self):
        if self.health < self._max_health - 5:
            self.health += 5
        else:
            self.health = self._max_health
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20, attack_name="Single Shot", evasion="Evade", sp_attack="Quick Shot")
        
    #Archer specific special attack
    def special_attack(self, opponent):
        print(f"The Archer {self.name} has used their Quick Shot ability!!!")
        opponent.damage(self.calculate_attack_damage(), self._attack_name, self)
        opponent.damage(self.calculate_attack_damage(), self._attack_name, self)

# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, attack_name="Holy Magic", evasion="Divine Shield", sp_attack="Holy Strike")
