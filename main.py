#Coffee Shop
import os

#Assign costs to variables
coffeeCost = 2.50
donutCost = 1.25
powerBarCost = 3.00

#This is for the repeat symbols
repeatSymbol = 30
lineSeperator1 = "-" * repeatSymbol
lineSeperator2 = "*" * repeatSymbol
lineSeperator3 = "^" * repeatSymbol

#This shows uer how much each item costs
#Concatenates string with variables
#Uses data type conversion str(), coverts integers or floats into string
#Four types of variables, string, floats, integers, and booleans(True or False)
print(lineSeperator3)
print("Items Costs: ")
print("Coffee: $ " + str(coffeeCost))
print("Donuts: $ " + str(donutCost))
print("Powerbars: $ " + str(powerBarCost))

print(lineSeperator2)
print("")

#This sets the orderAgain conditional for the while loop
#Runs while something is true
#Single equal sign is "assignment operator"
#Double equal sign is "boolean test"
orderAgain = "yes"
while orderAgain == "yes":

  #This gets the user's name
  userName = input("Enter your name: ")

  #initial message
  print ("Hi " + userName + ",Welcome to Advay's Coffee shop!")

  #This gets the user's age and type converts it into a integer
  userAge = int(input("What is your age"))
  #This prints the user's age
  print (userAge)

  #User Inputs
  coffeesOrdered = int(input("How many coffees do you want?: "))
  donutsOrdered = int(input("How many donuts do you want?: "))
  powerBarsOrdered = int(input("How many powerBars do you want"))
  print(lineSeperator3)

  #processing(costs * number of items ordered)
  coffeesOrderedSum = coffeeCost * coffeesOrdered
  donutsOrderedSum = donutCost * donutsOrdered
  powerBarsOrderedSum = powerBarCost * powerBarsOrdered
  
  #Outputs of subtotals and total
  print("Subtotals")
  print("Coffees Cost: " + str(coffeesOrdered) + " x " +str(coffeeCost) + " = $" + str(coffeesOrderedSum))
  print("Donuts Cost: " + str(donutsOrdered) + " x " +str(donutCost) + " = $" + str(donutsOrderedSum))
  print("PowerBars Cost: " + str(powerBarsOrdered) + " x " +str(powerBarCost) + "= $" + str(powerBarsOrderedSum))
  
  #This adds up all the subtotals, is integer type
  orderTotal = coffeesOrderedSum + donutsOrderedSum + powerBarsOrderedSum
  print("")
  print ("Your order total is: $" + str(orderTotal))
  Payment_Method = input("How would you like to pay? Cash/Card")
  if Payment_Method == "Card":
    cardNum = int(input("What is your card number?"))
    print ("Your card number is " + str(cardNum) +".Thank you for paying.")
  else:
    print("Thank you for paying.")
  
  #Collection of items seperated by commas using hard brackets,
  #Indexed starting at zero
  couponAmountsList = [5,10,15,20,25]
  seniorDiscount = 0
  
  #This gives senior discounts based on the user's age
  if userAge >= 60 and userAge <= 69:
    seniorDiscount = couponAmountsList[0]
  elif userAge >= 70 and userAge <=79:
    seniorDiscount = couponAmountsList[1]
  elif userAge >= 80 and userAge <=89:
    seniorDiscount = couponAmountsList[2]
  elif userAge >= 90 and userAge <=99:
    seniorDiscount = couponAmountsList[3]
  elif  userAge >= 100:
    seniorDiscount = couponAmountsList[4]
    
  #This gives the senior discount message with amount
  print("You get a senior discount coupon of: $" + str(seniorDiscount))
    
  #Option to play again, breaks loop if other than yes selected
  print("")
  orderAgain = input("Would you like to play again yes/no ?: ")
  print(")")
  print(lineSeperator1)
  os.system("clear")
#Final Message
print("")
print("See you next time!")