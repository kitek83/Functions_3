'''Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items
as the function call provides, and should print summary of the sandwich 
tha's bein ordered. Call function 3 times using diffrent number of arguments
each time'''

def make_sandwich(*toppings):
    print('You ordered the sandwich with following toppings:')
    count = 0
    for topping in toppings:
        count += 1
        print(f'{count}.{topping.title()}')
    print()

make_sandwich('ham','cocumber','pepper')
make_sandwich('salami','tomato','onion','extra cheese')
make_sandwich('egg','ham','cheese','toato','onion','mayonnaise')
