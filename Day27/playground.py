def add(*args):
    #args is an implementation of an unlimited positional argument
    #*args collects all of the arguments into a tuple
    return sum(args)

print(add(1,3,4,1))


def calculate(n, **kwargs):
    #**kwargs creates unlimited keyword arguments
    #
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

