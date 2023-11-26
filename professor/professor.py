class Professor(object):
    def __init__(self, name, value, pref, assigned=False):
        self.name = name
        self.value = [value]
        self.pref = pref
        self.assigned = [assigned]
        self.assignments = [False]
       
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
    
class x1(Professor):
    def __init__(self,name,pref):
        Professor.__init__(self,name,0.5,pref,assigned=False)

class x2(Professor):
    def __init__(self,name,pref):
        Professor.__init__(self,name,1, pref,assigned=False)

class x3( Professor):
    def __init__(self,name,pref):
        Professor.__init__(self,name,1.5, pref,assigned=False)
