import random


class RandomizedSet:

    def __init__(self):
        self.list_val = []
        self.dict_idx = dict()

    def insert(self, val: int) -> bool:
        if val in self.dict_idx:
            return False
        self.dict_idx[val] = len(self.list_val)
        self.list_val.append(val)
        return True

    def remove(self, val: int) -> bool:

        if val not in self.dict_idx:
            return False
        # index of value to remove
        val_idx = self.dict_idx[val]
        # last value to swap with val
        val_swap = self.list_val[-1]

        self.list_val[val_idx] = val_swap
        self.list_val.pop()
        self.dict_idx[val_swap] = val_idx
        self.dict_idx.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.list_val)