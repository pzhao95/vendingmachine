# assignment: programming assignment 2
# author: Peter Wang Zhao
# date: October 11, 2021
# file: shop.py implements a vending machine
# input: numbers (integers)
# output: interactive messages (strings)


import math
print("Vending Machine")
while True:
    # step 1: print the menu and get the user's choice
    print("Please enter what product you want to buy[1-3] or select quit[4]:")
    print("1. A bottle of water - $1.99")
    print("2. A bottle of orange juice - $2.15")
    print("3. A bottle of ice tea - $2.49")
    print("4. Quit")
    # step 2: depending on the user's choice,
    choice=input()
    # update product_price and product_name (the variables that keep track of the user's choice),
    # quit the program, or reprint the menu
    # step 3: ask for deposit

    if choice=="1":
        buy="You bought a bottle of water."
        product_price=1.99
    elif choice=="2":
        buy="You bought a bottle of orange juice."
        product_price=2.15
    elif choice=="3":
        buy="You bought a bottle of ice tea."
        product_price=2.49
    elif choice=="4":
        print("Goodbye!")
        break
    else:
        print("You made a wrong choice!")
        continue
    total=0
    while True:
        print("Please deposit money (in cents):")
        deposit=int(input())
        total=total+deposit
        if total>=product_price*100:
            break



    # step 4: calculate change, we use the greedy algorithm written below to get the minimum number of coins:
    change=math.ceil(total-product_price*100)
    dollars = change // 100   # get the quotient Quotient - Wikipedia (Links to an external site.)
    change = change % 100     # get the remainder Remainder - Wikipedia (Links to an external site.)
    quarters = change // 25
    change = change % 25
    dimes = change // 10
    change = change % 10
    nickels = change // 5
    change = change % 5
    cents = change
    # step 5: print the selected product and change
    print(buy)
    if change!=0:
        print("Your change is: ")
    if dollars!=0:
        print("Dollars - %d"%dollars)
    if quarters!=0:
        print("Quarters - %d"%quarters)
    if dimes!=0:
        print("Dimes - %d"%dimes)
    if nickels!=0:
        print("Nickels - %d"%nickels)
    if cents!=0:
        print("Cents - %d"%cents)

