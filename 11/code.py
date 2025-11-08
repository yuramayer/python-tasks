"""Code for the 11th task"""

tasks = [
    ('task1', 100, 20),
    ('task2', 100, 40),
    ('task3', 100, 50),
    ('task4', 100, 101)
]


def complete_tasks(tasks, N):
    
    # сортируем tasks
    tasks_sorted = sorted(tasks, key=lambda x: x[2])
    
    # создаём календарь воркеров:
    #  для каждго воркера храним момент времени,
    #  когда они освободились. В начале свободны
    workers_finish_time = {i: 0 for i in range(N)}

    # проходим по нашим таскам
    for task_name, dur, delay_max in tasks_sorted:

        # переменные под поиск свободного воркера
        #  - min_value = лучшее время освобождения
        min_value = float('inf')
        #  - early_worker_idx = индекс
        #    лучшего кандидата
        early_worker_idx = N + 1

        # проходимся по воркерам, ищем свободного
        for key, value in workers_finish_time.items():
            
            # если воркер освобождается
            #  раньше текущего лучшего -
            #  обновляю лучшего
            if value < min_value:
                # фиксируем нового
                #  самого раннего воркера
                min_value = value
                early_worker_idx = key
        
        # стартуем на самом раннем как можно раньше
        start_time = workers_finish_time[early_worker_idx]

        # если самый ранний воркер
        #  освобождается слишком поздно,
        #  то start_time > delay_max
        #  и возвращаем False
        if start_time > delay_max:
            return False

        # назначаем задачу раннему воркеру:
        #  теперь он будет занят до + duration
        workers_finish_time[early_worker_idx] = start_time + dur

    return True
 