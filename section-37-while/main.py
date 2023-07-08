# while condition:
#   break
#   continue
import random

rand_num = random.randint(1, 5)
while True:
    num = int(input("Guess number from 1 to 5: "))
    if num != rand_num:
        print("Try again...")
        continue
    print("Victory!")
    break
