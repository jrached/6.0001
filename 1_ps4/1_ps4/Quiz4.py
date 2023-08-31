# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 04:15:23 2020

@author: tutov
"""

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

class Rectangle(object):
    def __init__(self, coord, width, height):
        """
        width and height are positive numbers
        
        Initializes self, a Rectangle with `coord` as its top-left corner,
        with `width` as the horizontal side length, and `height` as the 
        vertical side length. If `coord` is not an instance of a Coordinate, 
        the top-left corner is initialized to a Coordinate object at <0,0>.
        """
        # your code here
        if isinstance(coord, Coordinate):
            self.coord = coord
        else:
            self.coord = Coordinate(0,0)
        
        self.width = width
        self.height = height
        self.bottomRight = Coordinate(coord.x + width, coord.y - height)
        
    def get_width(self):
        """ Returns the width of self.  """
        # your code here
        return self.width
    
    def get_height(self):
        """ Returns the height of self.  """
        # your code here
        return self.height
    
    def get_area(self):
        """ Returns the area of self. """
        # your code here 
        return self.height*self.width
    
    def set_width(self, w):
        """ Sets the width of self to w """
        # your code here
        self.width = w
        
    def set_height(self, h):
        """ Sets the height of self to h """
        # your code here
        self.height = h
        
    def get_top_left(self):
        """ Returns the top-left corner as a Coordinate object. """
        # your code here
        return self.coord
    
    def get_bottom_right(self):
        """ Returns the bottom-right corner as a Coordinate object. """
        # your code here
        return self.bottomRight
    
class RectangleWithOps(Rectangle):
    
    def __init__(self, coord, width, height):
        Rectangle.__init__(self, coord, width, height)
        
    def smaller(self, other):
        """
        self and other are Rectangles
        Returns the area of the smaller Rectangle object. 
        """
        
        # your code here
        if self.get_area() < other.get_area():
            return self.get_area()
        else:
            return other.get_area()
    
    def scale(self, x):
        """
        self is a Rectangle object
        If x is a positive float or int, changes the size of self so that
        each side is x times longer, and returns None. Otherwise, raises
        a ValueError exception.
        """
        # your code here
        try:
            self.height = x*self.height
            self.width = x*self.width
        except:
            raise TypeError(str(x) + "is not a possitive float or int")
