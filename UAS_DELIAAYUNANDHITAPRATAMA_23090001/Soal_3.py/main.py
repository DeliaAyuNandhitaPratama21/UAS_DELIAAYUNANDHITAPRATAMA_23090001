from queue import Queue

def main():
    antrian_pesanan = Queue()

    antrian_pesanan.enqueue("Pesanan 1")
    antrian_pesanan.enqueue("Pesanan 2")
    antrian_pesanan.enqueue("Pesanan 3")

    print(f"Jumlah pesanan dalam antrian: {antrian_pesanan.size()}")

    antrian_pesanan.dequeue()
    antrian_pesanan.dequeue()

    print(f"Pesanan di depan antrian: {antrian_pesanan.peek()}")

    antrian_pesanan.dequeue()
    antrian_pesanan.dequeue()  

    print(f"Jumlah pesanan dalam antrian: {antrian_pesanan.size()}")

if __name__ == "__main__":
    main() 
