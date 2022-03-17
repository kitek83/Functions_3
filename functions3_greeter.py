def get_formatted_name(first_name,last_name):
    formatted_mame = f'{first_name} {last_name}'
    return formatted_mame.title()

while True:
    print('Enter Your first name or \'q\' to quit any time.')
    f_name = input('Enter Your name or \'q\':')
    if f_name == 'q':
        break
    l_name = input('Enter your last name or \'q\' to quit: ')
    if l_name == 'q':
        break

    print(f'Hello {get_formatted_name(f_name, l_name)}!')
