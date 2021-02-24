#Added this for loop to check if the user types in a percentage sign. if so then we remove the % sign by slicing
def checkPercentage(percentStr):
    for i in range(len(percentStr)):
        if '%' in percentStr[i]:
            percentStr = percentStr[:i]
    return int(percentStr)

#calculate how much n% is out of the price of bill
def percentOfBill(price,percent):
   return ( price * (percent/100))

#add the percent to orginal bill
def totalPrice(price, percentFromPrice):
    return (price + percentFromPrice)

#divied the total price per person
def totalPircePerPerson(totalPrice,numOfPpl):
    return (round(totalPrice,2)/numOfPpl)

#get the total tip person calculation
def totalTipPerPerson(percentFromPrice,numOfPpl):
    return (percentFromPrice/numOfPpl)


