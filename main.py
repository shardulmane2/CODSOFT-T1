import random
letters=['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
cap_lets=['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
symb=['!','@','#','$','%','^','&','*']
numb=['1','2','3','4','5','6','7','8','9','0',]


nam=input("What is your  name?\n")
print(f"Welcome to the Password Generator {nam}!!\n")

name_chars=list(nam)
for char in name_chars:
    if char in letters:
        letters.remove(char)
    if char in cap_lets:
        cap_lets.remove(char)


noCL=int(input("Enter the number of Capital Letters you want in your password:"))
noL=int(input("Enter the number of Letters you want in your password:"))
noS=int(input("Enter the number of Symbols you want in your password:"))
noN=int(input("Enter the number of Numbers you want in your password:"))


pword_list=[]

for char in range(1,noCL+1):
    pword_list+= random.choice(cap_lets)
for char in range (1,noL + 1):
    pword_list += random.choice(letters)

for char in range(1, noS+1):
    pword_list += random.choice(symb)

for char in range(1,noN +1):
    pword_list += random.choice(numb)


random.shuffle(pword_list)
Password=""
for char in pword_list:
    Password+=char



print(f"Here is the your password {nam}:\n",Password)
