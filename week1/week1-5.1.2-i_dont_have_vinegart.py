import random
import datetime


def rand_year(first_date, second_date):
    """This function takes two dates as a range, finds a random date
        between those two dates, and returns it

        :param first: this is the start date (start range)
        :param second: this is the end date (end range)
        :returns: a random date inside that date
    """

    time_range = second_date - first_date
    days_range = time_range.days
    random_day = random.randrange(days_range)
    random_date = first_date + datetime.timedelta(days=random_day)
    return random_date

def main():
    NO_VINEGAR_MSG = "I DON'T HAVE VINEGART"
    MONDAY_MSG = "IT'S NOT MONDAY"
    MONDAY = 0
    first_day = input("Please enter a date in this format YYYY-MM-DD:").split('-')
    second_day = input("Please enter another date in this format YYYY-MM-DD:").split('-')
    first_date = datetime.date(int(first_day[0]), int(first_day[1]), int(first_day[2]))
    second_date = datetime.date(int(second_day[0]), int(second_day[1]), int(second_day[2]))
    if rand_year(first_date, second_date).weekday() == MONDAY:
        print(NO_VINEGAR_MSG)
    else:
        print(MONDAY_MSG)


if __name__ == '__main__':
    main()