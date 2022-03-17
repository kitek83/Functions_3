def my_pet(pet_type,pet_name):
    print(f'I have {pet_type}, which name is {pet_name.title()}')

my_pet('hamster','willy')
my_pet('dog','shagi')
print()

def formatted_name(first_name,last_name,middle_name=''):
    if middle_name: #if there is middle name
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name

musician1 = formatted_name('Kris','Kozak','Wladyslaw')
print(musician1)
print()

musician2 = formatted_name('Grzegorz','Kozak')
print(musician2)