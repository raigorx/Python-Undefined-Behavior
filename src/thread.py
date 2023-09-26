import threading
import time
import http.client
import ssl

def cpu_bound_task(n):
    while n > 0:
        n -= 1

start = time.time()
threads = []
# Create 2 threads that run a CPU-bound task
for _ in range(2):
    thread = threading.Thread(target=cpu_bound_task, args=(10**8,))
    thread.start()
    threads.append(thread)

# Wait for both threads to complete
for thread in threads:
    thread.join()

end = time.time()
thread_time = (end - start)
start = time.time()
cpu_bound_task(10**8)
cpu_bound_task(10**8)
end = time.time()
non_thread_time = (end - start)
"""
Multiple Python threads won't run your Python code concurrently (yes, you heard it right!).
It may seem intuitive to spawn several threads and let them execute your Python code concurrently, but, because of the Global Interpreter Lock in Python, all you're doing is making your threads execute on the same core turn by turn.
so case like this threads just make it slower instead of faster.

However these can lead to unexpected results so, some times is the opposite
thread_time < non_thread_time
these example is a CPU-bound one
"""
print(f"cpu bound task {thread_time=}")
print(f"cpu bound task {non_thread_time=}")

def fetch_website(url):
    domain = url.replace("https://", "").replace("http://", "")
    conn = http.client.HTTPSConnection(domain, context=ssl._create_unverified_context())
    conn.request("GET", "/")
    response = conn.getresponse()
    response.read().decode()
    conn.close()

websites = ['https://www.google.com', 'https://www.bing.com']

start = time.time()

threads = []
for website in websites:
    thread = threading.Thread(target=fetch_website, args=(website,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

IO_thread_time = (end - start)
start = time.time()
for website in websites:
    fetch_website(website)
end = time.time()
non_IO_thread_time = (end - start)
"""
In IO-bound tasks, threads improve perfomance because the GIL is released while waiting for the IO operation to complete.
"""
assert non_IO_thread_time > IO_thread_time
