from ngan_xep_oop import Stack

backward = Stack()
option = 0

while option != 3:
    option = int(input("Hay nhap su lua chon cua ban: "))

    if option == 1:
        website = input("Hay nhap dia chi trang web ban muon den: ")
        backward.push(website)
        print("Dang truy cap trang web: " + website)

    if option == 2:
        if backward.isEmpty():
            print("Ban chua truy cap trang web nao!")
        else:
            website = backward.pop()
            print("Dang truy cap trang web: " + website)
