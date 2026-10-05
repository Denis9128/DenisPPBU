# n = int(input("> "))
# sm=10
# cnt = 0
# while n!=0:
#     sm += n
#     cnt += 1
#     n = int(input("> "))
# print(sm)
# print(cnt)

n = int(input("> "))
nn = n
sm = 0
cnt = 0
while n>0:
    rem = n%10
    sm+=rem
    cnt += 1
    n = n // 10
print(f'В числе "{nn}" {cnt} ц. суммой {sm}')