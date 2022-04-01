import os
import threading
from flask import Flask
app = Flask(__name__)

lock = threading.Lock()
aList = []

@app.route('/')
def hello_world():
    print("Processing request in pid ", os.getpid())
    g = prime_generator(1000)
    add_item(' '.join(map(str, list(g))))
    return ' '.join(map(str, aList))

def prime_generator(end):
    for n in range(2, end):     # n starts from 2 to end
        for x in range(2, n):   # check if x can be divided by n
            if n % x == 0:      # if true then n is not prime
                break
        else:                   # if x is found after exhausting all values of x
            yield n

def add_item(item):
    lock.acquire()
    aList.append(item)
    lock.release()
