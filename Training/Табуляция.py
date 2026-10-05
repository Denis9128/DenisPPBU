import math

print("Число\tКвадратный корень\tКубический корень")
print("="*46)

for i in range(2,10):
    k =math.sqrt(i)
    k3 = i ** (i/3)
    print(f'{i:>5}\t {k:>16.2f} {k3:>20.4f}') #:>16.2f -16 символов, 2 после запятой