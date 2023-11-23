class course:
    def __init__(self, name, profs, value):
        self.name = name
        self.profs = profs
        self.value = value

    def get_value(self):
        return self.value
        
    def set_value(self, x):
        self.value -= x