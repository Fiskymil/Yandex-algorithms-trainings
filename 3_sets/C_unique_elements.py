nums = list(map(int, input().split()))

set_total = set(nums)
set_needed = set()
for n in nums:
    if n not in set_needed:
        set_needed.add(n)
    elif n in set_total:
        set_total.remove(n)

for n in nums:
    if n in set_total:
        print(n, end=' ')
