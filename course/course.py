class course:
    def __init__(self, name, value, assigned=False):
        self.name = name
        self.profs = []
        self.value = value
        self.assigned = assigned
        
    def set_value(self, x):
        self.value -= x
        if(self.value < 0):
            self.assigned = True
            
    def get_assigned(self):
        return self.assigned
    
    def set_prof(self, prof):
        self.profs.append(prof)