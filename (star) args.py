#*args = параметър който събира всички аргументи в tuple
#        полезен за подаването на n на брой аргументи на функция

def add(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add(1, 2, 3, 4, 5, 6))