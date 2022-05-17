# class Generic:
#     def __init__(self):
#         self._x = 10

#     def getter(self):
#         return self._x

#     def setter(self, value):
#         self._x = value

#     def deleter(self):
#         del self._x

#     x = property(getter,setter,deleter)


    
# generic = Generic()
# generic.x = 4
# print('generic.x: ', generic.x)
# del generic.x


class Generic:
    def __init__(self):
        self._x = 10
        
    @property
    def x(self):
        return self._x    
    
    # @x.getter
    # def x(self):
    #     return self._x
    @x.setter
    def x(self, value):
        self._x = value
        
    @x.deleter
    def x(self):
        del self._x


    
generic = Generic()
generic.x = 4
print('generic.x: ', generic.x)
del generic.x