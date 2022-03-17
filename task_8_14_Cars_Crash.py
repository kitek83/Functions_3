def make_car(manufacturer,model,**info):
    info['manufacturer'] = manufacturer
    info['model'] = model
    return info

car = make_car('Peguot','SW',color='black',type='combi',tow_package = True)
print(car)
