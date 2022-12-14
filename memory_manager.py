def initmemory(maxn):
    memory = []
    for i in range(maxn):
        memory.append([0, i + 1, 0])
    return [memory, 0]


def newnode(memstruct):
    memory, firstfree = memstruct
    memstruct[1] = memory[firstfree][1]
    return (firstfree)


def delnode(memstruct, index):
    memory, firstfree = memstruct
    memory[index][1] = firstfree
    memstruct[1] = index


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


memstruct = initmemory(10)
print(memstruct)
root = createandfillnode(memstruct, 8)
print(memstruct)
add(memstruct, root, 10)
add(memstruct, root, 9)
add(memstruct, root, 14)
add(memstruct, root, 13)
add(memstruct, root, 3)
add(memstruct, root, 1)
add(memstruct, root, 6)
add(memstruct, root, 4)
add(memstruct, root, 7)
print(memstruct)
print(find(memstruct, root, 13))

