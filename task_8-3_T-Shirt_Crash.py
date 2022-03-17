def make_shirt(size,message):
    print(f'The size of the t-shirt is: {size}.')
    print(f'Message on the t-shirt: {message.title()}.')

make_shirt('xl','I like Python')
print()
make_shirt(size='xxl',message='I like Java')
print(3*'---------------------')
print('Return function.')

def get_formatted_name(first_name,last_name):
    name = (f'{first_name} {last_name}').title()
    return name
musician = get_formatted_name('John','Kozak')
print(musician)