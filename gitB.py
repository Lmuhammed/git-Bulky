try:
    import os       #To run git clone
    import time     #To sleep :D
    import re       #To check regx pattern
except ImportError:
    print("Error: This script requires : 'os' , 'time' or 're' modules")
    print("Please install the dependencies then run the script.")
    raise SystemExit(1)

filename = "repos.txt"

# use the 're' module to check if a URL complies with a specific regex pattern : https://github.com/{username}/{repo_name}.git
def check_url(url):
    pattern = r'^https://github.com/([a-zA-Z0-9-]+)/([a-zA-Z0-9-]+)\.git$'
    if re.match(pattern, url):
        return True
    else:
        return False

def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0

#check if file exist
if os.path.exists(filename):
    #check if file not empty
    if not is_file_empty(filename):
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
        print("All repos SUCCESSFULLY cloned, make something Great !")
    #if file empty
    else:
        print(f"The file '{filename}' is empty.")

#if file not exist
else:
    print(f"The file {filename} not exist ... ")

