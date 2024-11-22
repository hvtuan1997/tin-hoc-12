# ham khai bao va khoi tao ngan xep rong
def Stack():
    return []

# ham kiem tra ngan xep rong
def isEmptyStack(S):
    return len(S) == 0

# ham bo sung phan tu x vao ngan xep
def push(S, x):
    S.append(x)

# ham loai bo va tra ve phan tu dinh
def pop(S):
    if isEmptyStack(S):
        raise RuntimeError("Ngan xep rong")
    return S.pop()

# ham tra ve gia tri phan tu dinh
def top(S):
    if isEmptyStack(S):
        raise RuntimeError("Ngan xep rong")
    return S[len(S) - 1]

# ham hien thi cac phan tu trong ngan xep tu dinh xuong day
def displayStack(S):
    while not isEmptyStack(S):
        x = pop(S)
        print(x)

# test chuong trinh
S = Stack()
push(S, 1)
push(S, 2)
push(S, 3)
push(S, 4)
push(S, 5)
displayStack(S)
top(S)
