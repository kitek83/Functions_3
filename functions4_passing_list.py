def greet_user(names):
    for name in names:
        msg = f'Hello {name}!'
        print(msg)

usernames = ['Kris','Jack','Kate']
greet_user(usernames)