import csv

def open_file():
    fp = open('drinkTest.csv','r')
    return fp

def build_dict(fp):
    dictionary={}
    reader=csv.reader(fp)
    temp=[]
    drinkName=""
    for row in reader:
        #Try except handles the difference between a drink label row and the pump time row
        try:
            numTest=float(row[0])
            newDrink=False
        except ValueError:
            newDrink=True

        if(newDrink==True):
            drinkName=row[0]
        else:
            temp=[float(row[0]),float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6])]
            dictionary[drinkName]=tuple(temp)

    return dictionary

def main():
    #open file
    fp = open_file()
    drink_dict=build_dict(fp)
    print(drink_dict)
    fp.close()
    return drink_dict

