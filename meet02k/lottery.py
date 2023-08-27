import random

list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

my_ticket = [4, "A", 6, "B"]
cnt = 0
while True:
    randomm = random.sample(list_number, 4)
    
    if randomm == my_ticket:
        break
    
    cnt += 1

print(f"ini adalah percobaan ke {cnt} untuk mendapatkan {my_ticket}")