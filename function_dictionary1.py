def personal(first_name,last_name,age=None):
    #Return a dictionary of information about person
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person


print(personal('Jack','Mencel'))
print(personal('Kris','Kozak',38))
