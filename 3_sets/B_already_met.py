nums = list(map(int, input().split()))
numsset = set()

for num in nums:
    if num in numsset:
        print('YES')
    else:
        print('NO')
    numsset.add(num)
