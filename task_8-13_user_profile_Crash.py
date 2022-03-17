def build_user(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last name'] = last
    return user_info
    print()

user_data = build_user('Kris','Kozak',location='Szczecin',country='Poland',
                       height='180cm',weight='120kg')

print(user_data)
print()

for key, val in user_data.items():
    print(f'{key}: {val}')