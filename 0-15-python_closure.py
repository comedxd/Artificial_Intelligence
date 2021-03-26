"""
Closures can avoid the use of global values and provides some form of data hiding.
It can also provide an object oriented solution to the problem.
When there are few methods (one method in most cases) to be implemented in a class,
closures can provide an alternate and more elegant solution.
But when the number of attributes and methods get larger, it's better to implement a class.
"""

def make_multiplier_of(n):  # n is non local varaible for 'multiplier' function
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)      # n=3

# Multiplier of 5
times5 = make_multiplier_of(5)  # n=5

# Output: 27
print(times3(9))                # x=9

# Output: 15
print(times5(3))                # x=3

# Output: 30
print(times5(times3(2)))        #=x=2 then 5*3*2