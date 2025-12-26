""two sums""
def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
               return i,j 
print(twosum([2,7,8,11,13,2],9))            