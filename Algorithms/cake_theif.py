#!/usr/bin/python
import sys
from time import time

ct= [(7,160), (3,90), (2,15), (50,15), (10,1), (1, 5), (6, 140)]
cap = 20

def max_duffle_bag_value(cake_tuples, capacity):

    while (0,0) in cake_tuples:
        cake_tuples.pop(cake_tuples.index((0,0)))

    try:
        price_per_pound = [(cake[1]/cake[0], cake[1], cake[0]) for cake in cake_tuples]
        print price_per_pound
    except ZeroDivisionError:
        #return sys.maxint
        return "Infinite"
    bag_value = 0

    while len(price_per_pound) > 0:
        most_valueable_cake = max(price_per_pound)
        print most_valueable_cake
        bag_value += capacity/most_valueable_cake[2]*most_valueable_cake[1]
        capacity %= most_valueable_cake[2]
        print capacity
        price_per_pound.pop(price_per_pound.index(most_valueable_cake))

    return bag_value

print max_duffle_bag_value(ct, cap)