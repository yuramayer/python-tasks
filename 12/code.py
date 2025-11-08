"""12th task"""

data = [
    (0, 30), (5, 10), (15, 20),
    (30, 40), (35, 45)
]

"""
Идея - создать словарь со статой.
Мы проходимся по элементам.
Для каждого элемента мы смотрим,
    есть ли открытый слот в словаре
Если есть - добавляем туда элемент
"""

def func(data):
    rooms_d = {}
    room_counter = 0
    # отсортировали по началу
    data = sorted(data, key=lambda x: x[0])

    for meet_start, meet_end in data:

        reused = False
        for room_number, time_end in rooms_d.items():
            # мы можем брать первую 
            #  попавшуюся свободную комнату
            if meet_start >= time_end:
                rooms_d[room_number] = meet_end
                reused = True
                break
        if not reused:
            room_counter += 1
            rooms_d[room_counter] = meet_end
    
    return room_counter
