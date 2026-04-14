class KeyValuePair(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.quantity = 0
        self.hash_map = [None] * self.capacity

    def hash_encode(self, key:int) -> int:
        return key % self.capacity

    def open_address_collision(self, hashed, key):
        while self.hash_map[hashed] is not None and self.hash_map[hashed].key != key:
            hashed += 1

        return hashed

    def insert(self, key: int, value: int) -> None:
        hashed_pos = self.hash_encode(key)
        hashed_pos = self.open_address_collision(hashed_pos, key)

        if self.hash_map[hashed_pos] is None:
            self.hash_map[hashed_pos] = KeyValuePair(key, value)
            self.quantity += 1 
        else:
            self.hash_map[hashed_pos].value = value
        
        if self.quantity >= self.capacity // 2:
            self.resize()

    def get(self, key: int) -> int:
        hashed_pos = self.hash_encode(key)
        hashed_pos = self.open_address_collision(hashed_pos, key)
        
        if self.hash_map[hashed_pos] is None:
            return -1

        return self.hash_map[hashed_pos].value

    def remove(self, key: int) -> bool:
        hashed_pos = self.hash_encode(key)
        hashed_pos = self.open_address_collision(hashed_pos, key)

        if self.hash_map[hashed_pos] is None:
            return False

        self.hash_map[hashed_pos] = None
        self.quantity -= 1

        return True

    def getSize(self) -> int:
        return self.quantity

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2 # Update size
        temp = self.hash_map # Store current entries
        self.hash_map = [None] * self.capacity # Create new storage array of new length

        self.quantity = 0 # Reset quantity, as it will be increment from insert
        for index, entry in enumerate(temp):
            if entry is None:
                continue
            
            self.insert(entry.key, entry.value) # Rehash the key based on new capacity
            