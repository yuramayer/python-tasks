"""Temp solution"""

import time
from collections import defaultdict


WINDOW = 60 * 15  # 15 минуток
THRESHOLD = 1000

class EventService:

    def __init__(self, get_events):
        
        # defaultdict(list)
        # позволяет добавлять списки
        # прямо по id пользователя;
        # мы будем хранить так время
        self.events = defaultdict(list)

        # get_events = функция получения
        # данных на определённую глубину
        # получает time_sec в int
        self.get_events = get_events

        # будем запоминать, когда мы последний раз обновлялись
        self._last_update = 0

    def add_event(self, user_id: int, ts: int):
        now = time.time()
        self.events[user_id].append(ts)
        cutoff = now - WINDOW

        self.events[user_id] = [
            t for t in self.events[user_id]
            if t >= cutoff
        ]

    def update(self):
        
        # получаем текущее время в секундах
        now = time.time()

        # если прогрузка была, прогружаем 
        # со следующей после прогрузки минуты
        if self._last_update:
            start = self._last_update
            # если у нас минутная дискретность, по +60 добавляем
        # если прогрузки не было, прогружаем последние WINDOW минут
        else:
            start = now - WINDOW

        for t in range(start, now):  # если минуты, то 60 добавляем и now+1 
            new_events = self.get_events(t)
            for user_id, ts in new_events:
                self.events[user_id].append(ts)

        # очищаем окошко
        cutoff = now - WINDOW

        for user_id in list(self.events):
            self.events[user_id] = [
                t for t in self.events[user_id]
                if t >= cutoff
            ]
            if not self.events[user_id]:
                del self.events[user_id]
    
    def get_active_users(self):

        return sum(
            1 for arr
            in self.events.values()
            if len(arr) > THRESHOLD
        )
