"""16th task"""

import time

WINDOW = 60 * 10  # 10 минут

class SlidingAvg:

    def __init__(self):
        self.user_state = {}
        self.sum_values = 0.0
        self.count = 0


    def add_event(self, event):

        user_id, ts, value = event
        
        # удаляем старые записи
        cutoff = ts - WINDOW
        old_users = [
            u for u, (t, _) in self.user_state.items()
            if t < cutoff
        ]

        for u in old_users:
            _, old_v = self.user_state.pop(u)
            self.sum_values -= old_v
            self.active_count -= 1

        # переписываем или добавляем новых
        if user_id in self.user_state:
            old_t, old_v = self.user_state[user_id]
            if ts > old_t:
                self.sum_values += value - old_v
                self.user_state[user_id] = (ts, value)
        else:
            self.user_state[user_id] = (ts, value)
            self.sum_values += value
            self.count += 1
    
    def get_avg(self):
        return self.sum_values / self.active_count if self.active_count else .0
