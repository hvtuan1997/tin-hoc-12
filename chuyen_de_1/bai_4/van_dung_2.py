# Cai dat cau truc du lieu Hang doi bang mang 1 chieu

# khai bao bien
N = 100
T = [None] * N  # T = [None, None, None, ...]
back_idx = -1  # hang doi dang rong


# ham khoi tao hang doi
def Queue():
    global back_idx
    back_idx = -1
    return T


# ham kiem tra hang doi rong
def is_empty():
    return back_idx == -1


# ham kiem tra hang doi day
def is_full():
    return back_idx == (N - 1)


# ham bo sung phan tu x vao hang doi
def enqueue(Q, x):
    global back_idx
    if is_full():
        raise RuntimeError("Hang doi da day!")
    else:
        back_idx += 1
        Q[back_idx] = x


# ham loai bo phan tu dau
def dequeue(Q):
    global back_idx
    if is_empty():
        raise RuntimeError("Hang doi da rong!")
    else:
        x = Q[0]
        back_idx -= 1
        Q.pop(0)
        return x


# ham tra ve gia tri phan tu dau
def front(Q):
    if is_empty():
        raise RuntimeError("Hang doi da rong!")
    else:
        return Q[0]
