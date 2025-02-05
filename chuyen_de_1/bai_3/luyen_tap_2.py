from ngan_xep_oop import Stack


def kiem_tra_bt(bieu_thuc, tong_tron, tong_vuong):
    hop_le = True
    ngoac_mo = Stack()

    for i in range(0, len(bieu_thuc)):
        if bieu_thuc[i] in {"(", "["}:
            ngoac_mo.push(bieu_thuc[i])
            if bieu_thuc[i] == "(":
                tong_tron += 1
            else:
                tong_vuong += 1
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

    return (hop_le, tong_tron, tong_vuong)


# ===chuong trinh chinh===
if __name__ == "__main__":
    bieu_thuc = input("Hay nhap bieu thuc cua ban: ")
    tong_tron = 0
    tong_vuong = 0
    hop_le, tong_tron, tong_vuong = kiem_tra_bt(bieu_thuc, tong_tron, tong_vuong)

    if hop_le:
        print("Bieu thuc vua nhap la hop le!")
        print("Tong so ngoan tron la: " + str(tong_tron))
        print("Tong so ngoan vuong la: " + str(tong_vuong))
    else:
        print("Bieu thuc vua nhap khong hop le!")
