#----------Practical 2 – OS Security-------------


#-----1) Key Concepts of OS Security

#------------a. User Authentication with Password Hashing-----

import hashlib
users={}
def hash_pass(passw):
    return hashlib.sha256(passw.encode()).hexdigest()
def register(username,passw):
    users[username]=hash_pass(passw)
    print("Registered Successfully!")
def login(user,passw):
    if users.get(user)==hash_pass(passw):
        print("Access Granted!")
    else:
        print("Access Denied!")
register("admin","securepass")
login("admin","securepass")
login("admin","wrongpass")



#--------b. Role-Based File Access (Read/Write Permissions)
permissions={
"admin":["read","write"],
"guest":["read"]
}
def access_file(user_role,action):
    if action in permissions.get(user_role,[]):
        print(f"{user_role} can {action} the file")
    else:
        print(f"{user_role} cannot {action} the file")
access_file("admin","write")
access_file("guest","write")
access_file("guest","read")


#-----------c. File Encryption with AES

from cryptography.fernet import Fernet
key=Fernet.generate_key()
with open("filekey.key","wb") as filekey:
    filekey.write(key)
def encrypt_file(filename):
    with open("filekey.key","rb") as filekey:
        key=filekey.read()
    fernet=Fernet(key)
    with open(filename,"rb") as file:
        data=file.read()
    encrypted=fernet.encrypt(data)
    with open(filename,"wb") as file:
        file.write(encrypted)
    print("File Encrypted")
encrypt_file("example.txt")

#-------d. File Integrity Checker---
import hashlib
def get_fhash(filename):
    with open(filename,"rb") as f:
        return hashlib.sha256(f.read()).hexdigest()
og_hash=get_fhash("example.txt")
curr_hash=get_fhash("example.txt")
if og_hash==curr_hash:
    print("File is intact")
else:
    print("File has been changes")


#-----e. Basic IP Firewall Simulation

blocked_ips=["192.168.1.100","10.0.0.5"]
def check_access(ip):
    if ip in blocked_ips:
        print(f"Access Denied for {ip}")
    else:
        print(f"Access Granted for {ip}")
check_access("192.168.1.100")
check_access("8.8.8.8")

#------f. Activity Logging

import datetime
def log_activity(user,action):
    with open("access_log","a") as logfile:
        time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logfile.write(f"[{time}]{user} -> {action}\n")
log_activity("admin","Accessed settings")
log_activity("guest","tried to delete files")



#-----------2) Key Concepts of OS Memory

#-------g. Simulate Memory Allocation (Static and Dynamic)
memory = [None] * 100
def allocate(process_id, size):
    for i in range(len(memory) - size + 1):
        if all(block is None for block in memory[i:i+size]):
            for j in range(i, i+size):
                memory[j] = process_id
            return f" Allocated {size} blocks to {process_id} at {i}"
    return " No sufficient memory"
def deallocate(process_id):
    count = memory.count(process_id)
    for i in range(len(memory)):
        if memory[i] == process_id:
            memory[i] = None
    return f"Deallocated {count} blocks from {process_id}"
# Demo
print(allocate("P1", 10))
print(allocate("P2", 20))
print(deallocate("P1"))

#------h. Monitor Real Memory Usage of Python Process

import os, psutil
process = psutil.Process(os.getpid())
print(f" Current Memory Usage: {process.memory_info().rss / 1024**2:.2f} MB")

#-----i. Garbage Collection Visualization

import gc
import sys
a = [1] * (10**6) # Create large object
print("Memory used:", sys.getsizeof(a), "bytes")
del a # Delete variable
gc.collect() # Force garbage collection
print(" Garbage collected")

#-------j. Paging Simulation

import math
def paging_simulator(process_size, page_size):
    num_pages = math.ceil(process_size / page_size)
    page_table = {f"Page {i}": f"Frame {i}" for i in range(num_pages)}
    return page_table
# Example: 1024 KB process with 256 KB pages
table = paging_simulator(1024, 256)
for k, v in table.items():
    print(f"{k} → {v}")

#--------k. Memory Leak Simulation and Detection

import tracemalloc
tracemalloc.start()
def leak_memory():
    leaky_list = []
    for _ in range(100000):
        leaky_list.append("leak" * 1000)
    return leaky_list
leak_memory()
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
print(" Memory Leak Detected at:")
for stat in top_stats[:3]:
    print(stat)


#--------l. Simulated Buffer Overflow

def safe_array_write(array, index, value):
    if index < len(array):
        array[index] = value
        return " Value written"
    else:
        return " Buffer Overflow Attempt!"
arr = [0] * 5
print(safe_array_write(arr, 2, 10))
print(safe_array_write(arr, 10, 10))

