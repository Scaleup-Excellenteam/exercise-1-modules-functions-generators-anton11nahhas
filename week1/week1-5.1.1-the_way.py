import os


def the_way(path):
    """This function receives a path and check if theres a file inside that directory
        the path is leading to that starts with deep

        :param path: the path of a certain directory
        :returns: a list of files that accomplish the goal of the function
    """

    WANTED_WORD = 'deep'
    FIRST_FOUR_LETTERS = 4

    result_lst = []
    for file_name in os.listdir(path):
        if file_name[:FIRST_FOUR_LETTERS].lower() == WANTED_WORD:
            result_lst.append(file_name)
    return result_lst


def is_valid_directory(path):
    """This function receives a directory path and checks if it exists and is a directory.

    :param path: The directory path to check.
    :returns: True if the path is a valid directory, False otherwise.
    """
    return os.path.isdir(path)

def main():
    ERROR_MSG = 'The path you provided is invalid'
    INPUT_MESSAGE = 'Please enter a path: '
    given_dir = input(INPUT_MESSAGE)
    if is_valid_directory(given_dir):
        the_way(given_dir)
    else:
        print(ERROR_MSG)

if __name__ == '__main__':
    main()


