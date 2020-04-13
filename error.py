n = int(input())
array = []
sum = 0

for i in range(0, n):
    a, b = map(int, input().split())
    array.append(int(a)*int(b))
    sum += a*b

for i in array:
    print(i/sum)
