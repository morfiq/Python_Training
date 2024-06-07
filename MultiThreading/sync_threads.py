import threading

x = 0
lock = threading.Lock()

def increment():
    global x
    for _ in range(10):
        with lock:
            x += 1

threads = []
for _ in range(4):
    t = threading.Thread(target=increment)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Final value of x:", x)











#
#
# class FakeDatabase:
#     def __init__(self):
#         self.value = 0
#         self._lock = threading.Lock()
#
#     def locked_update(self, name):
#         logging.info("Thread %s: starting update", name)
#         logging.debug("Thread %s about to lock", name)
#         with self._lock:
#             logging.debug("Thread %s has lock", name)
#             local_copy = self.value
#             local_copy += 1
#             time.sleep(0.1)
#             self.value = local_copy
#             logging.debug("Thread %s about to release lock", name)
#         logging.debug("Thread %s after release", name)
#         logging.info("Thread %s: finishing update", name)