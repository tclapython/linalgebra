import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __ne__(self, v):
        return self.coordinates != v.coordinates

    def __add__(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)] 
        return Vector(new_coordinates)

    def __sub__(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, scalar):
        new_coordinates = [scalar * x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        return math.sqrt(sum([x*x for x in self.coordinates]))
        # teacher's version
        # coordinates_squared = [x**2 for x in self.coordinates] 
        # return math.sqrt(sum(coordinates_squared))

    def normalized(self):
        # MY version
        # return [x / self.magnitude() for x in self.coordinates]
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)
       
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector') 
