"""
This is the first working draft / minimum viable product for a game concept. 
This will explore combat by mkaing and setting equipemnt manually then doing rounds of combat until there is a winner. 

For example, I will make player1, player2, player3, and player4.

Each player can have a spell with active and passive effects.
For this, I will make a burn spell that does 1 damage every turn for 3 turns, plus 2 damage on hit.

Each player can have a weapon with active and passive effects.
For this, I will make a sword that does 3 damage on hit, and a shield that blocks 1 damage every turn. Eventually, the shield will only block physical damage. 

Each player can have a piece of armor with active and passive effects.
We will not do this for now.
"""


class Character(object):
    def __init__(self, name, health, spell, weapon, armor):
        self.name = name
        self.health = health
        self.spell = spell
        self.weapon = weapon
        self.armor = armor
        self.conditions = []

    def __str__(self):
        return f"{self.name} has {self.health} health, {self.spell} spell, {self.weapon} weapon, and {self.armor} armor."

    # def __repr__(self):
    #     return f"{self.name} has {self.health} health, {self.spell} spell, {self.weapon} weapon, and {self.armor} armor."

    def attack(self, target):
        target.health -= self.weapon.damage
        print(
            f"{self.name} attacks {target.name} with {self.weapon.name} for {self.weapon.damage} damage."
        )

    def cast(self, target):
        target.health -= self.spell.damage
        print(
            f"{self.name} casts {self.spell.name} on {target.name} for {self.spell.damage} damage."
        )

    def defend(self):
        self.health += self.armor.defense
        print(
            f"{self.name} defends with {self.armor.name} for {self.armor.defense} health."
        )

    def checkConditions(self):
        for condition in self.conditions:
            if condition.duration > 0:
                self.health -= condition.damage
                condition.duration -= 1
                print(
                    f"{self.name} takes {condition.damage} damage from {condition.name}."
                )
            else:
                self.conditions.remove(condition)


class Condition(object):
    def __init__(self, name, damage, duration):
        self.name = name
        self.damage = damage
        self.duration = duration

    def __str__(self):
        return f"{self.name} does {self.damage} damage over {self.duration} turns."

    def __repr__(self):
        return f"{self.name} does {self.damage} damage over {self.duration} turns."


class Spell(object):
    def __init__(self, name, damage, duration):
        self.name = name
        self.damage = damage
        self.duration = duration

    def __str__(self):
        return f"{self.name} does {self.damage} damage over {self.duration} turns."

    def __repr__(self):
        return f"{self.name} does {self.damage} damage over {self.duration} turns."


class Weapon(object):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f"{self.name} does {self.damage} damage."

    def __repr__(self):
        return f"{self.name} does {self.damage} damage."


class Armor(object):
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def __str__(self):
        return f"{self.name} blocks {self.defense} damage."

    def __repr__(self):
        return f"{self.name} blocks {self.defense} damage."


# Create spells
burn = Spell("Burn", 2, 3)

# Create weapons
sword = Weapon("Sword", 3)

# Create armor
shield = Armor("Shield", 1)

# Create characters
player1 = Character("Player1", 10, burn, sword, shield)
player2 = Character("Player2", 10, burn, sword, shield)
player3 = Character("Player3", 10, burn, sword, shield)
player4 = Character("Player4", 10, burn, sword, shield)

# Print characters
print(player1)
print(player2)
print(player3)
print(player4)


import random

players = [player1, player2, player3, player4]
actions = ["attack", "cast", "defend"]
burned = Condition("Burn", 1, 3)


def isAlive(player):
    if player.health > 0:
        return True
    else:
        return False


def takeTurn(player):
    print(f"{player.name}'s conditions: {player.conditions}")
    player.checkConditions()
    action = random.choice(actions)
    # target should be a random choice from the list of players that are alive, and not the player taking the turn.
    targets = []
    for target in players:
        if isAlive(target) and target != player:
            targets.append(target)
    target = random.choice(targets)
    if action == "attack":
        player.attack(target)
    elif action == "cast":
        player.cast(target)
        if target.spell != burned:
            target.conditions.append(burned)
        else:
            print(f"{target.name} is already burned.")
    elif action == "defend":
        player.defend()


def takeTurns():
    for player in players:
        if isAlive(player):
            takeTurn(player)
        else:
            print(f"{player.name} is dead.")


def isGameOver():
    aliveCount = 0
    for player in players:
        if isAlive(player):
            aliveCount += 1
    if aliveCount <= 1:
        return True
    else:
        return False


def gameOver():
    for player in players:
        if isAlive(player):
            print(f"{player.name} wins!")
            break


turn = 0


def takeTurns():
    global turn
    turn += 1
    print(f"Turn {turn}")
    for player in players:
        if isAlive(player):
            takeTurn(player)
        else:
            print(f"{player.name} is dead.")


while not isGameOver():
    takeTurns()
gameOver()
