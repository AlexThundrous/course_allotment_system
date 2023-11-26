class course:
    def __init__(self, name, value):
        self.name = name
        self.profs = {}
        self.value = [value]
        self.assigned = [False]
        self.avg = 0

    def set_value(self, x, i):
         self.value[i] -= x
         if(self.value[i] <= 0):
            self.assigned[i] = True

    def append_value(self,x):
        self.value.append(x)
        if(self.value[len(self.value) - 1] <= 0):
             self.assigned.append(True)
        else:
             self.assigned.append(False)

    def get_assigned(self, i):
        return self.assigned[i]
    
    def set_prof(self, prof, rank):
        self.profs[prof] = rank
    
    def set_avg(self):
        self.profs = dict(sorted(self.profs.items(), key=lambda item: item[1]))
        avg = int(sum(self.profs.values())/len(self.profs))
        sums = 0
        for key in self.profs:
            sums += self.profs[key] - avg
        self.avg = sums/len(self.profs)
