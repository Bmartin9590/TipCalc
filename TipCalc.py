## WAP that calculates the tip on a bill. 
## The user enters a restaurant bill total. 
## The program should then display three amounts, 15% tip, 20% tip and a 25% tip
## 1. Create a print function greeting the user
    ## print("Hello! I am Tip Buddy, I would love to help you!")
## 2. Create an input function that asks the user to input the total amount of their bill
    ## billAmount = input("What was the total of your bill today?")
## 3. Convert the users input into float funtion so that entire number is used and the numbers after the decimal arent forgotten
    ## billAmount = float(billAmount)
## 4. Create a print function that uses the users input and incorporates an equation to calculate a 15% tip,
#       use float function so the cents isn't forgotten
    ## print("15% would be:", float(billAmount * .15))
## 5. Create a print function that uses the users input and incorporates an equation to calculate a 20% tip,
#       use float function so the cents isn't forgotten    
    ## print("20% would be:", float(billAmount * .20))
## 6. Run the program

print("Hello, I am Tip Buddy!")
billAmount = input("What was the total of your bill today? ")
billAmount = float(billAmount)

print("15% would be:", float(billAmount * .15))
print("20% would be:", float(billAmount * .20))
print("25% would be:", float(billAmount * .25))

