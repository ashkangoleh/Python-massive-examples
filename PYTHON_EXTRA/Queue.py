import multiprocessing
import time

def run():
    books = [
        "pride-and-prejudice.txt",
        "heart-of-darkness.txt",
        "frankenstein.txt",
        "dracula.txt",
    ]
    queue = multiprocessing.Queue()

    print("Enqueuing...")
    for book in books:
        print(book)
        queue.put(book)
        time.sleep(1)
    print("\nDequeuing...")
    while not queue.empty():
        time.sleep(1)
        print(queue.get())


if __name__ == "__main__":
    run()
    
    
    
#fastero 'file: Queue.py' for thest speed