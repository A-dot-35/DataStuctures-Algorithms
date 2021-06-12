class HashEntry:
    def __init__(self, key, data) -> None:
        # Key for entry
        self.key = key 
        # Data to be stored
        self.data = data 
        # Reference to new entry
        self.next = None
    
    def __str__(self) -> str:
        return str(self.key) + ', ' + self.value

