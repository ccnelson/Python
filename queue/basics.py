
import queue


def q_print(n):
    print("hi", n)


q = queue.Queue()
for i in range(100):
    q.put(q_print(i))  # build queue
while not q.empty():  # FIFO
    q.get()

