def randomNums(num, maxShingle_id):
    import random
    # Create a list of 'k' random values.
    randList = []
    while num > 0:
        # Get a random shingle ID.
        randIndex = random.randint(0, maxShingle_id)
        # Ensure that each random number is unique.
        while randIndex in randList:
            randIndex = random.randint(0, maxShingle_id)
            # Add the random number to the list.
        randList.append(randIndex)
        num = num - 1
    return randList
