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

def main():
    FIRST_PARAM = 'AB'
    SECOND_PARAM = [1,2]
    THIRD_PARAM = ('!', '@')
    result = interleave(FIRST_PARAM, SECOND_PARAM, THIRD_PARAM)
    print(list(result))


if __name__ == "__main__":
    main()