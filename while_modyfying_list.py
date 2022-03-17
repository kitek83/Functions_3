#Starts with some designs thet need to be printed.
unprinted_designs = ['phones case','robot pendant','dodecahedron']
completed_designs = []

while unprinted_designs:
    #printing desig
    current_design = unprinted_designs.pop()
    print(f'Printing the design: {current_design}')
    completed_designs.append(current_design)

print(f'The following designs have been printed: ')
for design in completed_designs:
    print(design)