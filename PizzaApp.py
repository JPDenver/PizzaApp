#PizzaApp
#An app that keeps track of the price while you add toppings to a pizza of a certain size

# I need to add up the price throughout so I think I should set a global price value
global price


# I'll keep it simple like its a kiosk and it just needs your name
def getordername():
    global ordername
    ordername = input("\nWhat is the name for the order: ")
    ordername=str(ordername)

#Then usually it would as you for the size first
def getsize():


    global size
    global price
    #This is the list with the sizes and prices
    size = input("\nOK, " + ordername + " What size pizza would you like "
                                      "\n\n Small - 12 inches, $12"
                                      "\n Medium - 14 inches, $14 "
                                      "\n Large - 16 inches, $16"
                                      "\n\n Enter Selection Here: ")
   #This is where the input is accepted and converted into the corresponding price as an integer
    if size == "Large":
        print("\n\nOK, " + ordername + " next we're going to add toppings to your " +size + " pizza: ")
        price = int(16)
    elif size == "Medium":
        print("\n\nOK, " + ordername + " next we're going to add toppings to your " + size + " pizza: ")
        price = int(14)
    elif size == "Small":
        print("\n\nOK, " + ordername + " next we're going to add toppings to your " + size + " pizza: ")
        price = int(12)
    #Incase the user input is invalid
    else:
        print("\n\nThat wasn't an option, please try again!")
        getsize()


#Then it will add some toppings

def getmeats():
    global meats
    global price
    #Pricestring is to convert the price to a string just to be able to print it
    #because you can not concatenate integers
    pricestring = str(price)
    global size


    #To show that the price is correct so far
    print("So far your pizza costs " +pricestring+" and each additional topping will cost extra!")
    #This is the list and prices of toppings
    meats = input("\n Let's add some meats, here are your choices"
          "\n\n   Pepperoni - $3"
          "\n   Sausage - $2"
          "\n   Ham -$1"
          "\n\n   Enter your selection here: ")
    #Taking the user input and doing the same thing as before but adding the amount
    #existing global price value
    if meats == "Pepperoni":
        price = price + 3
    elif meats == "Sausage":
        price = price + 2
    elif meats == "Ham":
        price = price + 1
    else:
        print("\n\nNot a valid choice, please select again.")
        getmeats()
    extrameats()

#The user has the option to choose more than one meat and it will continue to add prices
def extrameats():
    global price
    global meats
    #I'd like to find out how to get this to handle typos and case issues.
    extrameats = input("\n Great Choice! Would you like any other or extra meats (Yes or No) ?: ")
    if extrameats == "Yes":
        getmeats()
    if extrameats == "no":
        print("Great Choice! How about some veggies also?")
        return

#Copied the meat process but used vegetables
def getveggies():
    global price
    veggies = input("\n Ok, Let's add some veggies, here are your choices"
          "\n\n   Mushorooms - $2"
          "\n   Onions - $1"
          "\n   Peppers - $.50"
          "\n\n   Enter your selection here: ")
    if veggies == "Mushrooms":
        price = price + 2
    elif veggies == "Onions":
        price = price + 1
    elif veggies == "Peppers":
        price = price + .5
    else:
        print("\n\nNot a valid choice, please select again.")
        getveggies()
    extraveggies()

def extraveggies():
    global price
    global veggies
    extraveggies = input("\n Would you like any other or extra veggies?: ")
    if extraveggies == "Yes":
        getveggies()
    if extraveggies == "no":
        print("Great Choice! That will complete your order")
        return


#combining functions to make the complete process
def orderpizza():
    getordername()
    getsize()
    getmeats()
    getveggies()





orderpizza()
pricestring = str(price)
print("\n\nThank you for your order, " + ordername + " You're pizza will cost "+pricestring)
