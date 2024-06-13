import time
import threading

un_lock = threading.RLock()

class Myprocess (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        i = 0
        with un_lock:
            while i < 3:
            # print(threading.current_thread())
                letters = "ABC"
                for lt in letters:
                    print(lt)
                    time.sleep(0.3)
            i += 1


t1 = Myprocess()
t2 = Myprocess()


t1.start()
t2.start()

t1.join()
t2.join()

print("FIN DU PROGRAMME")


# def time_one():
#     i = 0
#     while i < 3:
#         print("La séquence oooooooooooooooo")
#         i += 1
#         time.sleep(0.3)

# def time_two():
#     i = 0
#     while i < 3:
#         print("La séquence xxxxxxxxxxxxxxxxx")
#         i += 1
#         time.sleep(0.3)

# t1 = threading.Thread(target=time_one)
# t2 = threading.Thread(target=time_two)

# t1.start()
# t2.start()

# t1.join()
# t1.join()

# print("FIN DU PROGRAMME")
