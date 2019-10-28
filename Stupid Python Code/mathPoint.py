import math 
class Point:
    def __init__(self, p):
        self.x = p[0]
        self.y = p[1]

class Line:
    def __init__(self, m, n):
        self.m = m
        self.n = n

        self.sortedX = [m.x, n.x]
        self.sortedX.sort()
        self.sortedY = [m.y, n.y]
        self.sortedY.sort()

        
        

    def onLine(self,c):
        if(not self.sortedX[0] <= c.x <= self.sortedX[1]):
            return False
        elif(not self.sortedY[0] <= c.y <= self.sortedY[1]):
            return False
        
        if(self.m.x == self.n.x):
            return c.x == self.m.x


        slope = (self.m.y - self.n.y)/(self.m.x - self.n.x)
        b = self.m.y-slope*self.m.x
        return (slope*c.x + b == c.y)

    def midpoint(self):
        return Point(((self.m.x + self.n.x)/2, (self.m.y + self.n.y)/2))
    def len(self):
        return math.sqrt((self.m.x-self.n.x)**2 + (self.m.y-self.n.y)**2)

    def intersects(self, l): 
        return self.intersect(l)
            
    def ccw(self,A,B,C):
        return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

    def intersect(self,l):
        return self.ccw(self.m, l.m, l.n) != self.ccw(self.n, l.m, l.n) \
               and self.ccw(self.m,self.n,l.m) != self.ccw(self.m,self.n,l.n)
