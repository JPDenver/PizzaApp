#PizzaApp
#An app that keeps track of the price while you add toppings to a pizza of a certain size

# I need to add up the price throughout so I think I should set a global price value
global price

#This is the variable to make a ticket for the completed order
ticket=[]
mods = []


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
    ticket.append(size)



#Then it will add some toppings

def getmeats():
    global meats
    global price
    #Pricestring is to convert the price to a string just to be able to print it
    #because you can not concatenate integers
    pricestring = str(price)
    global size


    #To show that the price is correct so far
    print("\nSo far your pizza costs " +pricestring+" and each additional topping will cost extra!")
    #This is the list and prices of toppings
    meats = input("\n Let's add some meats, here are your choices: "
          "\n\n   Pepperoni - $3"
          "\n   Sausage - $2"
          "\n   Ham -$1"
          "\n\n   Enter your selection here or enter None: ")
    #Taking the user input and doing the same thing as before but adding the amount
    #existing global price value
    if meats == "Pepperoni":
        price = price + 3
        ticket.append(meats)
        extrameats()
    elif meats == "Sausage":
        price = price + 2
        ticket.append(meats)
        extrameats()
    elif meats == "Ham":
        price = price + 1
        ticket.append(meats)
        extrameats()
    elif meats == "None":
        ticket.append("No meat")
        return
    else:
        print("\n\nNot a valid choice, please select again.")
        getmeats()




#The user has the option to choose more than one meat and it will continue to add prices
def extrameats():
    global price
    global meats
    #I'd like to find out how to get this to handle typos and case issues.
    extrameat = input("\n Great Choice! Would you like any other or extra meats (Yes or No) ?: ")
    if extrameat == "Yes":
        getmeats()
    if extrameat == "No":
        print(extrameat)
        print("\n Excellent Selections! Now how about some veggies also?")
        return
    else:
        print("\n\nNot a valid choice, please select again.")
        extrameats()

        



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
        ticket.append(veggies)
        extraveggies()
    elif veggies == "Onions":
        price = price + 1
        ticket.append(veggies)
        extraveggies()
    elif veggies == "Peppers":
        price = price + .5
        ticket.append(veggies)
        extraveggies()
    elif veggies == "None":
        return
    else:
        print("\n\nNot a valid choice, please select again.")
        getveggies()



def extraveggies():
    global price
    global veggies
    extraveggies = input("\n Would you like any other or extra veggies(Yes or No)?: ")
    if extraveggies == "Yes":
        getveggies()
    if extraveggies == "No":
        print("\n Great Choices! That will complete your pizza")
    else:
        print("\n\nNot a valid choice, please select again.")
        extraveggies()



def checkorder():

    print("\n")
    print(ticket)
    print(mods)
    orderok= input("\n Does your order look correct on the screen(Yes or No): ")
    if orderok == "Yes":
        pricestring = str(price)
        print("\n\nExcellent, Thank you for your order, " + ordername + " You're pizza will cost " + pricestring)
    if orderok == "No":
        pricestring = str(price)
        print("That sucks, If it was it would have cost " +pricestring)

def getmods():
    modifs = input("If you have any special modifications or instructions please enter them here: ")
    mods.append(modifs)


def getwings():
    wingsize = input("Would you like to add 6 or 12 wings: ")
    if wingsize == "6":
        ticket.append("6 wings")
        return
    if wingsize == "12":
        ticket.append("12 Wings")
        return
    else:
        print("Sorry please try again.")
        getwings()


#combining functions to make the complete process
def orderpizza():
    getordername()
    getsize()
    getmeats()
    getveggies()
    getmods()
    getwings()
    checkorder()







orderpizza()





