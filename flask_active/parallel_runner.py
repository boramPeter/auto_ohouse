import concurrent.futures

def run_parallel(*functions):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(func) for func in functions]
        concurrent.futures.wait(futures)

def run_parallel_process(*functions):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(func) for func in functions]
        concurrent.futures.wait(futures)