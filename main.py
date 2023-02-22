from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_m = CoffeeMaker()
money_m = MoneyMachine()

#asks for user input and starts the
def user_input():
    print("What kind of coffee would you like to have?")
    print(menu.get_items())
    u_i = input()
    if u_i == "report":
        coffee_m.report()
        money_m.report()
        return True
    else:
        order = menu.find_drink(u_i)
        while order is None:
            print("Would you like a different item?")
            print(menu.get_items())
            u_i = input()
            if u_i == "no":
                print("Goodbye")
                return False
            order = menu.find_drink(u_i)
        return order


def cont_service(order):
    if order is True:
        u_i = input("Can I help you with anything else? yes/no ")
        if u_i == "no":
            print("Goodbye")
            return False
        return True


def start():
    on = True

    print("Good morning!")
    while on:
        order = user_input()
        if cont_service(order) is False:
            return
        elif order is True:
            continue
        if coffee_m.is_resource_sufficient(order):
            if money_m.make_payment(order.cost):
                coffee_m.make_coffee(order)
                if cont_service(True):
                    continue
        else:
            if not cont_service(True):
                return
    return


start()
