from ngan_xep_oop import Stack

backward = Stack()
forward = Stack()

current_web = ""

option = 0

while option != 4:
    option = int(input("Hya nhap vao su lua chon cua ban: "))

    if option == 1:
        website = input("Hay nhap vao dia chi mot trang web: ")
        if current_web != "":
            backward.push(current_web)
        print("Dang truy cap trang web: " + website)
        current_web = website

    if option == 2:
        if backward.isEmpty():
            print("Chua truy cap trang web nao!")
        else:
            forward.push(current_web)
            current_web = backward.pop()
            print("Dang truy cap trang web: " + current_web)

    if option == 3:
        if forward.isEmpty():
            print("Du lieu trong!")
        else:
            backward.push(current_web)
            current_web = forward.pop()
            print("Dang truy cap trang web: " + current_web)
