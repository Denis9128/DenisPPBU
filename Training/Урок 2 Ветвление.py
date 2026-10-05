from math import * # импорт математических формул
a = 31
b = 43
c = 57

p = (a+b+c)/2
s = sqrt(p*(p-a)*(p-b)*(p-c))
print(round(s,5)) # 5 знаков после запятой
