class Stack:
    # ham khoi tao
    def __init__(self):
        self.ds = []
    
    # ham kiem tra ngan xep rong hya khong
    def isEmpty(self):
        return len(self.ds) == 0
    
    # ham bo sung phan tu vao ngan xep
    def push(self, x):
        self.ds.append(x)
    
    # ham loai bo phan tu ra khoi ngan xep
    def pop(self):
        if self.isEmpty():
            raise RuntimeError("Ngan xep rong!")
        
        # chi so phan tu dinh
        top_index = len(self.ds) - 1
        # gia tri phan tu dinh
        tg = self.ds[top_index]
        # xoa phan tu dinh
        del self.ds[top_index]
        # tra ve gia tri phan tu dinh
        return tg
    
    # ham tra ve gia tri phan tu dinh
    def top(self):
        if self.isEmpty():
            raise RuntimeError("Ngan xep rong!")
        
        # chi so phan tu dinh
        top_index = len(self.ds) - 1
        # tra ve gia tri phan tu dinh
        return self.ds[top_index]
