"""
  DESCRIPTION

  A tandem bicycle is a bicycle that's operated by two people: person A and     
  person B. Both people pedal the bicycle, but the person that pedals faster    
  dictates the speed of the bicycle. So if person A pedals at a speed of        
  5, and person B pedals at a speed of 4, the tandem
  bicycle moves at a speed of 5 (i.e.,
  tandemSpeed = max(speedA, speedB)).


  You're given two lists of positive integers: one that contains the speeds of  
  riders wearing red shirts and one that contains the speeds of riders wearing  
  blue shirts. Each rider is represented by a single positive integer, which is 
  the speed that they pedal a tandem bicycle at. Both lists have the same       
  length, meaning that there are as many red-shirt riders as there are
  blue-shirt riders. Your goal is to pair every rider wearing a red shirt with a
  rider wearing a blue shirt to operate a tandem bicycle.


  Write a function that returns the maximum possible total speed or the minimum 
  possible total speed of all of the tandem bicycles being ridden based on an   
  input parameter, fastest. If fastest = true, your
  function should return the maximum possible total speed; otherwise it should  
  return the minimum total speed.


  "Total speed" is defined as the sum of the speeds of all the tandem bicycles  
  being ridden. For example, if there are 4 riders (2 red-shirt riders and 2    
  blue-shirt riders) who have speeds of 1, 3, 4, 5, and if they're
  paired on tandem bicycles as follows: [1, 4], [5, 3], then the
  total speed of these tandem bicycles is 4 + 5 = 9.


  Time complexity O(nlogn)
  Space complexity O(n)
"""
import pytest


def tandemBicycle(blueShirtSpeeds, fastest, redShirtSpeeds):
    blueShirtSpeeds.sort()
    redShirtSpeeds.sort()

    if fastest:
        return sum([max(blue, red) for blue, red in zip(blueShirtSpeeds, redShirtSpeeds[::-1])])
    else:
        return sum([max(blue, red) for blue, red in zip(blueShirtSpeeds, redShirtSpeeds)])


# case [blueShirtSpeeds, fastest, redShirtSpeeds, expected]
cases = [
    [[3, 6, 7, 2, 1], True, [5, 5, 3, 9, 2], 32],
    [[3, 6, 7, 2, 1], False, [5, 5, 3, 9, 2], 25],
    [[3, 3, 4, 6, 1, 2], False, [1, 2, 1, 9, 12, 3], 30],
    [[3, 3, 4, 6, 1, 2], True, [1, 2, 1, 9, 12, 3], 37],
    [[3, 3, 4, 6, 1, 2, 5, 6, 34, 256, 123, 32], True, [1, 2, 1, 9, 12, 3, 1, 54, 21, 231, 32, 1], 816],
    [[3, 3, 4, 6, 1, 2, 5, 6, 34, 256, 123, 32], False, [1, 2, 1, 9, 12, 3, 1, 54, 21, 231, 32, 1], 484],
    [[5], True, [1], 5],
    [[5], False, [1], 5],
    [[1, 1, 1, 1], True, [1, 1, 1, 1], 4],
    [[1, 1, 1, 1], False, [1, 1, 1, 1], 4],
    [[1, 1, 1, 1, 3, 3, 3, 3, 5, 7], True, [1, 1, 1, 1, 2, 2, 2, 2, 9, 11], 48],
    [[1, 1, 1, 1, 3, 3, 3, 3, 5, 7], False, [1, 1, 1, 1, 2, 2, 2, 2, 9, 11], 36],
    [[3, 4, 4, 1, 1, 8, 9], True, [9, 8, 2, 2, 3, 5, 6], 49],
    [[3, 4, 4, 1, 1, 8, 9], False, [9, 8, 2, 2, 3, 5, 6], 35],
    [[1, 2, 3, 4, 5], False, [5, 4, 3, 2, 1], 15],
    [[1, 2, 3, 4, 5], True, [5, 4, 3, 2, 1], 21],
    [[], True, [], 0]
]

@pytest.mark.parametrize("blueShirtSpeeds, fastest, redShirtSpeeds, expected", cases)
def test_tandemBicycle(blueShirtSpeeds, fastest, redShirtSpeeds, expected):
    assert tandemBicycle(blueShirtSpeeds, fastest, redShirtSpeeds)==expected

