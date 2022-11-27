builds = list(map(int, input().split()))
list_dist = [0]

for i in range(len(builds)):
    dist_count_l = 0
    dist_count_r = 0
    closer_shop_l = closer_shop_r = len(builds)
    if builds[i] == 1:
        for j in range(i - 1, -1, -1):
            dist_count_l += 1
            if builds[j] == 2:
                closer_shop_l = dist_count_l
                break
        for j in range(i + 1, len(builds)):
            dist_count_r += 1
            if builds[j] == 2:
                if dist_count_r < closer_shop_l:
                    closer_shop_r = dist_count_r
                    break
        list_dist.append(min(closer_shop_r, closer_shop_l))

print(max(list_dist))

