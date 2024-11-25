# khai bao va khoi tao bien can thiet
N = 20
T = [None] * N  # mang T = [None, None, None, ...]
top_ind = -1


# ham khoi tao ngan xep rong
def Stack():
    global top_ind
    top_ind = -1


# ham kiem tra ngan xep rong
def isEmptyStack(S):
    return top_ind == -1


# ham kiem tra ngan xep day
def stackOverFlow(S):
    return top_ind == N - 1


# ham bo sung phan tu x vao ngan xep
def push(S, x):
    global top_ind
    if stackOverFlow(S):
        raise ValueError("Ngan xep day!")
    else:
        top_ind += 1
        T[top_ind] = x


# ham loai bo phan tu dinh
def pop(S):
    global top_ind
    if isEmptyStack(S):
        raise ValueError("Ngan xep rong!")
    else:
        x = T[top_ind]
        top_ind -= 1
        return x


# ham tra ve phan tu dinh
def top(S):
    if isEmptyStack(S):
        raise ValueError("Ngan xep rong!")
    else:
        return T[top_ind]


# chuong trinh chinh
if __name__ == "__main__":
    S = Stack()
    push(S, 1)
    push(S, 2)
    push(S, 3)
    push(S, 4)
    push(S, 5)

    print(pop(S))
    print(pop(S))
    print(pop(S))
    print(pop(S))
    print(pop(S))
