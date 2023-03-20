import os


def the_way(path):
    """This function receives a path and check if theres a file inside that directory
        the path is leading to that starts with deep

        :param path: the path of a certain directory
        :returns: a list of files that accomplish the goal of the function
    """

    result_lst = []
    for file_name in os.listdir(path):
        if file_name[:4].lower() == "deep":
            result_lst.append(file_name)
    return result_lst


the_way(input("Please enter a path:"))
