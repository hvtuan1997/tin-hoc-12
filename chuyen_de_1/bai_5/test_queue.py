from hang_doi_oop import Queue

# ===chuong trinh chinh===
if __name__ == "__main__":
    q = Queue()

    # bo sung
    q.enqueue(6)
    q.enqueue(10)
    q.enqueue(1)

    # hien thi
    print("Danh sach cac phan tu trong hang doi la:")
    while not q.is_empty():
        print(q.dequeue())
