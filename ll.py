f = open('Perepis.txt', 'r')
date1 = int(input())
date2 = int(input())
summ = 0
for i in f:
    if int(i.split()[3].split('.')[2]) < 1978 :
        summ += 1
    if date1 < int(i.split()[3].split('.')[2]) < date2 :
        print(i)
print(summ)
