from config import (
    store_1,
    store_2,
    store_3,
    store_4,
    store_5,
    store_6,
    store_7,
    setup_store,
)
from action import doubleClick


class Refill:
    def __init__(self):
        self.refill_count = 1
        self.refill_store = 1

        self.store = store_1

    def execute(self):
        self.refill_count = self.refill_count + 1
        if self.refill_count > 10:
            if self.refill_store == setup_store:
                self.refill_store = 1
            else:
                self.refill_store = self.refill_store + 1
            self.updateStore()
            self.refill_count = 0

        self.refill()

    def updateStore(self):
        if self.refill_store == 1:
            self.store = store_1
        elif self.refill_store == 2:
            self.store = store_2
        elif self.refill_store == 3:
            self.store = store_3
        elif self.refill_store == 4:
            self.store = store_4
        elif self.refill_store == 5:
            self.store = store_5
        elif self.refill_store == 6:
            self.store = store_6
        else:
            self.store = store_7

    def refill(self):
        storePosition = (
            (self.store[0] + self.store[2]) // 2,
            (self.store[1] + self.store[3]) // 2,
        )

        doubleClick(storePosition)
