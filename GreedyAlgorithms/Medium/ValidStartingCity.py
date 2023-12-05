"""
  DESCRIPTION

  Imagine you have a set of cities that are laid out in a circle, connected by a
  circular road that runs clockwise. Each city has a gas station that provides  
  gallons of fuel, and each city is some distance away from the next city.      


  You have a car that can drive some number of miles per gallon of fuel, and    
  your goal is to pick a starting city such that you can fill up your car with  
  that city's fuel, drive to the next city, refill up your car with that city's 
  fuel, drive to the next city, and so on and so forth until you return back to 
  the starting city with 0 or more gallons of fuel left.


  This city is called a valid starting city, and it's guaranteed that there will
  always be exactly one valid starting city.


  For the actual problem, you'll be given an array of distances such that city  
  i is distances[i] away from city i + 1.
  Since the cities are connected via a circular road, the last city is connected
  to the first city. In other words, the last distance in the
  distances array is equal to the distance from the last city to
  the first city. You'll also be given an array of fuel available at each city, 
  where fuel[i] is equal to the fuel available at city
  i. The total amount of fuel available (from all cities combined)
  is exactly enough to travel to all cities. Your fuel tank always starts out   
  empty, and you're given a positive integer value for the number of miles that 
  your car can travel per gallon of fuel (miles per gallon, or MPG). You can    
  assume that you will always be given at least two cities.

  Write a function that returns the index of the valid starting city.

  Time complexity O(###)
  Space complexity O(###)
"""
import pytest


def validStartingCity(distances, fuel, mpg):
    start_point = 0
    tank = 0
    miles_candidate = 0
    for idx in range(1, len(distances)):
        tank += fuel[idx-1] - distances[idx-1]/mpg
        if tank<miles_candidate:
            start_point = idx
            miles_candidate = tank

    return start_point


# case [distances, fuel, mpg, expected]
cases = [
    [[5, 25, 15, 10, 15], [1, 2, 1, 0, 3], 10, 4],
    [[10, 20, 10, 15, 5, 15, 25], [0, 2, 1, 0, 0, 1, 1], 20, 1],
    [[30, 25, 5, 100, 40], [3, 2, 1, 0, 4], 20, 4],
    [[1, 3, 10, 6, 7, 7, 2, 4], [1, 1, 1, 1, 1, 1, 1, 1], 5, 6],
    [[5, 2, 3], [1, 0, 1], 5, 2],
    [[4, 6], [1, 9], 1, 1],
    #[[30, 40, 10, 10, 17, 13, 50, 30, 10, 40], [1, 2, 0, 1, 1, 0, 3, 1, 0, 1], 25, 1], # work well
    [[30, 40, 10, 10, 17, 13, 50, 30, 10, 40], [10, 0, 0, 0, 0, 0, 0, 0, 0, 0], 25, 0],
    [[15, 20, 25, 30, 35, 5], [0, 3, 0, 0, 1, 1], 26, 5],
    [[10, 10, 10, 10], [1, 2, 3, 4], 4, 2]
]

@pytest.mark.parametrize("distances, fuel, mpg, expected", cases)
def test_validStartingCity(distances, fuel, mpg, expected):
    assert validStartingCity(distances, fuel, mpg)==expected

