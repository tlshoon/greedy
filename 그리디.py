# 동전
# n = 1260
# count = 0
#
# coin_type = [500, 100, 50, 10]
#
# for coin in coin_type:
#     count += n // coin
#     n %= coin
#
# print(count)

# 큰 수의 법칙
# n, m, k = map(int, input().split())
#
# data = list(map(int, input().split()))
#
# data.sort()
#
# first = data[n-1]
# second = data[n-2]
#
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1
#
# print(result)

# 숫자 카드 게임
#1
# n, m = map(int, input().split())
#
# result = 0
#
# for i in range(n):
#     data = list(map(int, input().split()))
#
#     min_value = min(data)
#
#     result = max(result, min_value)
# print(result)

#2
# n, m = map(int, input().split())
#
# result = 0
#
# for i in range(n):
#     data = list(map(int, input().split()))
#
#     min_value = 10001
#
#     for a in data:
#         min_value = min(min_value, a)
#     result = max(result, min_value)
# print(result)


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
#     target += i  # 목푯값 갱신
#
# print(target)

# 볼링공 고르기
# n, m = map(int,input().split())
# data = list(map(int,input().split()))
#
# array = [0] * 11  # 1부터 10까지의 무게를 담을 수 있는 리스트
#
# for x in data:
#     array[x] += 1  # 각 무개에 해당하는 볼링공의 개수 카운트
#
# result = 0
# # 1부터 m까지의 각 무게에 대하여 처리
# for i in range(1,m+1):
#     n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
#     result += array[i] * n  # B가 선택하는 경우의 수와 곱하기
#
# print(result)

# 무지의 먹방 라이브
# import heapq
#
# def solution(food_times, k):
#
#     # 전체 음식을 먹는 시간보다 네트워크 지연 시작 시간이 크거나 같다면 더 이상 먹을 음식이 없으므로 -1 출력
#     if (sum(food_times) <= k):
#         return -1
#
#     # 먹는 시간이 작은 음식부터 제거해야하므로 우선순위 큐를 사용
#     q = []
#     # 우선순위 큐에 (소요 시간, 음식 번호) 튜플을 삽입
#     for i in range(len(food_times)):
#         heapq.heappush(q, (food_times[i], i+1))
#
#     # 이전 음식 섭취까지 소요한 전체 시간
#     sum_time = 0
#     # 이전 음식의 섭취 시간
#     previous_time = 0
#     # 남은 음식 개수
#     length = len(food_times)
#
#     # [이전 음식 섭취까지 소요한 전체 시간 + 현재 음식을 섭취하기 위해 필요한 시간]이 K보다 커지면, 반복문 종료
#     # 현재 음식을 섭취하기 위한 시간은, (현재 음식 섭취 시간 - 이전 음식 섭취 시간) * 남은 음식 개수
#     while (sum_time + ((q[0][0] - previous_time) * length) <= k):
#         # 현재 음식을 우선순위 큐에서 제거하며, 현재 음식의 섭취 시간을 저장
#         now_time = heapq.heappop(q)[0]
#         # 현재 음식을 모두 섭취하기 위해 걸리는 시간을, 음식 섭취에 소요한 전체 시간에 추가
#         sum_time += (now_time - previous_time) * length
#         # 남은 음식 개수 감소
#         length -= 1
#         # 이전 음식 섭취 시간을 현재 음식 섭취 시간으로 변경
#         previous_time = now_time
#
#     # 반복문 종료 이후에는, K 발생까지 남은 시간을 확인해, K 이후에 섭취할 음식을 결정
#
#     # 우선순위큐의 남아있는 요소들을 음식 번호를 기준으로 오름차순 정렬
#     result = sorted(q, key=lambda x:x[1])
#
#     # (K 발생까지 남은 시간 % 남은 음식 개수), 배열의 idx는 0부터 시작하므로 나머지 값을 idx로 사용하면 됨
#     return result[(k-sum_time) % length][1]