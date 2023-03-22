import random
import datetime


def rand_year(first, second):
    """This function takes two dates as a range, finds a random date
        between those two dates, and returns it

        :param first: this is the start date (start range)
        :param second: this is the end date (end range)
        :returns: a random date inside that date
    """

    time_range = second - first
    days_range = time_range.days
    rand_day = random.randrange(days_range)
    rand_date = first + datetime.timedelta(days=rand_day)
    return rand_date


first = input("Please enter a date in this format YYYY-MM-DD:").split('-')
second = input("Please enter another date in this format YYYY-MM-DD:").split('-')
first_date = datetime.date(int(first[0]), int(first[1]), int(first[2]))
second_date = datetime.date(int(second[0]), int(second[1]), int(second[2]))
if rand_year(first_date, second_date).weekday() == 0:
    print("I DON'T HAVE VINEGAR!")
else:
    print("its not monday..")