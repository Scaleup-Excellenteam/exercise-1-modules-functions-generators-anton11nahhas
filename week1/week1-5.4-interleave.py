def interleave(*lists):
    """
        this function receives a tuple of strings of the same size,
        the function takes a member from each list and yields it so
        we can get a new list if each member is different from one
        another when traversing the list.
        :param *lists: a tuple of lists with the same size
        :return: the function doesn't return anything however it yields
                the results.
    """

    iterator = 0
    size = max(map(len, lists))

    for iteration in range(size):
        for list in lists:
            yield list[iterator]
        iterator += 1


result = interleave('ab', [1, 2], ('!', '@'))
print(list(result))