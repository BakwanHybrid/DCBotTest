import random

ch = "~!@#$%&*_-+QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm"
ln = int(input("Password length:"))
pw = " "
for i in range(ln):
    pw += random.choice(ch)
    print(pw)
