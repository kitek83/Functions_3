def pizza(size,*toppings):
    print(f'You ordered pizza size {size} inches with the following toppings:')
    count = 0
    for topping in toppings:
        count += 1
        print(f'{count}.{topping}')

pizza(20,'pepperoni')
print()
pizza(30,'mushrooms','green peppers','extra cheese')