"""Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.

The smallest perfect number is 6, which is the sum of 1, 2, and 3.

Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.

Write a function that finds perfect numbers between 1 and 1000. Check perfect numbers
between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions."""


from functools import reduce
def perfectnumber(number):
    """Function will ask that number is perfect number ?  """
    divisors = []
    for i in range(1,number):
        if number % i == 0 : 
            divisors.append(i)
    if number == reduce(lambda x,y : x+y ,divisors) :
        return True
    else :
        return False

print(list(filter(perfectnumber,range(2,1000))))