#exception = събития засечени по време на изпълнението, които прекъсват нормалното
#            протичане на програмата

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero dumbass!!!")
except ValueError as e:
    print(e)
    print("Enter only WHOLE numbers")
else:
    print(result)
finally:        #винги се изпълнява без значение дали има или няма грешка
    print("This will always execute!")