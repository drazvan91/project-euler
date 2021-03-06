# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

import math


def generate_triangle_number():
    sum = 0
    add = 1
    while True:
        sum += add
        yield sum
        add += 1


def number_of_divisors(number):
    sqrt = math.floor(math.sqrt(number))
    count = 2
    for i in range(2, sqrt+1):
        if number % i == 0:
            count += 2
            if i == sqrt:
                count -= 1

    return count


def find_triangle_with_minimum_divisors(minimum_divisors):
    for triangle in generate_triangle_number():
        divisors = number_of_divisors(triangle)
        if divisors > minimum_divisors:
            return (triangle, divisors)


print(find_triangle_with_minimum_divisors(500))
