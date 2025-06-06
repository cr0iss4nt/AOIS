from hash_table_functions import table_term


class HashTable:
    def __init__(self, size=8):
        self.size = size
        self.count = 0
        self.keys = [None] * size
        self.values = [None] * size
        self.deleted_flags = [False] * size

    def _hash(self, key):
        hash_value = 0
        for i, char in enumerate(str(key)):
            hash_value += (i + 1) * ord(char)
        return hash_value % self.size

    def _probe(self, hash_index, i):
        return (hash_index + i ** 2) % self.size

    def _resize(self):
        old_keys = self.keys
        old_values = self.values
        old_deleted = self.deleted_flags
        self.size *= 2
        self.count = 0
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.deleted_flags = [False] * self.size
        for k, v, deleted in zip(old_keys, old_values, old_deleted):
            if k is not None and not deleted:
                self.set(k, v)

    def set(self, key, value):
        if self.count / self.size > 0.6:
            self._resize()

        idx = self._hash(key)
        i = 0
        added = 1
        while True:
            pos = self._probe(idx, i)
            if self.keys[pos] is None or self.deleted_flags[pos]:
                self.keys[pos] = key
                self.values[pos] = value
                self.deleted_flags[pos] = False
                self.count += 1
                return
            elif self.keys[pos] == key and not self.deleted_flags[pos]:
                print(f"Ключ '{key}' уже существует, запись не произведена.")
                return
            i += added ** 2
            added += 1
            if i >= self.size:
                self._resize()
                idx = self._hash(key)
                i = 0
                added = 1

    def get(self, key):
        idx = self._hash(key)
        i = 0
        added = 1
        while True:
            pos = self._probe(idx, i)
            k = self.keys[pos]
            if k is None:
                return None
            if k == key and not self.deleted_flags[pos]:
                return self.values[pos]
            i += added ** 2
            added += 1

    def delete(self, key):
        idx = self._hash(key)
        i = 0
        added = 1
        while self.keys[self._probe(idx, i)] is not None:
            pos = self._probe(idx, i)
            if self.keys[pos] == key and not self.deleted_flags[pos]:
                self.deleted_flags[pos] = True
                self.values[pos] = None
                self.count -= 1
                return True
            i += added ** 2
            added += 1
        return False

    def __str__(self):
        return '\n'.join([
            table_term(self, k)
            for k, deleted in zip(self.keys, self.deleted_flags)
            if k is not None and not deleted
        ])


def hash_table_from_terms(terms):
    table = HashTable()
    for term, definition in terms.items():
        table.set(term, definition)
    return table
