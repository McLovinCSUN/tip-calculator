from calculations import *

#first I am going to create two variables 
 #then set them equal to the information from the user
print("~~~~~~~~~~Tip Calculator~~~~~~~~~~")
price = int(input('Please, enter total price:\n'))
percent = input('Please, enter tip percent amount :\n')
percent=checkPercentage(percent)
numOfPpl=int(input('Please, enther the total number of people in your party:\n'))

#call functions to do calculations
percentFromPrice = percentOfBill(price,percent)
totalPrice = totalPrice(price,percentFromPrice)
totalPircePerPerson = totalPircePerPerson(totalPrice,numOfPpl)
totalTipPerPerson = totalTipPerPerson(percentFromPrice,numOfPpl)

#list out all the calculations for the user to see
print("~~~~~~~~~~Bill~~~~~~~~~~~~~~~~")
print(f'${price}')
print(f"~~~~~~Tip per person~~~~~~~~~~~~")
print(f'${round(totalTipPerPerson,2)}')
print(f"~~~~~~~Total per person~~~~~~~~~~")
print(f'${round(totalPircePerPerson,2)}')