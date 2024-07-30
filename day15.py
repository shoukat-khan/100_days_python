#coffe machine project

resourses ={
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

menu = {
     "Latte":{
        "water":200,
        "coffee":24,
        "milk":150,
        "price":2.5,
    },
        "Expresso":{
        "milk":0.0,
        "water":50,
        "coffee":18,
        "price":1.5,
    },
     "Cappuccina":{
        "water":250,
        "coffee":24,
        "milk":100,
        "price":3.0
    }
}

def check_resourses(order):
    for item in resourses:
        if order[item] >= resourses[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


#testing the check_resourses function
order = menu["Latte"]
print(check_resourses(order))

def process_coins():
    print("Please insert coins")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.10
    total += int(input("How many nickles?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total

def transaction_successful(money, cost):
    if money >= cost:
        change = round(money - cost, 2)
        if change > 0:
            print(f"Here is your change {change}")
        else:
            print("thanks for chosing us")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False
    
def make_coffee(order):
    for item in resourses:
        resourses[item] -= order[item]
    print(f"Here is your {order} ☕️. Enjoy!")


def coffee_machine():
    profit=0
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            break
        elif choice == "report":
            print(profit)
            print(resourses)
        else:
            order = menu
            if check_resourses(order):
                payment = process_coins()
                if transaction_successful(payment, order["price"]):
                    profit += order["price"]
                    make_coffee(order)

coffee_machine()







