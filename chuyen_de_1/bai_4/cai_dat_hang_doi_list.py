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
        raise RuntimeError("Hang doi rong!")
    else:
        return Q.pop(0)


# ham tra ve gia tri phan tu dau
def front(Q):
    if is_empty(Q):
        raise RuntimeError("Hang doi rong!")
    else:
        return Q[0]
