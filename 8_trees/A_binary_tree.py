def initmemory(maxn):
    memory = []
    for i in range(maxn):
        memory.append([0, i + 1, 0])
    return [memory, 0]


def newnode(memstruct):
    memory, firstfree = memstruct
    memstruct[1] = memory[firstfree][1]
    return firstfree


def createandfillnode(memstruct, key):
    index = newnode(memstruct)
    memstruct[0][index][0] = key
    memstruct[0][index][1] = -1
    memstruct[0][index][2] = -1
    return index


def find(memstruct, root, x):
    key = memstruct[0][root][0]
    if x == key:
        return root
    elif x < key:
        left = memstruct[0][root][1]
        if left == -1:
            return -1
        else:
            return find(memstruct, left, x)
    else:
        right = memstruct[0][root][2]
        if right == -1:
            return -1
        else:
            return find(memstruct, right, x)


def add(memstruct, root, x):
    key = memstruct[0][root][0]
    if x < key:
        left = memstruct[0][root][1]
        if left == -1:
            memstruct[0][root][1] = createandfillnode(memstruct, x)
        else:
            add(memstruct, left, x)
    elif x > key:
        right = memstruct[0][root][2]
        if right == -1:
            memstruct[0][root][2] = createandfillnode(memstruct, x)
        else:
            add(memstruct, right, x)


def printtree(memstruct, root, depth=0):
    key = memstruct[0][root][0]
    left = memstruct[0][root][1]
    if left != -1:
        printtree(memstruct, left, depth + 1)
    print(f"{''.join('.' * depth)}{key}")
    right = memstruct[0][root][2]
    if right != -1:
        printtree(memstruct, right, depth + 1)


memstruct = initmemory(1000)

first = True

while True:
    try:
        request = list(input().split())
        if not request:
            break
        elif request[0] == 'ADD' and first:
            root = createandfillnode(memstruct, int(request[1]))
            print('DONE')
            first = False
        elif request[0] == 'ADD' and not first:
            if find(memstruct, root, int(request[1])) == -1:
                add(memstruct, root, int(request[1]))
                print('DONE')
            else:
                print('ALREADY')
        elif request[0] == 'SEARCH' and first:
            print('NO')
        elif request[0] == 'SEARCH' and not first:
            if find(memstruct, root, int(request[1])) != -1:
                print('YES')
            else:
                print('NO')

        if request[0] == 'PRINTTREE':
            printtree(memstruct, root)
    except:
        break
