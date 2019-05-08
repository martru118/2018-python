kroggAttack = 26.0
kroggDefense = 20.0
kroggHP = 200.0

bossAttack = 5.0
bossDefense = 12.5
bossHP = 200.0

gameRound = 1

while kroggHP >= 0 and bossHP >= 0:
    print("\nRound", gameRound)
    print("Krogg does ", kroggAttack, " damage to Boss")
    print("Boss does ", bossAttack, " damage to Krogg")

    bossHP -= kroggAttack
    print("Boss: ", bossHP)
    kroggHP -= bossAttack
    print("Krogg: ", kroggHP)
    
    gameRound += 1

    if kroggHP <= 0:
        print("Boss has won. You have been defeated!")
        break
    elif bossHP <= 0:
        print("Krogg has won. You are victorious!")
        break
