def make_pizza(size,*toppings):
    print(f'You ordered the {size} inches pizza with the following toppings: ')
    count = 0
    for topping in toppings:
        count += 1
        print(f'{count}.{topping.title()}')
