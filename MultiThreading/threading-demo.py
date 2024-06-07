import concurrent.futures
import time
import threading

start = time.perf_counter()

# def do_something(sleeptime):
#     # print(" new thread")
#     print(f'Sleeping {sleeptime} second...')
#     time.sleep(sleeptime)
#     print("Done sleeping!..")

# do_something()
# do_something()
# do_something()
# do_something()
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
# t3 = threading.Thread(target=do_something)
# t4 = threading.Thread(target=do_something)
# # #
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# print("in the middle of the threads")
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# print("waiting for threads to join")
#
# threads = []
# for i in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)
# for thread in threads:
#     thread.join()
#
# end = time.perf_counter() - start
# print(f"Finished in {end} seconds", )
#
#
#
#
#
#
#
#
#
#
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'
#
# #
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [.5, 4, 3, 2, 1]
    # executor.submit(do_something, 1)
    # executor.submit(do_something,1)
    results = executor.map(do_something, secs)

    # for result in results:
    #     print(result)
end = time.perf_counter() - start
print(f"Finished in {end} seconds", )
