#nested function calls = повикване на функция в друга финкция
#                        най-вътршният метод се извиква пръв
#                        return value се използва като аргумент в следващата външна функция

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

print(round(abs(float(input("Enter a whole positive number: ")))))
