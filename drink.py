#BartenderBotV0
#https://github.com/zsarnold
#Drink file. Used to start drink and configure what drink.

import math

#import pump.py (Custom motor driver using a time)
#call motor code for the pump within drink function
#import pump.py

#import convey.py (Custom conveyor functions)
#call stepper functions: homeConvey(0mm), fillConvey(150mm?), finalConvey(300mm?)
#import convey.py

#given file
drinkList = "Files/drink.txt"

#Gets the drink recipe from the csv file
#input: string of drink name
def getRecipe ( drinkName ):
    vebose = False
    recipe = []
    #Get file line size
    f = open(drinkList, "r")
    f.seek(0, 2)
    pos = f.tell()
    f.seek(0)

    #read column 1 of csv until you find drink name
    line = f.readline()
    while line:
        if line.strip() == drinkName:
            #print("Found it!)
            verbose = True
            break
        line = f.readline()

    #once found, grab that line and 7 after for the recipe array(1x8)
    if verbose:
        recipe.append(f.readline().strip("\n").split(","))
        recipe.append(f.readline().strip("\n").split(","))
        recipe.append(f.readline().strip("\n").split(","))
        recipe.append(f.readline().strip("\n").split(","))
        recipe.append(f.readline().strip("\n").split(","))
        recipe.append(f.readline().strip("\n").split(","))
        recipe.append(f.readline().strip("\n").split(","))
        recipe.append(f.readline().strip("\n").split(","))

    #print(recipe)
    f.close()
    return recipe
#Gets the strength multiplier for the drink recipe
#input: string of the strength
def getStrength ( drinkStrength ):
    if drinkStrength == "strong":
        strengthMulti = 1.5
    elif drinkStrength == "weak":
        strengthMulti = .75
    else:
        strengthMulti = 1
    return strengthMulti

#Tells the pumps to start dispensing the drink according to recipe
#input: 1x8 array with time for each pump after strength multiplier
def drink ( drinkRecipeStrength ):
    #for 1 -> 8, turn each respective pump on for time in array
    print(test)
        #pump.py will have function that takes pump # and time in S

#tells the bot to start creating a drink
#input: drink recipe from fun(getDrink), strenght multipler value from getStrength
def startDrink ( drinkName, drinkStrength ):
    #home pallet, move convey until hits switch
    print("Homing Pallet")

    #move pallet until under dispenser
    print("Under Dispenser")

    #get multiplier
    mult = getStrength( drinkStrength )

    #add multipler to drink recipe array
    rec = getRecipe( drinkName )
    #rec[:,2] = math.prod(rec[:,2], mult)
    for x in range(0, 8):
        rec[x][0] = int(rec[x][0])
        rec[x][1] = int(rec[x][1]) * mult
        print(rec[x][1])

    #dispense drink by calling drink function
    print("Dispensing")

    #move pallet to end of conveyor
    print("Drink done!")

    #wait 30 seconds
    print("Waiting.......")

    #home pallet, move convey until hits switch
    print("Homing pallet again.")

startDrink("GreenTea", "weak")
