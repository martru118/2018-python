partyNames = ['Krogg', 'Glinda', 'Geoffrey']
partyHP = [180, 120, 150]
partyAttack = [20, 5, 15]
partyDefense = [20, 20, 15]
partyDead = [False, False, False]

bossAttack = 25
bossDefense = 15
bossHP = 500

gameRound = 1

while (partyDead[0] == False or partyDead[1] == False or partyDead[2] == False) and bossHP > 0:
    print("\nRound", gameRound)
    gameRound += 1

    #Party's turn
    for party in range(3):
        if bossHP > 0:
            if party == 0 or party == 2:
                if partyHP[0] <= 0:
                    partyDead[0] = True
                    print(partyNames[0], " cannot attack because he is dead.")
                elif partyHP[2] <= 0:
                    print(partyNames[2], " cannot attack because he is dead.")
                    partyDead[2] = True
                else:
                    print(partyNames[party], " does ", partyAttack[party], " points of damage to boss.")
                    bossHP -= partyAttack[party]
            else:
                if partyHP[1] > 0:
                    partyHP[0] += partyAttack[1]
                    partyHP[2] += partyAttack[1]
                else:
                    partyDead[1] = True
                    print(partyNames[1], " cannot heal because she is dead.")
        
    #Boss's turn
    for boss in range(3):
        if partyHP[boss] > 0:
            print("Boss does ", bossAttack, " points of damage to ", partyNames[boss])
            partyHP[boss] -= bossAttack
    
    #print health
    print("Boss: ", bossHP)
    for hp in range(3):
        print(partyNames[hp], ": " , partyHP[hp])
