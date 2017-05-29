"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.
def is_bries_hometown(name_of_town):
    """ Take in the name of a city and evaluate if it matches Brie's hometown

    >>> is_bries_hometown("San Mateo")
    False

    >>> is_bries_hometown("Foster City")
    True

    """
    return name_of_town.lower() == "foster city"


#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.
def name_in_one_string(first_name, last_name):
    """ Take two arguments and return them as one string

    >>> name_in_one_string("Brianne", "Kodakari")
    'Brianne Kodakari'

    """
    return first_name + " " + last_name


#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.
def who_are_you_and_where_are_you_from(home_town, first_name, last_name):
    """ Take in the name and hometown of a user, see if they are from Brie's hometown and print a statement to Brie.
    >>> who_are_you_and_where_are_you_from("Foster City", "Brianne", "Kodakari")
    Hi, Brianne Kodakari, we're from the same place!

    >>> who_are_you_and_where_are_you_from("San Mateo", "Brianne", "Kodakari")
    Hi Brianne Kodakari, I'd like to visit Foster City!

    """
    player1 = name_in_one_string(first_name, last_name)
    if is_bries_hometown(home_town) is True:
        print "Hi, %s, we're from the same place!" % (player1)
    else:
        print "Hi %s, I'd like to visit Foster City!" % (player1)

###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry", or
#        "blackberry."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a number and a list of numbers. It should
#        return a new list containing the elements of the input list, along with
#        given number, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax, and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price under $100 and $3 for items $100 or more. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.


def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """

    return "berry" in fruit


def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """

    if is_berry(fruit) is True:
        return 0
    if is_berry(fruit) is False:
        return 5


def append_to_list(lst, num):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    """
    lst.append(num)
    return lst


def calculate_price(base_price, state_abbrv, tax_rate=.05):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """

    if state_abbrv.lower() == "ca":
        tax = float(base_price) * tax_rate
        base_plus_tax = float(base_price) + tax
        recycling_fee = base_plus_tax * .03
        total_price = recycling_fee + base_plus_tax
        return total_price
    # above formatting is easier to read, but performs the same as below
    # if state_abbrv.lower() == "ca":
    #     return ((((float(base_price)*tax_rate))+base_price)*.03) + ((float(base_price)*tax_rate)+base_price)
    if state_abbrv.lower() == "pa":
        return (float(base_price)*tax_rate)+base_price+2
    if state_abbrv.lower() == "ma":
        if float(base_price) < 100:
            return (float(base_price)*tax_rate)+base_price+1
        if float(base_price) >= 100:
            return (float(base_price)*tax_rate)+base_price+3
    else:
        return (float(base_price)*tax_rate)+base_price


###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.
def adding_multiple_numbers_to_a_list(lst, *num):
    """ Take a list of integers and an unlimited number of additional integers and append the additional integers to the input list.

    >>> adding_multiple_numbers_to_a_list([1, 2, 3, 4], 5, 6, 7, 8, 9)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

     """
    # found the arbitrary argument answer on stack overflow (sited below)
    # https://stackoverflow.com/questions/919680/can-a-variable-number-of-arguments-be-passed-to-a-function
    additional_arguments = list(num)
    for number in additional_arguments:
        lst.append(number)
    return lst


#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')
def outer_function(word):
    """ Take in a word and print a tuple showcasing that word and that word * 3 using the word_by_three function

    >>> outer_function("Balloonicorn")
    ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

    """
    new_tup = (word, word_by_three(word))
    print new_tup


def word_by_three(word):
    """ Take in an argument as a string and return it 3 times.

    >>> word_by_three("apple")
    'appleappleapple'
    """
    return word * 3


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
