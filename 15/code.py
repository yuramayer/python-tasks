"""15th task"""

"""
Для каждого user_id храним массив его меток

При каждом новом событии:

- добавляем метку в список
- удаляем метки старше ts - 900 секунд

Проверяем, превышает ли длина окна 1000

Поддерживаем глобальный счётчик актив. юзеров
"""

import time
from collections import defaultdict

WINDOW = 15 * 60  # 15 минут в секундах
THRESHOLD = 1000

class EventTracker:

    def __init__(self, get_events):
        # defaultdict
        # позволяет нам добавлять элементы
        # в виде events['user_id'] = [1, 2]
        # без проверок на user_id
        self.events = defaultdict(list)

        # функция для проверки по таймингу
        self.get_events = get_events

        self.last_update = 0

    def update(self, user_id, ts):
        """Подгружаем новые события и очищаем старые"""
        now = time.time()
        if self.last_update:
            start = self.last_update + 60
        else:
            start = now - WINDOW
        
        # за каждую минуту добавляем историю в events
        for t in range(start, now + 1, 60):
            # данные берём функцией get_events(time)
            for user_id, ts in self.get_events(t):
                self.events[user_id].append(ts)
        
        # удаляем старенькое
        cutoff = now - WINDOW

        for uid in list(self.events):
            self.events[uid] = [
                ts for ts in self.events[uid]
                if ts >= cutoff
            ]
            if not self.events[uid]:
                del self.events[uid]
        
    def get_active_user_count(self):
        """Возвращаем юзеров"""
        # количество всех кто больше threshold
        return sum(
            1 for arr
            in self.events.values()
            if len(arr) > THRESHOLD
        )

