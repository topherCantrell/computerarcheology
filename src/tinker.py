class Point(object): #A point is x and y

    def __init__(self,x,y): #Takes in the initial x and y
        self._x = x #x stored in _x object
        self._y = y
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
def __repr__(self): #Representation method
    return '('+str(self._x)+','+str(self._y)+')'

p = Point(1,2)

print(p) #Output should be (1,2)