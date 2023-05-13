import random
numbers = set()
while len(numbers) < 6:

    x = random.randint(1, 49)
    numbers.add(x)


print(numbers)
