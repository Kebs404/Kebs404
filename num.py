number = 0
a = int(input())
while a != 0:
  number += a % 10
  a //= 10
print(number)
