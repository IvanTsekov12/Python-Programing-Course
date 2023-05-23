#контроли за управление на цикли = променя изпълнението на цикъла от обикновеното

# break = прекратява изпълнението на цикъла
#continue = пропуска настоящата итерация на цикъла
#pass = не прави нищо, подава команда за да не изкара грешка в цикъла

#break
while True:
    name = input("Enter your name: ")
    if name != "":
        break

#continue
phone_number = "087-601-6444"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
print()
#pass
for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)