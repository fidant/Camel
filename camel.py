import random

print('\nWelcome to Camel!')
print('\nYou have stolen a camel to make your way across the great Mobi desert.')
print('The natives want their camel back and are chasing you down! Survive your')
print('desert trek and outrun the natives. \n' )

done = False
milesTraveled = 0
thirst = 0
camelTiredness = 0
nativeDistance = -20
drinksInCanteen = random.randint(3, 12)
oasis = random.randint(1,20)

while (done == False):
    print('A. Drink from your canteen.')
    print('B. Ahead moderate speed.')
    print('C. Ahead full speed.')
    print('D. Stop for the night.')
    print('E. Status check.')
    print('Q. Quit. \n')
    answer = input('What will you do? \n ')
# Quit
    if answer.upper() == 'Q':
        done = True
#Status
    elif answer.upper() == 'E':
        print('\nYou have traveled ' + str(milesTraveled) + ' miles.')
        print('There are ' + str(drinksInCanteen) + ' drinks left in your canteen.')
        print('The natives are ' + str(abs(nativeDistance)) + ' miles behind you. \n')
#Rest
    elif answer.upper() == 'D':
        camelTiredness = 0
        nativeDistance += random.randint(7, 14)
        print('\n The camel is glad to have a break. \n')
        if nativeDistance >= 0 :
            print('\nYou have been captured by the natives!')
            print('They have taken back their camel and cut off your hand.')
            print('GAME OVER!!!! \n')
            done = True
#FullSpeed
    elif answer.upper() == 'C' :
            nativeThisTrip = random.randint(7,14)
            oasisChance = random.randint(1,20)
            thisTrip = random.randint(10,20)
            print('\nYou traveled ' + str(thisTrip) + ' miles.\n')
            if oasisChance == oasis:
                milesTraveled += thisTrip
                thirst = 0
                camelTiredness = 0
                drinksInCanteen = 12
                print('\nYou found an oasis in the desert. You quench your thirst, rest your camel, and fill your canteen.\n')
            else:
                milesTraveled += thisTrip
                thirst += 1
                camelTiredness += random.randint(1,3)
                nativeDistance = nativeDistance + nativeThisTrip - thisTrip
            if thirst > 6 :
                print('\nYou have died of thirst.')
                print('GAME OVER!!!! \n')
                done = True
            if thirst > 4:
                print ('\nYou are very thirsty.\n')
            if camelTiredness > 5 :
                print('\nYour camel is looking tired.\n')
            if camelTiredness > 8 :
                print('\nYour camel collapses exahausted falling on top of you and killing you.\n')
                print('GAME OVER !!!!\n')
                done = True
            if nativeDistance >= 0 :
                print('\nYou have been captured by the natives!')
                print('They have taken back their camel and cut off your hand.')
                print('GAME OVER!!!! \n')
                done = True
            if milesTraveled == 200 :
                print('\nYou have done it! You have escaped with your new camel.\n')
                done = True
#ModerateSpeed
    elif answer.upper() == 'B' :
        nativeThisTrip = random.randint(7,14)
        oasisChance = random.randint(1,20)
        thisTrip = random.randint(5,12)
        print('\nYou traveled ' + str(thisTrip) + ' miles.\n')

        if oasisChance == oasis:
            milesTraveled += thisTrip
            thirst = 0
            camelTiredness = 0
            drinksInCanteen = 12
            print('\nYou found an oasis in the desert. You quench your thirst, rest your camel, and fill your canteen.\n')
        else:
            milesTraveled += thisTrip
            thirst += 1
            camelTiredness += random.randint(1,3)
            nativeDistance = nativeDistance + nativeThisTrip - thisTrip
        if thirst > 6 :
            print('\nYou have died of thirst.')
            print('GAME OVER!!!! \n')
            done = True
        if thirst > 4:
            print ('\nYou are very thirsty.\n')
        if camelTiredness > 5 :
            print('\nYour camel is looking tired.\n')
        if camelTiredness > 8 :
            print('\nYour camel collapses exahausted falling on top of you and killing you.\n')
            print('GAME OVER !!!!\n')
            done = True
        if nativeDistance >= 0 :
            print('\nYou have been captured by the natives!')
            print('They have taken back their camel and cut off your hand.')
            print('GAME OVER!!!! \n')
            done = True
        if milesTraveled == 200 :
            print('\nYou have done it! You have escaped with your new camel.\n')
            done = True

#Drink
    elif answer.upper() == 'A':
        if drinksInCanteen > 0 :
            print ('\nYou take a long drink from your canteen. \n')
            drinksInCanteen -= 1
            thirst -= 1
            nativeDistance += random.randint(1, 3)
        else :
            print ('\nThere is no more water in your canteen.\n')
            nativeDistance += random.randint(1, 3)
        if thirst > 6 :
            print('\nYou have died of thirst.')
            print('GAME OVER!!!! \n')
            done = True
        if thirst > 4:
            print ('\nYou are very thirsty.\n')
        if camelTiredness > 5 :
            print('\nYour camel is looking tired.\n')
        if camelTiredness > 8 :
            print('\nYour camel collapses exahausted falling on top of you and killing you.\n')
            print('GAME OVER !!!!\n')
            done = True
        if nativeDistance >= 0 :
            print('\nYou have been captured by the natives!')
            print('They have taken back their camel and cut off your hand.')
            print('GAME OVER!!!! \n')
            done = True
        if milesTraveled == 200 :
            print('\nYou have done it! You have escaped with your new camel.\n')
            done = True
#comment nativeThisTrip
