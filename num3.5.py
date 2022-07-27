# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
k = int(input('Введите число N: '))
res_list = []
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == -1:
        return 1
    elif n > 0:
        return fib(n-1)+fib(n-2)
    else:
        return fib(n+2)-fib(n+1)
    
for i in range(-k, k+1):
     res_list.append(fib(i))
print(res_list)



