def build_profile(first,last,**user_info):
    #Building dictionary containing everything we know about user
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert','einstein',location='princenton',
              field='physics',pets='cat')

print(user_profile)
print()

for key, value in user_profile.items():
    print(f'{key}: {value.title()}')