#keyword arguments = аргументи предшествани от идентификатор, когато ги подадем на функция
#                    Подредбата на аргументите е без значение, не както при позиционните аргументи
#                    Програмата знае имената на аргументите, които функцията получава

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

hello(middle="Iliyanov", last="Tsekov", first="Ivan")