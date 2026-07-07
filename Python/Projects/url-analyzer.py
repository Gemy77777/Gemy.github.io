import re
import time

url = input("Enter your URL: ")
search = re.match(r"^(https?)://(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)?$", url)

if search:
    print("Valid URL")
    time.sleep(1)
    if search.group(1) is not None:
        print("Protocol:", search.group(1))
        time.sleep(1)
    if search.group(2) is not None:
        print("Subdomain:", search.group(2))
        time.sleep(1)
    if search.group(3) is not None:
        print("Domain:", search.group(3))
        time.sleep(1)
    if search.group(4) is not None:
        print("TLD:", search.group(4))
        time.sleep(1)
    if search.group(5) is not None:
        print("Port:", search.group(5))
        time.sleep(1)
    if search.group(6) is not None:
        print("Path:", search.group(6))
else:
    print("Invalid URL")