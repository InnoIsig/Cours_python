import time

# print("Premier message")

#1èré Janvier 19970 00h00
# time.sleep(5)
#print(time.time())

# bigin = time.time()
# print("Début")

# time.sleep(5)

# End = time.time()
# print("Fin")

# print(f"L'execution s'est fait pendant {End - bigin}")

#print(time.localtime())
tps = time.localtime()
print(tps)

tps = time.mktime(tps)
print(tps)

print(time.strftime("%Z"))