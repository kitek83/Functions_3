def greet_user(username):
    print(f'Hello {username.title()}!!')

greet_user('jack')
greet_user('amanda')

print(3*'----------------')
names = ['Kris','Alan','Becky','Kate']
for name in names:
    greet_user(name)