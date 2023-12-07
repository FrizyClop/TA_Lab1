import random

f = open('StartFile2.txt','w')

print("Введите минимальное число в списке: ")
min = int(input())
print("Введите максимальное число в списке: ")
max = int(input())
print("Введите количество чисел в списке: ")
count = int(input())

while(count > 0):
    count = count - 1
    f.write(str(random.randint(min,max)) + '\n')

print('Файл создан!')
f.close