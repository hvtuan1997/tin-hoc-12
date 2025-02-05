from ngan_xep_oop import Stack


def kiem_tra_bt(bieu_thuc):
    hop_le = True
    ngoac_mo = Stack()

    for i in range(0, len(bieu_thuc)):
        if bieu_thuc[i] in {"(", "["}:
            ngoac_mo.push(bieu_thuc[i])
        elif bieu_thuc[i] in {")", "]"}:
            if ngoac_mo.isEmpty():
                hop_le = False
                break
            else:
                tmp = ngoac_mo.pop()
                if ((bieu_thuc[i] == ")") and (tmp != "(")) or (
                    (bieu_thuc[i] == "]") and (tmp != "[")
                ):
                    hop_le = False
                    break
    if not ngoac_mo.isEmpty():
        hop_le = False

    return hop_le


# ===chuong trinh chinh===
if __name__ == "__main__":
    bieu_thuc = input("Hay nhap bieu thuc cua ban: ")
    hop_le = kiem_tra_bt(bieu_thuc)

    if hop_le:
        print("Bieu thuc vua nhap la hop le!")
    else:
        print("Bieu thuc vua nhap khong hop le!")
