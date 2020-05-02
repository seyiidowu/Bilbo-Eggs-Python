#This program helps to calculate the bill for the number of eggs to be purchased by user
#
#Author: Seyi Idowu
#        27-Jan-2020
#
#Description: this python program calculates the bill for Bilbo's wholesale
#
#Input values is the number of eggs to be purchased

egg_number = int(input("How many eggs do you like to purchase?: "))

# calculate the cost of each egg

if (egg_number >= 0) and (egg_number <= 47) :
    egg_cost = 0.50/12
    print("your cost is ${:.3f} per egg".format(egg_cost))
elif (egg_number >= 48) and (egg_number <= 71) :
    egg_cost = 0.45/12
    print("your cost is ${:.3f} per egg".format(egg_cost))
elif (egg_number >= 72) and (egg_number <= 131) :
    egg_cost = 0.40/12
    print("your cost is ${:.3f} per egg".format(egg_cost))
else :
    egg_cost = 0.35/12
    print("your cost is ${:.3f} per egg".format(egg_cost))

#calculate bill for the total number of eggs

total_bill = egg_number * egg_cost
print("Your bill comes to ${:.2f}".format(total_bill))
    
