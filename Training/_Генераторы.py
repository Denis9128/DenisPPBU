from functools import reduce

l = [22,22,44]
l1 = [2,3,4]

def gen():
    i =0
    while i < 3:
        i += 1
        yield i


# res= gen()
# print(res)
# print('1', next(res))
# print('2', next(res))
# print('3', next(res))
#
# for i in res:
#     print(i)
#
# for i in res:
#     print(i)

res= map (lambda n,m: n>m, l,l1)
print(list(res))

res = filter(lambda n: n%2 != 0, l1)
print(list(res))

city = ('у','ф','а','-',4,5)
#print(''.join(city))
res = reduce(lambda x,y:str(x) + str(y), city)
print(res)

