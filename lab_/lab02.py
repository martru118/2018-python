kroggName = 'Krogg'
kroggClass = 'Warrior'
kroggLevel = 1
kroggAttack = 18.5
kroggDefense = 12.5
kroggHP = 200
kroggXP = 0
kroggWeapons = ['Axe', 'Dagger', 'Unarmed']
krogg = (kroggName, kroggClass, kroggLevel, kroggAttack, kroggDefense, kroggHP, kroggXP, kroggWeapons)

glindaName = 'Glinda'
glindaClass = 'Spellcaster'
glindaLevel = 1
glindaAttack = 4.5
glindaDefense = 25.0
glindaHP = 120
glindaXP = 0
glindaWeapons = ['Staff', 'Unarmed']
glinda = (glindaName, glindaClass, glindaLevel, glindaAttack, glindaDefense, glindaHP, glindaXP, glindaWeapons)

geoffereyName = 'Geofferey'
geoffereyClass = 'Paladin'
geoffereyLevel = 1
geoffereyAttack = 15.0
geoffereyDefense = 12.5
geoffereyHP = 180
geoffereyXP = 0
geoffereyWeapons = ['Bow', 'Sword']
geofferey = (geoffereyName, geoffereyClass, geoffereyLevel, geoffereyAttack, geoffereyDefense, geoffereyHP, geoffereyXP, geoffereyWeapons)

darkdragonName = 'Dark Dragon'
darkdragonClass = 'Warrior'
darkdragonLevel = 10
darkdragonAttack = 25
darkdragonDefense = 17.5
darkdragonHP = 500
darkdragonXP = 1000
darkdragonWeapons = ['Flame Breath']
darkdragon = (darkdragonName, darkdragonClass, darkdragonLevel, darkdragonAttack, darkdragonDefense, darkdragonHP, darkdragonXP, darkdragonWeapons)


#simulate battles and game
party = [kroggName, glindaName, geoffereyName]
partyAttack = True

print("Krogg attacks Dark Dragon. DMG:", kroggAttack)
print("Glinda attacks Dark Dragon. DMG:", glindaAttack)
print("Geofferey attacks Dark Dragon. DMG:", geoffereyAttack)
darkdragonHP -= (kroggAttack + glindaAttack + geoffereyAttack)
print(darkdragonHP)