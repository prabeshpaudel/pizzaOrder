from copy import deepcopy
name = input("Enter your name ")

# Check If Provided Number of Pizza is an integer, if not, keep on asking until a valid integer is given
while True:
    numberofPizza = input("\nHello, "+name+"!\nHow many pizza do you want?\n")
    if numberofPizza.isdigit() and int(numberofPizza)>0:
        break
    else:
        print("Please enter a valid number! \n")
pizzas = []
cheese = []
topping = []
crust = []
crust_price = {'Thin':'4.0','Thick':'6.5','Wood Fired':'8.5'}
topping_price = {'Tomato': '0.75',
                 'Mushrooms': '0.75',
                 'Pepperoni': '0.50',
                 'Onions': '0.25',
                 'Black Olives': '0.75',
                 'Green Peppers': '0.50',
                 'Anchovies': '0.25',
                 'Garlic' : '0.50',
                 'Ham' : '1.50',
                 'Bacon': '1.25'}

for i in range(int(numberofPizza)):
    # Check If provided crustType is a among the valid ones,if not, keep on asking until a valid number is provided
    while True:
        crustType = input("For Pizza Number "+str(i+1)+"\nEnter Crust Type:\nChoose from :"
                          "\n1.Thin"
                          "\n2.Thick"
                          "\n3.Wood Fired\n")
        if crustType in crust_price:
            break
        else:
            print("Invalid Crust Type Entered, Please choose from available crust types \n\n\n")
    crust.append(crustType)

    # Cheese amount should be an integer less than or equal to 3
    while True:
        cheese_amount = input("How many cheese?\n")
        if cheese_amount.isdigit() and 1 <= int(cheese_amount) <= 3:
            break
        else:
            print("Cheese amount should be from 1 to 3 ")

    # We want to get every cheese styles
    for j in range(int(cheese_amount)):
        # Check if cheese_style being provided is among the valid options
        while True:
            cheese_style = input("\n\nFor cheese Number "+str(j+1)+"\n\nEnter cheese Style\n\nYou have to choose from: "
                                 "\n1.Cheeder\n"
                                 "2.Colby\n"
                                 "3.Edam\n"
                                 "4.Emmental\n"
                                 "5.Gruyere \n"
                                 "6. Mozzarella\n"
                                 "7. Provolone\n"
                                 "8. Ricotta\n")
            if cheese_style in ['Cheeder','Colby', 'Edam','Emmental','Gruyere','Mozzarella','Provolone','Ricotta']:
                break
            else:
                print("Please Choose From available cheese_style only!\n\n\n")
        cheese.append(cheese_style)

    while True:
        # Check for the amount of topping, which must be a valid integer from 1 to 6
        topping_amount = input("Enter number of Topping\n")
        if topping_amount.isdigit() and 1 <= int(topping_amount) <= 6:
            break
        else:
            print("Please provide a number from 1 to 6!\n")

    for k in range(int(topping_amount)):
        # Need to check if given topping type is among the valid options
        while True:
            topping_choice = input("For topping number "+str(k+1)+
                                   "\n1. Tomato "
                                   "\n2. Mushrooms"
                                   "\n3.Pepperoni"
                                   "\n4.Onions"
                                   "\n5.Black Olives"
                                   "\n6.Green Peppers"
                                   "\n7.Anchovies"
                                   "\n8. Garlic"
                                   "\n9.Ham"
                                   "\n10.Bacon\n")
            if topping_choice in topping_price:
                break
            else:
                print("Please choose from available Topping types only!\n\n\n")
        topping.append(topping_choice)
    # Add crust, cheese,topping to make a pizza
    # deepcopy is used to pass arrays by value
    pizzas.append([deepcopy(crust),deepcopy(cheese),deepcopy(topping)])
    # clearing is need in case of 2 or more pizzas
    crust.clear()
    cheese.clear()
    topping.clear()
print("\n\nOrder Summary for Mr./Mrs/Miss "+name+"\n\n")

price = 0
for i, pizza in enumerate(pizzas):
    print("-------------------------For Pizza number : "+str(i+1)+" ------------------------------------------\n")
    crust_name = pizza[0][0]
    print("Crust Type: "+crust_name+"\tPrice = " + crust_price.get(crust_name)+"\n\n")
    price += float(crust_price.get(crust_name))

    print("Cheese:\n")

    # Add price for each cheese

    for j, cheese_ in enumerate(pizza[1]):
        print("Cheese "+str(j+1)+" : "+cheese_+"\tPrice = 5.0")
        price += 5.0
    print('\n\nTopping:\n')

    # Add price for each Topping

    for k, topping_ in enumerate(pizza[2]):
        print("Topping "+str(k+1)+" : "+topping_+"\tPrice = "+topping_price.get(topping_)+"\n\n")
        price += float(topping_price.get(topping_))

print('\n\n----------------------------\n\nTotal Price =  ' + str(price)+'\n\n----------------------------------')



