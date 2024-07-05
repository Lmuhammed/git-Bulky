import os
import time
import re

filename = "repos.txt"

# use the 're' module to check if a URL complies with a specific regex pattern : https://github.com/{username}/{repo_name}.git
def check_url(url):
    pattern = r'^https://github.com/([a-zA-Z0-9-]+)/([a-zA-Z0-9-]+)\.git$'
    if re.match(pattern, url):
        return True
    else:
        return False

# Read URL from file
with open(filename, 'r') as file:
    lines = file.readlines()

for line in lines:
    # Test the URL
    if check_url(line):
        os.system(f"git clone {line}")
        time.sleep(1)
    else:
        print(f"{line} is not a git repo , fix url and retry ...")
        exit(1)

print("تم نسخ جميع المستودعات ، أظهر للعالم إبداعاتك")
print("All repos SUCCESSFULLY cloned, Make something Geat !")

