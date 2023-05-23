#str.format() = метод, който дава на потрбителия повече контрол когато изкарва изход

# animal = "cow"
# item = "moon"

#print("The " + animal + " jumped over the " + item)

# print("The {} jumped over the {}".format(animal, item))
# print("The {0} jumped over the {1}".format(animal, item)) #positional formating(позиционно форматирене)
#print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))

# text = "The {} jumped over the {}"
# print(text.format(animal, item))

#name = "Ivan"

# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))
# print("Hello, my name is {:>10}. Nice to meet you".format(name))
# print("Hello, my name is {:^10}. Nice to meet you".format(name))
# print("Hello, my name is {0:^10}. Nice to meet you".format(name))

number = 3.14159
number2 = 1000

print("The number pi is {:.2f}".format(number))
print("The number is {:,}".format(number2)) #добавя запетая след хилядните
print("The number is {:b}".format(number2)) #binary(двоична бройна система)
print("The number is {:o}".format(number2)) #octale(осмична бройна система)
print("The number is {:X}".format(number2)) #hexa
