class Professor(object):
    def __init__(self, name, value, pref):
        self.name = name
        self.value = value
        self.pref = pref


class x1(Professor):
    def __init__(self,name,pref):
        Professor.__init__(self,name,0.5,pref)

class x2(Professor):
    def __init__(self,name,pref):
        Professor.__init__(self,name,1, pref)

class x3( Professor):
    def __init__(self,name,pref):
        Professor.__init__(self,name,1.5, pref)
