#check if party is dead
def isPartyDead(hp):
    for pts in range(len(hp)):
        if hp[pts] <= 0:
            return True
        else:
            return False

#check if party member is dead
def isDead(health):
    if health <= 0:
        return True
    else:
        return False

def main():
    partyNames = ['Krogg', 'Glinda', 'Geoffrey']
    partyHP = [180, 120, 150]
    partyAttack = [20, 5, 15]
    partyDefense = [20, 20, 15]

    bossAttack = 25
    bossDefense = 15
    bossHP = 500

    gameRound = 1

    while isPartyDead(partyHP) == False and bossHP > 0:
        #display round number
        print("\nRound", gameRound)
        gameRound += 1

        #Party's turn
        for party in range(len(partyNames)):
            if bossHP > 0:
                #Krogg's turn or Geoffery's turn
                if partyNames[party] == "Krogg" or partyNames[party] == "Geoffrey":
                    if isDead(partyHP[party]) == True:
                        print(partyNames[party], "cannot attack because he is dead")
                        isPartyDead(partyHP)
                    else:
                        print(partyNames[party], "does", partyAttack[party], "points of damage to Boss")
                        bossHP -= partyAttack[party]
                #Glinda's turn
                else:
                    if isDead(partyHP[party]) == False:
                        partyHP[party - 1] += partyAttack[party]
                        partyHP[party + 1] += partyAttack[party]
                    else:
                        isDead(partyHP[party])
                        print(partyNames[party], "cannot heal because she is dead")
                        isPartyDead(partyHP)
            
        #Boss's turn
        for boss in range(len(partyNames)):
            if partyHP[boss] > 0:
                print("Boss does", bossAttack, "points of damage to", partyNames[boss])
                partyHP[boss] -= bossAttack
        
        #print health
        print("Boss:", bossHP)
        print("Krogg:", partyHP[0])
        print("Glinda:", partyHP[1])
        print("Geoffrey:", partyHP[2])
    
    #display ending message
    if isPartyDead(partyHP) == True:
        print("\nYour whole party is dead. You lose.")
    elif bossHP <= 0:
        print("\nThe boss is dead. You are victorious!")

main()
