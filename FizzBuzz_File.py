import numpy as np

def FizzBuzz(start, finish):

    num = np.arange(start, finish + 1)

    v = np.array(num, dtype=object)

    fizz = (num % 3 == 0)
    buzz = (num % 5 == 0)

    v[fizz] = "fizz"
    v[buzz] = "buzz"
    v[fizz & buzz] = "fizzbuzz"

    return(v)
