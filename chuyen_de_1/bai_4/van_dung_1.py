# cai dat cau truc du lieu hang doi bang kieu danh (list) trong Python


# ham tao hang doi rong
def Queue():
    return []


# ham kiem tra hang doi rong
def is_empty(Q):
    return len(Q) == 0


# ham bo sung x vao hang doi
def enqueue(Q, x):
    Q.append(x)


# ham loai bo phan tu dau cua hang doi
def dequeue(Q):
    if is_empty(Q):
        raise RuntimeError("Hang doi rong, khong the thuc hien lenh")
    else:
        return loai_bo_phan_tu_dau(Q)


# ham tra ve gia tri phan tu dau
def front(Q):
    if is_empty(Q):
        raise RuntimeError("Hang doi rong, khong the thuc hien lenh")
    else:
        return Q[0]


# ham tra ve so luong phan tu cua Q
def length(Q):
    return len(Q)


# ham loai bo va tra ve gia tri phan tu dau
def loai_bo_phan_tu_dau(Q):
    tg = Q[0]
    for i in range(len(Q) - 1):
        Q[i] = Q[i + 1]
    return tg
