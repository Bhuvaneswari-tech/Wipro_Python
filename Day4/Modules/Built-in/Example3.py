#random module

import random

#Random integer
print("Random integer between 1 and 10:",
      random.randint(1,10))

#Random float
print("Random float between 0 and 1:",
      random.random())

#random choice from list
colors = ["red","blue","green","yellow"]
print("Randome color:",random.choice(colors))

#shuffle a list
numbers = [1,2,3,4,5]
random.shuffle(numbers)
print("shuffled numbers:",numbers)

#random sample from list
print("Random 2 numbers:",random.sample(numbers,2))