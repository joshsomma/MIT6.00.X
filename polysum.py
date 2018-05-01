"""
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: 

(0.25 * n * s**2) / (tan(pi/n))

The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
"""

from math import pi, tan

def polysum(n,s):
    """
    n - number of sides in the polygon
    s - length of each side

    returns: sum of the perimeter and area of a given polygon to 4 decimal places
    """
    # calculate perimeter
    perimeter = n * s
    # calculate area
    area = (0.25 * n * s**2) / (tan(pi/n))
    # return sum of area and perimeter squared
    return round(area + perimeter**2,4)
