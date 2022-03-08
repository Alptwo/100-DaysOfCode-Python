from tarfile import is_tarfile


resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200,
    "money": 2.5
    }

def check_for_resources(order):

    is_there_enough_resources = False

    water = resources.get("water")
    coffee = resources.get("coffee")
    milk = resources.get("milk")
    
    if(order == "latte"):
        if(water >=200 and coffee >=24 and milk >= 150):
            is_there_enough_resources = True
            return is_there_enough_resources
        else:
            if(water < 200):
                print("Sorry there is not enough water")
                return is_there_enough_resources
            elif(coffee < 24):
                print("Sorry there is not enough coffee")
                return is_there_enough_resources
            elif(milk < 150):
                print("Sorry there is not enough milk")
                return is_there_enough_resources
    elif(order == "espresso"):
        if(water >=50 and coffee >=18):
            is_there_enough_resources = True
            return is_there_enough_resources
        else:
            if(water < 50):
                print("Sorry there is not enough water")
                return is_there_enough_resources
            elif(coffee < 18):
                print("Sorry there is not enough coffee")
                return is_there_enough_resources
    elif(order == "cappuccino"):
        if(water >=250 and coffee >=24 and milk >= 100):
            is_there_enough_resources = True
            return is_there_enough_resources
        else:
            if(water < 250):
                print("Sorry there is not enough water")
                return is_there_enough_resources
            elif(coffee < 24):
                print("Sorry there is not enough coffee")
                return is_there_enough_resources
            elif(milk < 100):
                print("Sorry there is not enough milk")
                return is_there_enough_resources
    else:
        print("There is no such item!")
        return is_there_enough_resources

def process_coins(num_of_pennies, num_of_nickels, num_of_dimes, num_of_quarters):
    total_of_pennies = (float(num_of_pennies) / 100)
    total_of_nickels = ((float(num_of_nickels) * 5) / 100)
    total_of_dimes = (float(num_of_dimes) / 10)
    total_of_quarters = ((float(num_of_quarters) * 0.25))
    total_money_inserted_in_machine =  total_of_pennies + total_of_nickels + total_of_dimes + total_of_quarters
    return total_money_inserted_in_machine

def transaction_successful(total_money_inserted, order):
    money_in_machine = resources.get("money")
    returned_money = 0
    is_transaction_successful = False
    if(order == "latte"):
        if(total_money_inserted >= 2.5):
            is_transaction_successful = True
            if(total_money_inserted > 2.5):
                returned_money = total_money_inserted - 2.5
                print(f"Here is {returned_money} dollars in change.")
                resources.update({"money": money_in_machine + total_money_inserted - (2.5)})
                return is_transaction_successful
            else:
                resources.update({"money": money_in_machine + total_money_inserted})
                return is_transaction_successful
        else:
            is_transaction_successful = False
            print("Sorry that's not enough money. Money refunded.")


    elif(order == "espresso"):
        if(total_money_inserted >= 1.5):
            is_transaction_successful = True
            if(total_money_inserted > 1.5):
                returned_money = total_money_inserted - 1.5
                print(f"Here is {returned_money} dollars in change.")
                resources.update({"money": money_in_machine + total_money_inserted - (1.5)})
                is_transaction_successful = True
            else:
                resources.update({"money": money_in_machine + total_money_inserted})
                is_transaction_successful = True
        else:
            is_transaction_successful = False
            print("Sorry that's not enough money. Money refunded.")

    elif(order == "cappuccino") :
        if(total_money_inserted >= 3):
            is_transaction_successful = True
            if(total_money_inserted > 3):
                returned_money = total_money_inserted - 3
                print(f"Here is {returned_money} dollars in change.")
                resources.update({"money": money_in_machine + total_money_inserted - (3)})
                is_transaction_successful = True
            else:
                resources.update({"money": money_in_machine + total_money_inserted})
                is_transaction_successful = True
        else:
            is_transaction_successful = False
            print("Sorry that's not enough money. Money refunded.")

def make_coffee(order):
    water = resources.get("water")
    coffee = resources.get("coffee")
    milk = resources.get("milk")
    
    if(order == "latte"):
        resources.update({"water": water-200})
        resources.update({"coffee": coffee-24})
        resources.update({"milk": milk-150})
    elif(order == "espresso"):
        resources.update({"water": water-50})
        resources.update({"coffee": coffee-18})
    elif(order == "cappuccino"):
        resources.update({"water": water-250})
        resources.update({"coffee": coffee-24})
        resources.update({"milk": milk-100})
    print(f"Here is your {order}. Enjoy!")
        

order = input("What would you like? (Espresso, latte or cappuccino)\n")

while(order != "off"):

    if(order == "report"):
        print(resources)
    
    is_there_enough_resources = check_for_resources(order)

    if(is_there_enough_resources):
        num_of_pennies = int(input("How many pennies:"))
        num_of_nickels = int(input("How many nickels:"))
        num_of_dimes = int(input("How many dimes:"))
        num_of_quarters = int(input("How many quarters:"))

        total_money_inserted = process_coins(num_of_pennies, num_of_nickels, num_of_dimes, num_of_quarters)

        is_transaction_successful = transaction_successful(total_money_inserted,order)

        if(is_transaction_successful):
            make_coffee(order)















    order = input("What would you like? (Espresso, latte or cappuccino)\n")

