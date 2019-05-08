class Character():

    def __init__(self, name, hp, attackpower, defensepower, magic = 0):
        self.name = name
        self.hp = hp
        self.attackpower = attackpower
        self.defensepower = defensepower
        self.magic = magic

    def isDead(self):
        if self.hp <= 0:
            return True
        else:
            return False
    
    def isPartyDead(self):
        partyDead = []
        for p in range(len(party)):
            partyDead.append(party[p].isDead())

    def attack(self):
        #party's turn
        if self.name != "Boss":
            damage = self.attackpower - boss.defensepower
            if self.magic > 0:
                damage += self.magic
            return damage

        #Boss's turn
        else:
            for bTurn in range(len(party)):
                if party[bTurn].isDead() == False:
                    damage = self.attackpower - party[bTurn].defensepower
                    party[bTurn].hp -= damage
                    print("Boss does", damage, "damage to", party[bTurn].name)

    def heal(self):
        for atk in range(len(party)):
            if party[atk].isDead() == False:
                party[atk].hp += self.attack()
                print(self.name, "heals", self.attack(), "HP for", party[atk].name)
    
    def __str__(self):
        return self.name + " has " + str(self.hp) + " HP."


#get character information
krogg = Character("Krogg", 180, 20, 20)
glinda = Character("Glinda", 120, 5, 20, 5)
geofferey = Character("Geofferey", 150, 15, 15)
party = [krogg, glinda, geofferey]
boss = Character("Boss", 500, 25, 15)

#start game
gameRound = 1
while party.isDead() == False and boss.isDead() == False:
    #display round number
    print("\nROUND", gameRound)
    gameRound += 1

    #Party's turn
    for pTurn in range(len(party)):
        #Krogg's turn or Geoffery's turn
        if party[pTurn].name == krogg.name or party[pTurn].name == geofferey.name:
            if party[pTurn].isDead() == True:
                print(party[pTurn].name, "cannot attack because he is dead.")
            else:
                #attack the boss
                boss.hp -= party[pTurn].attack()
                print(party[pTurn].name, "does", party[pTurn].attack(), "points of damage to Boss")
        
        #Glinda's turn
        else:
            if party[pTurn].isDead() == True:
                print(party[pTurn].name, "cannot heal because she is dead.")
            else:
                #heal the party
                glinda.heal()
        
    #Boss's turn
    if boss.isDead() == True:
        print("Boss cannot attack because it is dead.")
    else:
        #attack the party
        boss.attack()
    
    #display information of each character
    print(boss.__str__())
    for p in range(len(party)):
        print(party[p].__str__())

#game endings
if boss.isDead() == True:
    print("\nThe Boss is dead. You are victorious!")
elif krogg.isDead() == glinda.isDead() == geofferey.isDead() == True:
    print("\nYour whole party is dead. You lose.")
