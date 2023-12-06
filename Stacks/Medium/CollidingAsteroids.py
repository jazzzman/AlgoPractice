"""
  DESCRIPTION

    You're given an array of integers asteroids,
    where each integer represents the size of an asteroid.
    The sign of the integer represents the direction the asteroid
    is moving (positive = right, negative = left). All asteroids
    move at the same speed, meaning that two asteroids moving in the same direction can never collide.


    For example, the integer 4 represents an asteroid
    of size 4 moving to the right. Similarly, -7 represents
    an asteroid of size 7 moving to the left.


    If two asteroids collide, the smaller asteroid (based on absolute value) explodes.
    If two colliding asteroids are the same size, they both explode.


    Write a function that takes in this array of asteroids and returns
    an array of integers representing the asteroids after all collisions occur.



  Time complexity O(###)
  Space complexity O(###)
"""
import pytest


def collidingAsteroids(asteroids):
    output = []
    
    while asteroids:
        if len(output)==0:
            output.append(asteroids.pop(0))
            continue

        while output:
            if output[-1]>0 and asteroids[0]<0:
                if output[-1]<abs(asteroids[0]):
                    output.pop()
                elif output[-1]==abs(asteroids[0]):
                    output.pop()
                    asteroids.pop(0)
                else:
                    asteroids.pop(0)



    return output

# case [asteroids, expected]
cases = [
    [[5], [5]],
    [[-5], [-5]],
    [[5, -5], []],
    [[-5, 5], [-5, 5]],
    [[-5, -5], [-5, -5]],
    [[5, 5], [5, 5]],
    [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]],
    [[34, 2, 5, 42, 100, 20], [34, 2, 5, 42, 100, 20]],
    [[-6, -2, -10, -100, -30], [-6, -2, -10, -100, -30]],
    [[1, 2, 3, -4], [-4]],
    [[4, -1, -2, -3], [4]],
    [[-3, 7, -8, 6, 7, -5, -7], [-3, -8, 6]],
    [[4, -5, -5, -5], [-5, -5, -5]],
    [[6, -5, -5, -5], [6]],
    [[4, 7, -3, -5, 6, -10, 100, -50, 99], [-10, 100, 99]],
    [[-70, 100, 23, 42, -50, -75, 1, -2, -3], [-70, 100]],
    [[-70, 10, 23, 42, -50, -75, 1, -2, -3], [-70, -50, -75, -2, -3]],
    [[42, 30, 12, 65, -50, 32, -15, -25], [42, 30, 12, 65, 32]],
    [[5123, -34, 654, -3636, 2432, 4242, 1267, 1337, -43, -864, 38, 38, 1, -400], [5123, 2432, 4242, 1267, 1337]],
    [[651, 13, -1246, 754, 1252, -300, 5468, -5200, 22, 17, -100, 87, 100, -250, 1], [-1246, 754, 1252, 5468, 1]]
]

@pytest.mark.parametrize("asteroids, expected", cases)
def test_collidingAsteroids(asteroids, expected):
    assert collidingAsteroids(asteroids)==expected

