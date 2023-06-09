import random
str=input("What is your name?\n>")
print("Hello,",str,"!")
x=random.randrange(1,6,1)
y=random.randrange(1,6,1)
print("Rolling dice...")
print("Die 1:",x)
print("Die 2:",y)
print("Total value:",x+y)
