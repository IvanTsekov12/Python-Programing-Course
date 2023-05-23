temp = float(input("What is the temperature?: "))

#AND operator
if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("Go outside!")
#OR operator
elif temp < 0 or temp > 30:
    print("The temperature is bad today!")
    print("Stay inside!")
#NOT operator
if not(temp >= 0 and temp <= 30):
    print("The temperature is bad today!")
    print("Stay inside!")
elif not(temp < 0 or temp > 30):
    print("The temperature is good today!")
    print("Go outside!")