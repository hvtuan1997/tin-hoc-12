class Queue:
    # ham khoi tao
    def __init__(self):
        self.ds = []
        self.front_idx = 0

    # ham __compress -> xoa cac vi tri trong o dau day
    def __compress(self):
        new_list = []
        for i in range(self.front_idx, len(self.ds)):
            new_list.append(self.ds[i])
        self.ds = new_list
        self.front_idx = 0

    # ham bo sung phan tu x vao hang doi
    def enqueue(self, x):
        self.ds.append(x)

    # ham loai bo phan tu dau cua hang doi
    def dequeue(self):
        # kiem tra hang doi rong
        if self.is_empty():
            raise RuntimeError("Hang doi rong!")

        # loai bo o trong du thua o dau hang doi
        if self.front_idx * 2 > len(self.ds):
            self.__compress()

        # loai bo va tra ve phan tu dau cua day
        tg = self.ds[self.front_idx]
        del self.ds[self.front_idx]
        return tg

    # ham kiem tra hang doi rong
    def is_empty(self):
        return self.front_idx == len(self.ds)

    # ham tra ve gia tri dau tien cua hang doi
    def front(self):
        if self.is_empty():
            raise RuntimeError("Hang doi rong!")
        else:
            return self.ds[self.front_idx]
