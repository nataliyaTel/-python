#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите положительное целое число N: '))
list=[]
for i in range(1,9):
    if n%i == 0 and i!=4 and i!=6 and i!=8:
        list.append(i)
print(list)        