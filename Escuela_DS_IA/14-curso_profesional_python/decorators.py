from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        delta_time = final_time - initial_time
        print(f"Execution time: {delta_time.total_seconds()} s")
    return wrapper

@execution_time
def random_func():
    for _ in range(1000000):
        pass

@execution_time
def sum(a:int, b:int) -> int:
    return a + b

if __name__ == "__main__":
    sum(2,5)

