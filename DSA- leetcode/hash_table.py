class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_func(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_func(key)
        # Check if already key exists -> update
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_func(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_func(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return True
        return False

    def display(self):
        for i, chain in enumerate(self.table):
            print(f"{i} --> {chain}")


# Test
ht = HashTable()
ht.insert("name", "Choti")
ht.insert("age", 20)
ht.insert("city", "Bengaluru")

print("Search:", ht.search("age"))
#ht.delete("city")
ht.display()
