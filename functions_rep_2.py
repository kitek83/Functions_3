def make_pizza(*toppings):
    print('Pizza has the following toppings: ')
    for topping in toppings:
        print(f'-{topping}')

make_pizza('pepperoni')
print()
make_pizza('mushrooms','ham','green peppers','extra cheese')
print()

def make_pizza2(size,*toppings):
    print(f'This {size} inch pizza has the following toppings: ')
    for topping in toppings:
        print(f'-{topping}')

make_pizza2(16,'pepperoni')
print()
make_pizza2(22,'extra chesse','ham','extra bacon','mushrooms')
print()
print('-------------------------------------------')
def person_info(name,surname,**infos):
    infos['firs_name'] = name
    infos['surname'] = surname
    return infos

user1 = person_info('Kris','Kozak',
            location='Szczecin',
            field='programming')
print(user1)


