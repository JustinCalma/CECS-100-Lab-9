#Import random
import random

#Define Main
def main():
    randList()
    lowNumb(list)
    highNumb(list)
    totalNumb(list)

#Generate random numbers
def randList():
    list = []
    for i in range(0, 20):
        x = random.randint(0, 100)
        list.append(x)
    lowNumb(list)
    highNumb(list)
    print(list)

#Function for Lowest number
def lowNumb(list):
    low = min(list)
    print("Low:", low)

#Function for Highest number
def highNumb(list):
    high = max(list)
    print("High:", high)
    
#Function for getting the total
def totalNumb(list):
    total = 0
    for i in list:
        total = total + list[i]
    print("Total:", total)
    

main()


