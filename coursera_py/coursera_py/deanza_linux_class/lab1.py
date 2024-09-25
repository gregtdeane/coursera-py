# Name: Gregory Tuayev-Deane
# Summary: Write a program that mimics what a typical cash register transaction might look like.

import math

#1
price_1 = float(input("Enter the price of your first item: "))
price_2 = float(input("Enter the price of your second item: "))
price_3 = float(input("Enter the price of your third item: "))
#2
subtotal = price_1+ price_2+ price_3
print("Your subtotal is: ", subtotal)
#3
discounted_price = subtotal*0.9
print("Your subtotal after discount is: ", round(discounted_price,2))

total_after_tax = discounted_price*1.1
print("Your total after tax is: ", round(total_after_tax,2))

pmt_amt = float(input("Please enter the amount you wish to pay: "))

change = pmt_amt-total_after_tax
print("Your change is: ",round(change,2))

#Extra Credit
print("##############EXTRA CREDIT##########")
print("Your change is: ", int(change//1), " dollars and ",int(change%1 *100), "cents." )


