n = int(input())
reply = [0] * n
topic = [''] * n
for i in range(n):
    a = int(input())
    if a == 0:
        reply[i] = i
        topic[i] = input()
        input()
    else:
        reply[i] = reply[a - 1]
        input()

count_replies = {}

for el in reply:
    count_replies[el] = count_replies.get(el, 0) + 1

ans = []
for cnt in count_replies:
    ans.append((-count_replies[cnt], cnt))
print(topic[min(ans)[1]])
