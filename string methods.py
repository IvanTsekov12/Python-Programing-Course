name = "Ivan"

print(len(name))    #връща дължината на стринга
print(name.find("a"))   #връща индекса на който се намира даден символ от стринга
print(name.capitalize())    #прави първата буква в стринга главна
print(name.upper())     #прави целият стринг в главни букви
print(name.lower())     #прави целият стринг в малки букви
print(name.isdigit())   #връща дали стринга е число (True или False)
print(name.isalpha())   #връща дали стринга садържа само букви от английската азбика
print(name.count("a"))     #връща колко пъти даден символ се среща в стринга
print(name.replace("a", "o"))   #заменя символ от стринга с друг символ
print(name * 3)     #изписва стринга n на брой пъти, долепен един до друг