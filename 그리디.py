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
# n,k = map(int, input().split())
# result = 0
#
# while n >= k:
#     while n % k != 0:
#         n -= 1
#         result += 1
#     n //= k
#     result += 1
#
# while n > 1:
#     n -= 1
#     result += 1
#
# print(result)


######################## 3장 문제 ########################


# 모험가 길드
# n = int(input())
#
# data = list(map(int,input().split()))
# data.sort()
#
# group_su = 0
# mohumga_su = 0
#
# for i in data:   # 현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도보다 크거나 같다면 그룹 결성
#     mohumga_su += 1
#     if mohumga_su >= i:
#         group_su +=1
#         mohumga_su = 0
#
# print(group_su)


# 곱하기 혹은 더하기
# data = input()
#
# result = int(data[0]) # 첫 번째 문자를 숫자로 변경하여 대입
#
# for i in range(1, len(data)):  # 1부터 시작
#     num = int(data[i])
#     if num <= 1 or result <=1:
#         result += num
#     else:
#         result *= num
# print(result)

# 문자열 뒤집기
# data = input()
#
# count0 = 0  # 전부 0으로 바꾸는 경우
# count1 = 0
#
# if data[0] == '1':
#     count0 += 1
# else:
#     count1 += 1
#
# for i in range(len(data)-1):
#     if data[i] != data[i+1]:
#         if data[i+1] == '1':
#             count0 += 1
#         else:
#             count1 += 1
#
# print(min(count0,count1))

# 만들 수 없는 금액
# n = int(input())
# data = list(map(int,input().split()))
# data.sort()
#
# target = 1
# for i in data:
#     if target < i:
#         break
#     cnt += i  # 목푯값 갱신
#
# print(target)


# 볼링공 고르기

# 무지의 먹방 라이브