import time
import datetime
import string
import random

chars = string.ascii_letters + string.digits
#random.seed(int(time.time()))
start = int(datetime.datetime(2021, 7, 10).timestamp())
end = start + 86400 * 3

#NovaSecurity.net
#NovaSecurity.net

with open("passwords.txt","w") as f:
    for seed in range(start, end):
        random.seed(int(seed))
        password = ''.join([random.choice(chars) for x in range(32)])
        f.write(password + "\n")
