#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
n = int(input('Введите число: '))
li = [i for i in range(1,n+1)]
print(len(li))
def changed(li_n):
    count=1
    for i in range(n):
        count = li_n[i]*count
        li_n[i]=count
    return li_n
print(changed(li))
