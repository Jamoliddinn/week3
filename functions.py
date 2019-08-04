# functions 
# def greet_user():
#     """greeting the user """
#     print("Hello!!!")
# greet_user()

#execution
# greet_user()
# greet_user()

# defining the function (not executed unless you call the function)
# def greet_user(name):
#     """greeting the user """
#     print(f"Hello, {name.title()}!!!")
# greet_user('akmal')
# greet_user('nurbek')

# def favourite_place(name, place):
#     """prints message with favourite place"""
#     print(f"{name.title()} loves the {place.title()}. ")

# favourite_place('john', 'barselona')

def favourite_places(name, places):
    """prints message with favourite place"""
    for place in places:
        print(f"{name.title()} loves the {place.title()}. ")

favourite_places('john', ['barcelona', 'madrid', 'london'])


def sum_of_numbers (number1, number2):
    # pass # do nothing 
    return number1 + number2
new_num = sum_of_numbers(15, 20)
print(new_num)
