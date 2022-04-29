from resources import MENU, resources
profit=0

def report():
    for k,v in resources.items():
        print(f"{k}: {v}")

def sufficient(order):
    for item in order:
        if order[item]> resources[item]:
            print("Sorry, there is not enough {item}.")
            return False
    return True

def total():
    print("Please insert coins.")
    total = int(input("How many quartes?: "))*0.25
    total += int(input("How many dimes?: "))*0.10
    total += int(input("How many nickels?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total

def sucessful(money, drink):
    if money>=drink:
        change= round(money- drink, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit+= drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
