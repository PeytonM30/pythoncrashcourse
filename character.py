import random
class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        self.is_alive = True

    def greet(self):
        print(f"My name is {self.name}!")

    def instigate(self, opponent_name):
        print(f"{self.name}: You suck at your job {opponent_name}")

    def instigate_2(self, opponent_name):
        print(f"{self.name}: You're even worse at your job {opponent_name}")


    def attack(self, opponent):
        # who is attacking who
        # how much damage they do
        # remaining health of the one who was attacked
        damage = self.damage()
        print(f"{self.name} attacks {opponent.name}")
        print(f"{self.name} does {damage} damage")
        opponent.health = opponent.health - damage
        if (opponent.health < 0):
            opponent.is_alive = False
            print(f"{opponent.name} is dead!")
        else:
            print(f"{opponent.name} has {opponent.health} health remaining")

    def damage(self):
        return int(self.strength + random.randrange(0,int(self.strength/2)) - self.strength/4)


character_1 = Character("Joel", 100, 25)
character_2 = Character("Troy", 100, 25)

character_1.greet()
character_2.greet()
character_1.instigate(character_2.name) 
character_2.instigate_2(character_1.name)

while character_1.health > 0 and character_2.health > 0:
    if (random.randrange(0,2)) == 0:
        character_1.attack(character_2)
        if character_2.is_alive:
            character_2.attack(character_1)
    else:
        character_2.attack(character_1)
        if character_1.is_alive:
            character_1.attack(character_2)
