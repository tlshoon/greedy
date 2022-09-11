# 동전
"""n = 1260
count = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += n // coin
    n %= coin

print(count)"""

# 큰 수의 법칙
"""n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)"""

# 숫자 카드 게임
#1
"""n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = min(data)

    result = max(result, min_value)
print(result)"""

#2
"""n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = 10001

    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
print(result)"""


# 1이 될 때까지
"""n,k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)"""


######################## 3장 문제 ########################


# 모험가 길드
# n = int(input())
#
# fear = list(map(int, input().split()))
#
# fear.sort()
#
# result = 0 # 총 그룹의 수
# count = 0 # 현재 그룹의 인원 수
#
# for horror in fear:
#     count += 1  # 현재 그룹의 인원 추가
#     if (count >= horror):
#         result += 1
#         count = 0
#
# print(result)

# 곱하기 혹은 더하기
# s = list(map(int,input()))
#
# result = s[0]
#
# for i in range(1, len(s)): # 두번째 정수부터 탐색 시작
#     if(s[i] <= 1 or result <= 1):
#         result += s[i]
#     else:
#         result *= s[i]
# print(result)
