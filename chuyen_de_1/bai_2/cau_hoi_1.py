# ham kiem tra ngan xep rong
def isEmptyStack(S):
    return len(S) == 0


# ham loai bo va tra ve phan tu dinh
def pop(S):
    if isEmptyStack(S):
        print("Ngan xep rong, khong the thuc hien duoc lenh nay")
    else:
        return S.pop()


# ham tra ve gia tri phan tu dinh
def top(S):
    if isEmptyStack(S):
        print("Ngan xep rong, khong the thuc hien duoc lenh nay")
    else:
        return S[len(S) - 1]
