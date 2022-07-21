from math import pow as pw
from math import sqrt as sq
from random import choice as ch
from random import shuffle as shf
from random import randint as rand

result_1 = pw(2,4)
print("result_1 is ",result_1)

result_2 = sq(16)
print("result_2 is ",result_2)

result_3 = rand(0,100)
print("result_3 is ",result_3)

names = ["Amaryllis","Godson","Emily","Reina","Derin","Elena","Inarcio"]
print("Original names:", names)

shf(names)
print("Names after shuffling ", names)

result_4 = ch(names)
print("Chosen name is ",result_4)