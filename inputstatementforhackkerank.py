#The first line of input contains the space separated values of m and n .
#The next n lines contains m space separated integers.


m, n = map(int, input().split())
arrays = []
for _ in range(n):
    row = list(map(int, input().split()))
    arrays.append(row)