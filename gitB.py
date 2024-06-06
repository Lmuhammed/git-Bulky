import os
import time

filename = "repos.txt"

with open(filename, 'r') as file:
    lines = file.readlines()

for line in lines:
    os.system(f"git clone {line}")
    time.sleep(1)

print("تم نسخ جميع المستودعات ، أظهر للعالم إبداعاتك")
print("ALl repos SUCCESSFULLY , Make something Geat !")

