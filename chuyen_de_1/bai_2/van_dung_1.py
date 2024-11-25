def Stack():
    pass


def push(S, x):
    pass


def pop(S):
    pass


def isEmptyStack(S):
    pass


def kiem_tra_bieu_thuc(bt):
    """
    Hàm kiểm tra xâu biểu thức chỉ gồm ký ( và ) có hợp lệ hay không
    Hàm trả về True nếu biểu thức đúng.
    Ngược lại, trả về False nếu biểu thức sai.
    """
    S = Stack()
    kq = True
    for ch in bt:
        if ch == "(":
            push(S, "(")
        if ch == ")":
            if isEmptyStack(S):
                kq = False
                break
            else:
                pop(S)
    return kq and isEmptyStack(S)
