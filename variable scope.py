#variable scope = мястото, в което една променлива бива разпозната
#                 променливата е достъпна само в мястото където е създадена
#                 Могат да бъдат създадени глобални и локални scope-ове на променливите

name = "Ivan"

def display_name():
    name = "Tsekov"
    print(name)

display_name()
print(name)
