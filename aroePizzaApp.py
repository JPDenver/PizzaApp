##make sure to use with python3
import sys
price = 0

toppings = {
    'mushrooms': .5,
    'onions': .5,
    'pepperoni': 1,
    'extra-cheese':1
}

pizzaSize = {
    'small': 8,
    'medium': 10,
    'large': 12,
    'x-large': 14

}

##If using python2 must use raw_input syntax below

order1 = input("Welcome to the pizza store what size pizza can we get for you (small, medium, large, or x-large): " )

order1List = order1.split() ##puts the order into a list
## add error handling/splitting for multiple inputs
for x in order1List:
    sizePrice = pizzaSize.get(x)
    if sizePrice != None:
        price = sizePrice
        print(price)

    else:
        print(f"What in the absolute fuck is  '{order1}' we don't have that, try again")
        sys.exit()

    #add handling that reverts back to order1 input without having to rerun the programHERE



order2 = input(f"Your current total is ${price}" "\n" "Would you like to order some toppings?" "\n" "We have mushrooms, onions, pepperoni, and extra-cheese: ")

orderList = order2.split()


# for topping in orderList:
for x in orderList:
    toppingsPrice = toppings.get(x)
    if toppingsPrice != None:
        price += toppingsPrice
        print(f"Your total is ${price}")

    else:
        print(f"sorry we don't have {order2} try again")
