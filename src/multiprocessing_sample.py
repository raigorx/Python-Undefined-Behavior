import multiprocessing
import time

def cpu_bound_task(n):
    while n > 0:
        n -= 1
"""
compare to threads the multiprocessing spawn a new process and each process has its own GIL
so the CPU-bound task can be executed in parallel
"""
if __name__ == '__main__':
    start = time.time()
    processes = []
    # Create 2 processes that run a CPU-bound task
    for _ in range(2):
        process = multiprocessing.Process(target=cpu_bound_task, args=(10**8,))
        process.start()
        processes.append(process)

    # Wait for both processes to complete
    for process in processes:
        process.join()

    end = time.time()
    multiprocessing_time = (end - start)
    start = time.time()
    cpu_bound_task(10**8)
    cpu_bound_task(10**8)
    end = time.time()
    non_multiprocessing_time = (end - start)
    print(f"cpu bound task {multiprocessing_time=}")
    print(f"cpu bound task {non_multiprocessing_time=}")
    assert multiprocessing_time < non_multiprocessing_time