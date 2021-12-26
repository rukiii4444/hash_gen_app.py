import hashlib
import sys


try:
    num = int(input("num: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(0)
except Exception as e:
    print("Error: Unknown error")
    print(e)
    sys.exit(0)

i = 1

while i <= num:
    hash_num = hashlib.sha256(str(i).encode()).hexdigest()
    print(i, hash_num)
    i += 1