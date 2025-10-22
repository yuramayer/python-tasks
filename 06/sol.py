class ListNode:
    def __init__(self, val):
        self.val, self.next = val, None

    def reverse_list(lst):
        left_ix = 0
        right_ix = len(lst) - 1
        while left_ix < right_ix:
            lst[left_ix], lst[right_ix] = lst[right_ix], lst[left_ix]
            left_ix += 1
            right_ix -= 1
        return lst