#Вычислить число c заданной точностью d.
#Пример:
#при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
from math import acos
from unicodedata import name
def isdigit(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

while True:
    n = str(input('Введите число n: \n'))
    if isdigit(n):
        b = int(n)
        break
    else:
        print('Некорректный ввод. Повторите')

def printValueOfPi(n) :
    b = '{:.' + str(n) + 'f}'
    pi = b.format(2 * acos(0.0))
    print(pi)
if name== "main":
    printValueOfPi(n)