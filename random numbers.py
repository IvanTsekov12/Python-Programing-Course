import random

x = random.randint(1, 6)
y = random.random()
rpc = ['rock', 'paper', 'scissors']
z = random.choice(rpc)
card =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
random.shuffle(card)

print(x)
print(y)
print(z)
print(card)