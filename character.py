class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"My name is {self.name}!")

    def instigate(self, opponent_name):
        print(f"{self.name}: You suck at your job {opponent_name}")

    def instigate_2(self, opponent_name):
        print(f"{self.name}: Your even worse at your job {opponent_name}")


    def attack(self, opponent):
        # who is attacking who
        # how much damage they do
        # remaining health of the one who was attacked
        print(f"{self.name} attacks {opponent.name}")
        print(f"{self.name} does {self.strength} damage")
        opponent.health = opponent.health - self.strength
        print(f"{opponent.name} has {opponent.health} health remaining")



character_1 = Character("Joel", 100, 30)
character_2 = Character("Troy", 100, 25)


print(character_1.name, character_1.health)
print(character_2.name, character_2.health)

character_1.greet()
character_2.greet()
character_1.instigate(character_2.name) 
character_2.instigate_2(character_1.name)
character_1.attack(character_2)