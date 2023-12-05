import time

def insertion_sort(ls):
    for i in range(1, len(ls)):
        temp = ls[i]
        j = i - 1
        while (j >= 0 and temp < ls[j]):
            ls[j + 1] = ls[j]
            j = j - 1
        ls[j + 1] = temp

f1 = open('StartFile2.txt', 'r')
f2 = open('EndFile2.txt', 'w')

ls = f1.readlines()
f1.close

ls2 = list(map(int,ls))

start_time = time.time()
insertion_sort(ls2)
end_time = time.time()

for i in ls2:
    f2.write(str(i) + "\n")
f2.close

print('Сортировка завершена! ' + str(end_time - start_time))