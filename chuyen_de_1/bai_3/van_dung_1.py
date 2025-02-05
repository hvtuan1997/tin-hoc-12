from ngan_xep_oop import Stack

tu_sach = Stack()

# mo file de doc, bo sung sach vao ngan xep
print("Trong tu sach gom co nhung quyen sach la:")
with open("sach.txt", "r") as file:
    for line in file:
        new_word = ""
        for ch in line:
            if ch != "\n":
                new_word += ch
        print(new_word, end="\t")
        tu_sach.push(new_word)

# nhap sach can lay
sach_can_lay = input("\nBan hay nhap vao quyen sach can lay: ")

# lay sach va kiem tra
kt = False
so_quyen_sach = 0
while not tu_sach.isEmpty():
    sach_tren = tu_sach.pop()
    if sach_tren == sach_can_lay:
        kt = True
        break
    so_quyen_sach += 1

# hien thi ket qua
if kt == True:
    print(
        "Tong so quyen sach duoc lay ra truoc quyen can lay la: " + str(so_quyen_sach)
    )
else:
    print("Khong tim thay quyen sach nhu quyen can tim!")
