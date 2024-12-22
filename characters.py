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

    #generic attack function definition
    def attack(self, opponent): 
        opponent.damage(self.calculate_attack_damage(), self._attack_name, self)
    
    #heal fuction for characters
    def heal(self):
        #check that health won't exceed max_health and then add 20
        if self.health + 20 < self._max_health:
            self.health += 20
        # set health to max_health if adding 20 will meet or exceed max_health
        else:
            self.health = self._max_health

        print(f"\n{self.name} healed themself. Current health: {self.health}")

    #damage function for character taking damage from attack and evasion of attacks using special skills
    def damage(self, hit_damage, attack_name, opponent):
        #Check if evasion ability flag is True and continue without taking damage
        if self.__evasion:
            print(f"\n{opponent.name} attacked {self.name} with {attack_name}. {self.name} evaded the attack using their {self._abilities["evasion"]} ability!")
            self.display_stats()
            self.__evasion = False
        #no flag set: add damage value from arguements and update user
        else:
            self.health = self.health - hit_damage
            print(f"\n{self.name} was hit by {attack_name} for {hit_damage} damage.")
            self.display_stats()

    #function to enable the evasion special ability
    def evade_attack(self):
        self.__evasion = True #set evasion flag for the evasion ability
        print(f"\n{self.name} has used their {self._abilities["evasion"]} ability")

    #special attack function for characters
    def special_attack(self, opponent):
        print(f"\n{self.name} has used their {self._abilities["attack"]} attack !!!")
        #randomize extra damage from the special attack and add it to the base attack power
        opponent.damage(self.__attack_power + randint(10, 20), self._abilities["attack"], self)

    #function to access the character's special abilities
    def use_abilities(self, opponent):
        #choice loop
        while True:
            print("\n--- Special Abilities ---")
            print(f"1. Evade the next attack with your {self._abilities["evasion"]} ability")
            print(f"2. Use your {self._abilities["attack"]} special attack")
            choice = input("Please input the number of your choice: ")
            #choose the evasion special ability
            if choice == "1":
                self.evade_attack()
                break
            #choose the special attack ability
            elif choice == "2":
                self.special_attack(opponent)
                break
            #invalid choice
            else:
                print("That was an incorrect choice. Please try again")
    #function that displays the character's current stats
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health if self.health > 0 else 0}/{self._max_health}, Attack Power: {self.__attack_power}\n")

    #function to quickly calculate randomized attack damage within a standardized range based on character attack power
    def calculate_attack_damage(self): 
        return randint(self.__attack_power - self.__attack_power // 5 , self.__attack_power + self.__attack_power // 5)

# Warrior class (inherits from Character) no special functions
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, attack_name="Sword Thrust", evasion="Parry", sp_attack="Legendary Sword")
        
# Mage class (inherits from Character) no special functions
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, attack_name="Attack Magic", evasion="Barrier", sp_attack="Fireball")

#EvilWizard's Undead Minions class (inherits from Character) no special functions
class Minion(Character):
    def __init__(self, name):
        super().__init__(name, health = randint(10, 15), attack_power = randint(1, 5), attack_name = "Bone Sword", evasion = None, sp_attack= None)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, attack_name="Evil Magic", evasion="Devils' Sheild", sp_attack="Undead Minions")

    #special randomized attack function for the EvilWizard class that selects between, attack, the special abilities and healing actions
    def attack(self, opponent):
        try:
            attack_decision = randint(1,4)
            #attack
            if attack_decision == 1:
                super().attack(opponent)
            #evasion special ability
            elif attack_decision == 2:
                self.evade_attack()
            #special attack ability
            elif attack_decision == 3:
                self.special_attack(opponent)
            #heal if health is below threshold
            elif attack_decision == 4 and self.health <= 100:
                self.heal()
            #just do a basic attack if above threshold
            elif attack_decision == 4 and self.health > 100:
                super().attack(opponent)
            #invalid RNG Value
            else:
                raise ValueError("RNG value not in acceptable range")
        except ValueError as ve:
            print(f"an error has occured: {ve}")

    #implementation of the undead minions logic
    def undead_minions(self, minions, opponent):
        print(f"You must now fight the Undead Minions of {self.name}")
        
        #Verify that minions are actually created for attack
        while minions:
            #randomly select minion, have it attack player
            minion_index = randint(0, len(minions) - 1)
            minions[minion_index].attack(opponent)
            #player automatically attacks back if not killed by minion attack
            if opponent.health <= 0:
                print(f"\n{self.name}'s {self._abilities["attack"]} defeated {opponent.name}")
                break
            opponent.attack(minions[minion_index])
            #remove minion from minions list if minion killed by player attack
            if minions[minion_index].health <= 0:
                print(f"{minions[minion_index].name} was killed by {opponent.name}")
                minions.pop(minion_index)
            
            #check and notify player if all minions defeated by last attack
            if not minions:
                print(f"\n{opponent.name} has defeated all of {self.name}'s {self._abilities["attack"]}")
                break

    #EvilWizard specific special attack function that calls on the undead_minions function
    def special_attack(self, opponent):
        print(f"The {self.name} has used called upon their 7 {self._abilities["attack"]}!!!")
        minions = [Minion(name = f"Minion {x + 1}") for x in range(0,7)]
        self.undead_minions(minions, opponent)

    #EvilWizard's regeneration function with protection against values higher than max_health
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
        
    #Archer specific special attack that shoots 2 regular shots quickly one after the other
    def special_attack(self, opponent):
        print(f"The Archer {self.name} has used their Quick Shot ability!!!")
        opponent.damage(self.calculate_attack_damage(), self._attack_name, self)
        opponent.damage(self.calculate_attack_damage(), self._attack_name, self)

# Paladin class (inherits from Character) no special functions
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, attack_name="Holy Magic", evasion="Divine Shield", sp_attack="Holy Strike")
