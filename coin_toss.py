#The monte carlo simulation
from __future__ import division
from random import randint

heads = 0
tails = 0

for _ in range(10000):
    while randint(0, 1) == 0:
       tails += 1
    heads += 1

print("Heads / Tails", heads / tails) 