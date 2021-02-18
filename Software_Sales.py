### calculates a discount based off of the ammount purchased ###

#DRIVER: Tianna Davis (U69901851)
#NAVIGATOR: Peyton Krimmel (U85951028)


quantity = int(input("How many packages did you purchase? \n"))
PRICE = 99.00
#function to do all the calculations so i dont have to repeat code 5 times
def calculate(discount):
    calculate.subtotal = quantity * PRICE
    calculate.percent = discount * 100
    calculate.sales = calculate.subtotal * discount
    calculate.total = calculate.subtotal - calculate.sales

#for each quantity range, calls the calculate function with the corresponding discount input
if quantity < 10:
    calculate(0.00)
elif 10 < quantity < 20:
    calculate(0.10)
elif 20 <= quantity < 50:
    calculate(0.20)
elif 50 <= quantity < 100:
    calculate(0.30)
else:
    calculate(0.40)

#prints the results 
print("Discount Amount @ %{:,.0f}: ${:,.2f} \nTotal Amount: ${:,.2f}".format(calculate.percent, calculate.sales, calculate.total))
