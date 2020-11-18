#BartenderBotV0
#https://github.com/zsarnold
#Drink file. Used to start drink and configure what drink.

#import pump.py (Custom motor driver using a time)
#call motor code for the pump within drink function
import pump.py

#import convey.py (Custom conveyor functions)
#call stepper functions: homeConvey(0mm), fillConvey(150mm?), finalConvey(300mm?)
import convey.py

#given file
drinkList = "files/drink.csv"

#Gets the drink recipe from the csv file
#input: string of drink name
def getDrink ( drinkName ):
    #read column 1 of csv until you find drink name

    #once found, grab that line and 7 after for the recipe array(1x8)

#Gets the strength multiplier for the drink recipe
#input: string of the strength
def getStrength ( drinkStrength ):
    if strength == "strong":
        strengthMulti = 1.5
    elif strength == "weak":
        strengthMulti = .75
    else:
        strengthMulti = 1

#Tells the pumps to start dispensing the drink according to recipe
#input: 1x8 array with time for each pump after strength multiplier
def drink ( drinkRecipeStrength ):
    #for 1 -> 8, turn each respective pump on for time in array

        #pump.py will have function that takes pump # and time in mS

#tells the bot to start creating a drink
#input: drink recipe from fun(getDrink), strenght multipler value from getStrength
def startDrink ( drinkRecipe, strengthMulti ):
    #home pallet, move convey until hits switch

    #move pallet until under dispenser

    #add multipler to drink recipe array

    #dispense drink by calling drink function

    #move pallet to end of conveyor

    #wait 30 seconds

    #home pallet, move convey until hits switch
