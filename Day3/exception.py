#print(10/0)
nums = [1,2,3,4] 
#print(nums[4])


try:
    print(nums[4]) 
except IndexError as e:
    print(f'{e}')
finally:
    print('end')