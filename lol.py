class Hash_Table:
    def __init__(self, size = 7):
        self.data_map = [None]*size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash+ord(letter)*23)%len(self.data_map)
        return my_hash

    def insert(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0]==key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    def printTable(self):
        for i, val in enumerate(self.data_map):
            print(f'{i}:{val}')

ht1 = Hash_Table()
ht1.printTable()
print(ht1.data_map)
print('=========')
ht1.insert('bolts', 1200)
ht1.insert('washers', 1000)
ht1.insert('lumber', 2000)
ht1.printTable()
print(ht1.get('lumber'))
print(ht1.keys())