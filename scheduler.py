import redis
import time
from website import db # this is how we communicate with the SQL database

# initializing redis
global red
red = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# this will handle each job as it is created by job scheduler
def handle_job(item):
    print(f"Item => {item}")


# infinite loop since program is constantly checking for jobs
while True:
    item = red.lpop('datasets')
    if item: # if there is a dataset to be run
        handle_job(item)
    else: # no dataset in queue
        print("Nothing...")
        time.sleep(2) # else we sleep for 2 seconds and wait for the next one



