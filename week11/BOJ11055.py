# 가장 큰 증가하는 수열
# 수열 A가 주어졌을 때, 그 수열의 증가하는 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램

N = int(input())
nums = list(map(int, input().split()))
total_sums = []

def sum(current_nums, index, current_sum):
  if index == N:
    return

  i_num = nums[index]
  
  # index 번째 숫자가 들어기는 경우
  if i_num > current_nums[-1]:
    new_nums = [num for num in current_nums]
    new_nums.append(i_num)
    total_sums.append(current_sum + i_num)
    sum(new_nums, index+1, current_sum + i_num)

  # index 번째 숫자가 안들어 가는 경우
  sum(current_nums, index+1, current_sum)


current_nums = [nums[0]]
current_sums = nums[0]

sum(current_nums, 1, current_sums)

print(max(total_sums))