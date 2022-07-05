#2 максимальных числа без перебора выборки

n = int(input())

max1 = 0
max2 = 0

for i in range(n):
  num = int(input())
  if num > max1:
    max2 = max1
    max1 = num
  elif num > max2 and num < max1:
    max2 = num
print(max1, max2, sep="\n")