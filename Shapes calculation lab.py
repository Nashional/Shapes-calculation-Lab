import math


class Polygon:
    def __init__(self, nbr_sides):
        self.nbr_sides = nbr_sides

    def whoamI(self):
        if self.nbr_sides == 3:
            return "Triangle"
        elif self.nbr_sides == 4:
            return "Rectangle"
        else: return "Polygon"

    def howmanysides(self):
        return self.nbr_sides

    def area(self):
        return "No Area"

    def perimeter(self):
        return "No Perimeter"


class rectangle(Polygon):
    def __init__(self, breadth, length):
        Polygon.__init__(self, 4)
        self.breadth = breadth
        self.length = length

    def area (self):
        area= self.length * self.breadth
        return area

    def perimeter(self):
        perimeter = (2*(self.length + self.breadth))
        return perimeter


class triangle(Polygon):
    def __init__(self, a, b, c):
        Polygon.__init__(self, 3)
        self.a = a
        self.b = b
        self.c = c


    def perimeter(self):
        perimeter =(self.a + self.b + self.c)
        return perimeter


    def area(self):
        s = (self.a + self.b + self.c)/2.0
        calc_area = s*(s-self.a)*(s-self.b)*(s-self.c)
        return math.sqrt(calc_area)
    
def main():
    tri1 = triangle(2,2,2)
    rect = rectangle(2,3)
    tri2 = triangle(3,3,3)
    figures = [tri1,rect,tri2]
    for fig in figures:
        print ("Type of Polygon =>", fig.whoamI())
        print ("Sides =", fig.howmanysides())
        print ("Area =", fig.area())
        print ("Perimeter =", fig.perimeter())
main()
