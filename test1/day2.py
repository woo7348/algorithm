# BOJ 2750
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

n = int(input())
array = list()
for i in range(n):
    array.append(int(input()))

array.sort()

for i in array:
    print(i)