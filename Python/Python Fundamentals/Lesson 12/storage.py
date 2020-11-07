class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def get_product(self):
        return self.storage

    def add_product(self, product):
        if len(self.storage) < self.capacity:
            self.storage.append(product)





