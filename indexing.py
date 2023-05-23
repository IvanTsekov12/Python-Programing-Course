#index оператор '[]' = дава достъп до елемент от поредица (стринг, списък(list), tuples)

name = "ivan Tsekov!"

#islower() - проверява дали даден елемнт от стринга (или целият стринг) е малка буклва.
#            Връща True или False
# if name[0].islower():
#     name = name.capitalize()

first_name = name[:4].upper()
last_name = name[5:].lower()
last_char = name[-1]
print(first_name)
print(last_name)
print(last_char)
