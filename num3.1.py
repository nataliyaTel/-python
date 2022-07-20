#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
list = [4, 8, 5, 10, 5, 7, 9]
print(list)
list_length = len(list)
sumOfElements = 0
count = 1
while count < list_length:
    sumOfElements = sumOfElements + list[count]
    count = count + 2
print("Сумма элементов,стоящих на нечётной позиции:", sumOfElements)