from HashEntry import HashEntry

class HashTable:
    def __init__(self) -> None:
        # Size of the HashTable
        self.slots = 10
        # Current entries in the table
        # Used to rezise table when half is filled
        self.size = 0
        # List of HashEntry objects 
        self.bucket = [None] * self.slots
        self.threshold = 0.6
    
    
    def get_index(self, key):
        hash_code = hash(key)
        index = hash_code % self.slots
        return index
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.get_size() == 0

    # Resize HashTable when threshold is reached
    def resize(self):
        new_slots = self.slots * 2
        new_bucket = [None] * new_slots

        # rehash all items into new table 
        for item in self.bucket:
            head = item
            while(head != None):
                new_index = hash(head.key) % new_slots
                if(new_bucket[new_index] == None):
                    new_bucket[new_index] = HashEntry(head.key,head.data)
                else:
                    node = new_bucket[new_index]
                    while(node != None):
                        if(node.key == head.key):
                            node.data = head.data
                            node = None
                        elif(node.next == None):
                            node.next = HashEntry(head.key,head.data)
                            node = None
                        else:
                            node = node.next
                head = head.next
        self.bucket = new_bucket
        self.slots = new_slots
        return

    # Insert key, value into HashTable
    def insert(self, key, data):
        b_index = self.get_index(key)
        if(self.bucket[b_index] == None):
            self.bucket[b_index] = HashEntry(key,data)
            print(key, "-", data, "inserted at index", b_index)
            self.size += 1
        else:
            head = self.bucket[b_index]
            while(head != None):
                if(head.key == key):
                    head.data = data
                    break
                elif(head.next == None):
                    head.next = HashEntry(key,data)
                    print(key, "-", data, "inserted at index", b_index)
                    self.size += 1
                head = head.next
        load_factor = float(self.size) / float(self.slots)
        if(load_factor >= self.threshold):
            self.resize()
        return
    
    # Search for a key in the HashTable
    def search(self,key):
        b_index = self.get_index(key)
        head = self.bucket[b_index]
        while(head != None):
            if(head.key == key):
                return head.data
            head= head.next
        return None
    
    def delete(self,key):
        b_index = self.get_index(key)
        head = self.bucket[b_index]

        if(head.key == key):
            self.bucket[b_index] = head.next
            print(key, "-", head.data, "deleted")
            # Decrease the size by one
            self.size -= 1
            return
        prev = None
        while(head != None):
            if(head.key == key):
                prev.next = head.next 
                print(key, "-", head.data, "deleted")
                self.size -= 1
                return
            prev = head 
            head = head.next
