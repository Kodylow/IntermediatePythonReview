# Random: pseudorandom
import random

random.seed(1) # sets reproducible random data seed

a = random.random # random float 0 to 1
a = random.uniform(0,10)
a = random.randint(1,10) # includes upper bound
a = random.randrange(1,10) # excludes upper bound
a = random.normalvariate(0,1)

my_list = list("ABCDEFGH")
print(my_list)
a = random.choice(my_list)
a = random.sample(my_list, 3) # always picks unique elements
a = random.choices(my_list, k=3) # can pick same element multiple times

random.shuffle(my_list)


# Secrets: cryptographic randomness, only 3 funcs
import secrets

a = secrets.randbelow(10) # excludes upper bound
a = secret.randbits(4)
a = secets.choice(my_list)


# Random with numpy, for rand arrays
# uses different random library than python std lib, seed is completely different between the 2
import numpy as np

# rand 3x3 array
a = np.random.rand(3, 3)

# low, high, dimensions (3x4)
a = np.random.randint(0,10, (3,4))

np.random.shuffle(arr) # only shifts first dimension
