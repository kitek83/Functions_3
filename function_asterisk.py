def pizza(*toppings):
    return toppings

print(pizza('pepperoni'))
print()
print(pizza('mushrooms','green peppers','extra cheese'))
print(3*'--------------------')

toppings = pizza('ham','extra cheese','beef')
for topping in toppings:
    print(topping)
print(len(toppings))
print()

for i in range(len(toppings)):
    print(toppings[i])
