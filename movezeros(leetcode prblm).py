def movzeros(nums):
    x=[]
    y=[]
    for i in range(len(nums)):
        if nums[i]:
            x.append(nums[i])
        else:
            y.append(nums[i])
    z=x+y
    print(z)
nums=[0,1,0,3,12]
movzeros(nums)
    