"""
  DESCRIPTION

  You're given a string of length 12 or smaller, containing only digits. Write a
  function that returns all the possible IP addresses that can be created by    
  inserting three .s in the string.


  An IP address is a sequence of four positive integers that are separated by   
  .s, where each individual integer is within the range
  0 - 255, inclusive.


  An IP address isn't valid if any of the individual integers contains leading  
  0s. For example, "192.168.0.1" is a valid IP
  address, but "192.168.00.1" and
  "192.168.0.01" aren't, because they contain "00" and
  01, respectively. Another example of a valid IP address is
  "99.1.1.10"; conversely, "991.1.1.0" isn't valid,
  because "991" is greater than 255.


  Your function should return the IP addresses in string format and in no       
  particular order. If no valid IP addresses can be created from the string,    
  your function should return an empty list.


  Note: check out our Systems Design Fundamentals on SystemsExpert to learn more
  about IP addresses!


  Time complexity O(###)
  Space complexity O(###)
"""
import pytest


def validIPAddresses(string):
    ips = []
    for group1 in range(3):
        for group2 in range(group1+1, group1+4):
            for group3 in range(group2+1, group2+4):
                candidate = [string[0:group1+1], string[group1+1:group2+1], string[group2+1:group3+1], string[group3+1:]]
                if all([validGroup(part) for part in candidate]):
                    ips.append('.'.join(candidate))

    return ips

def validGroup(string):
    if not string or int(string)>255:
        return False

    if len(string)>1:
        if string[0] == '0':
            return False

    return True

# case [string, expected]
cases = [
    ['1921680', ['1.9.216.80', '1.92.16.80', '1.92.168.0', '19.2.16.80', '19.2.168.0', '19.21.6.80', '19.21.68.0', '19.216.8.0', '192.1.6.80', '192.1.68.0', '192.16.8.0']],
    ['3700100', ['3.70.0.100', '37.0.0.100']],
    ['9743', ['9.7.4.3']],
    ['97430', ['9.7.4.30', '9.7.43.0', '9.74.3.0', '97.4.3.0']],
    ['997430', ['9.9.74.30', '9.97.4.30', '9.97.43.0', '99.7.4.30', '99.7.43.0', '99.74.3.0']],
    ['255255255255', ['255.255.255.255']],
    ['255255255256', []],
    ['99999999', ['99.99.99.99']],
    ['33133313', ['33.13.33.13', '33.133.3.13', '33.133.31.3']],
    ['00010', ['0.0.0.10']],
    ['100100', ['1.0.0.100', '10.0.10.0', '100.1.0.0']],
    ['1072310', ['10.7.23.10', '10.7.231.0', '10.72.3.10', '10.72.31.0', '107.2.3.10', '107.2.31.0', '107.23.1.0']],
    ['1', []],
    ['11', []],
    ['111', []],
    ['00001', []]
]

@pytest.mark.parametrize("string, expected", cases)
def test_validIPAddresses(string, expected):
    assert validIPAddresses(string)==expected
