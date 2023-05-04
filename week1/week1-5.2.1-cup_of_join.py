def join(*lists, sep='-'):
    """
    this function recieves a number of lists, could be none, unites them into one string
    yet they are seperated by the sep variable. and returns the result
    :param *lists: any amount of lists
    :param sep: seperator variable, default '-' if not provided by user
    :return: return None if no lists were provided, or the result of the concatenated lists"""

    if not lists:
        return None
    result = []
    for lst in lists:
        result += lst
        result.append(sep)
    result.pop()

    return result


def main():
    print(join())


if __name__ == "__main__":
    main()
