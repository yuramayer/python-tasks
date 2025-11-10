"""temp code"""

tasks = [
    ('task1', 100, 20),
    ('task2', 100, 40),
    ('task3', 100, 50),
    ('task4', 100, 101)
]

def check_tasks(tasks, N):

    tasks = sorted(tasks, key=lambda x: x[2])

    # создаём мапу вида
    # воркер - его время освобождения
    workers = {i: 0 for i in range(N)}

    # мы проверяем, если каждый раз
    # будем отправлять самого раннего воркера,
    # сработает ли схема?
    # если поймаем ошибку,
    # значит невозможно
    for task_name, dur, delay_max in tasks:
        
        # создадим переменные под поиск
        # самого свободного воркера
        min_value = float('inf')
        min_worker_ix = N+1

        for worker_ix, worker_time in workers.items():
            if worker_time < min_value:
                min_value = worker_time
                min_worker_ix = worker_ix
        
        # по итогу стартуем на раннем воркере
        worker_start_time = workers[min_worker_ix]
        
        # упс - самый ранний воркер не успел
        if worker_start_time > delay_max:
            return False

        # воркер теперь будет загружен
        workers[min_worker_ix] = worker_start_time + dur
    
    return True
