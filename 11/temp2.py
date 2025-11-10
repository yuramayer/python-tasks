"""temp2 solution"""


data = [
    ('task1', 100, 20),
    ('task2', 100, 40),
    ('task3', 100, 50),
    ('task4', 100, 100)
]

def func(data: list, N: int):

    # сортируем, o n logn
    data = sorted(data, key=lambda x: x[2])

    # будем искать самых ранних воркеров
    workers_time = {i: 0 for i in range(N)}

    for task_name, dur, delay_max in data:

        earliest_time = float('inf')
        earliest_worker_ix = N

        for worker_ix, worker_time in workers_time.items():

            if worker_time < earliest_time:
                earliest_time = worker_time
                earliest_worker_ix = worker_ix 

        if earliest_time > delay_max:
            return False
        
        workers_time[earliest_worker_ix] = earliest_time + dur
    
    return True
