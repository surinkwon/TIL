while True:
    nums = sorted(list(map(int, input().split())))
    if nums[0] == nums[1] == nums[2] == 0:
        break
    else:
        if nums[2] ** 2 == nums[0] ** 2 + nums[1] ** 2:
            print('right')
        else:
            print('wrong')