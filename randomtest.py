import random
data = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@$#%&"
a = ''.join(random.choice(data) for _ in range(32))
print(a)