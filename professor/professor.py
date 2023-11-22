class Professor(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class x1(Professor):
    def __init__(self,name,value):
        Professor.__init__(self,name,0.5)

class x2(Professor):
    def __init__(self,name,value):
        Professor.__init__(self,name,1)

class x3( Professor):
    def __init__(self,name,value):
        Professor.__init__(self,name,1.5)


