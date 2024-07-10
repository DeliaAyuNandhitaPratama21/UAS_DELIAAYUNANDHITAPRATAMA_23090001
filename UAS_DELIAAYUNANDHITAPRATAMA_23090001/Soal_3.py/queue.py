class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)
        print(f"Pesanan '{item}' telah ditambahkan ke antrian")

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.items.pop(0)
            print(f"Pesanan '{removed_item}' telah dihapus dari antrian")
            return removed_item
        else:
            print("Antrian kosong dan tidak ada pesanan yang dapat dihapus")
            return None

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
