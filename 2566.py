# 2566.py
nums = [list(map(int, input().split())) for i in range(9) ]


curr_max = -1
max_i = -1
max_j = -1
for i in range(9):
    for j in range(9):
        if nums[i][j] > curr_max:
            curr_max = nums[i][j]
            max_i = i
            max_j = j
            
            
print(curr_max)
print(max_i + 1, max_j + 1)