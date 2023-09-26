import time

"""
This will print the wtfpython after 3 seconds due to the end argument because the output buffer is flushed either after encountering \n or when the program finishes execution. We can force the buffer to flush by passing flush=True argument.
"""
print("wthpython", end="_")
time.sleep(2)

print()
print("python_fix", end="_", flush=True)
time.sleep(2)