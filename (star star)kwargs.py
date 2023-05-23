#**kwargs = параметър, който ще събере всички аргументи в библиотека(dictionary)
#           полезен, функцията да приема n на брой keyword аргументи

def hello(**kwargs):
    #print(f"Hello {kwargs['first']} {kwargs['last']}")
    print("Hello,", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello(first="Ivan",second = "- Petar", middle="Iliyanov" , last="Tsekov")