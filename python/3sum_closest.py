# https://leetcode.com/problems/3sum-closest/

# initial commit comment for a new branch in an jupiter notebook
from itertools import chain, combinations

# nums = [0,0,0], 
# target = 1

# nums = [-1,2,1,-4]
# target = 1

target_l = [target-1, target, target+1]

print(type(target_l[2]))


def all_subsets_size3(ss):
    if len(ss) > 3:
        return combinations(ss, 3)
    else:
        return (ss)
    

subset_list_nums = []

for subset in all_subsets_size3(nums):
    subset_list_nums.append(subset)
    #print(subset)

print(subset_list_nums)
threesum_val = []
for val in subset_list_nums:
    if sum(val) in target_l and len(val) == 3: 
        #print(val) 
        threesum_val = val

print(*threesum_val)