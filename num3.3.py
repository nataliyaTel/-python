#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением
#  дробной части элементов.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

def get_list ( n,start, end):
    return [round(uniform(start,end), 2) for i in range(n)]

def diff(delta):
    num = [round(x - int(x), 2) for x in (delta)]
    return max(num) - min(num)
n = 5
start = 1
end = 20
res_list = get_list(n, start, end)
print (res_list)
print(diff(res_list))

