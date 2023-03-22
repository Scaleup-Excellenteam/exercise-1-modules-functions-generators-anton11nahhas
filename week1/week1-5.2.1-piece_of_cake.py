def get_recipe_price(prices, optionals=[], **ingredients):
    """
    this function receives a dictionary of prices, and optional list and another
    dict ingredients, it calculates the total prices according to data given.
    the function first deletes any ingredients found in optionals since we are
    not including them in the calculations, then loops through the new items and
    calculates the total price according the amounts given.

    :param prices: a dictionary were the keys are the ingredients and the values are the prices
    :param optionals: an optional param, if its empty then include all the ingredients in the
                    calculations, if not remove all the ingredients found in optionals.
    :param ingredients: another dictionary were the key is the ignredient and the value is the
                    amount in grams we need to buy/calculate.
    :return : the function returns the total prices.
    """

    total_price = 0
    if not prices:
        return 0
    if not optionals == []:
        for recipe in list(prices.items()):
            if optionals.count(recipe) > 0:
                del prices[recipe]
    for recipe in prices:
        for ing, amount in ingredients.items():
            if ing == recipe:
                total_price += prices[recipe] * amount / 100

    return total_price


print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))