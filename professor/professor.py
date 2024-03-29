class Professor(object):
    def __init__(self, name, value, pref, assigned=False):
        self.name = name
        self.value = [value]
        self.pref = pref
        self.assigned = [assigned]
       
    def set_value(self, x, i):
        self.value[i] -= x
        if(self.value[i] <= 0):
            self.assigned[i] = True


    def get_assigned(self, i):
        return self.assigned[i]
    
    def remove_value(self, x):
        self.value.pop(x)
        self.assigned.pop(x)
    
class x1(Professor):
    def __init__(self,name,pref):
        Professor.__init__(self,name,0.5,pref,assigned=False)
    def append_value(self,x):
        self.value.append(0.5)
        self.value[len(self.value) - 1] -= x
        if(self.value[len(self.value) - 1] <= 0):
            self.assigned.append(True)
        else:
            self.assigned.append(False)

class x2(Professor):
    def __init__(self,name,pref):
        Professor.__init__(self,name,1, pref,assigned=False)
    def append_value(self,x):
        self.value.append(1)
        self.value[len(self.value) - 1] -= x
        if(self.value[len(self.value) - 1] <= 0):
            self.assigned.append(True)
        else:
            self.assigned.append(False)

class x3( Professor):
    def __init__(self,name,pref):
        Professor.__init__(self,name,1.5, pref,assigned=False)
    
    def append_value(self,x):
        self.value.append(1.5)
        self.value[len(self.value) - 1] -= x
        if(self.value[len(self.value) - 1] <= 0):
            self.assigned.append(True)
        else:
            self.assigned.append(False)
