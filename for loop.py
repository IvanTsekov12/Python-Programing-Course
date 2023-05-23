import time

#цифров range

for i in range(10 + 1): # default стъпка 1
    print(i)

for i in range(50, 100 + 1, 2): # със стъпка
    print(i)

# текст range
for i in "Ivan Tsekov":
    print(i)

# таймер
for seconds in range(10, 0, -1): #отрицателна стъпка --> брои назад
    print(seconds)
    time.sleep(1)
print("Happy New Year")