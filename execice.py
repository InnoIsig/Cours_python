import time
import threading

# un_lock = threading.RLock()

# class Myprocessibg(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)

#     def run(self):
#         i = 0
#         with un_lock:
#             while i < 3:
#                 leters = "ABC"
#                 for lt in leters:
#                     print(lt)
#                     time.sleep(0.3)
#                     i += 1

# t1 = Myprocessibg()
# t2 = Myprocessibg()

# t1.start()
# t2.start()

# t1.join()
# t2.join()

def Premier_sequence():
    i = 0
    while i < 3:
        print("Je suis la premiere sequence")
        time.sleep(5)
        i += 1

def Deuxieme_sequence():
    i = 0
    while i < 3:
        print("Je suis la deuxieme sequence")
        time.sleep(5)
        i += 1

t1 = threading.Thread(target=Premier_sequence)
t2 = threading.Thread(target=Deuxieme_sequence)

t1.start()
t2.start()

t1.join()
t1.join()

