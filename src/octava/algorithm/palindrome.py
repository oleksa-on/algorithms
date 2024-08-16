def palindrome_string_what_to_delete(s):
    """
    Function that calculates how much chars must be deleted from given string use the rest of the chars
    to build palindrome string.

    Hint: A set of characters can form a palindrome if at most one character occurs an odd number of times and
    all characters occur an even number of times.


    :param s: string to analyze
    :return: int : number of chars that must be removed from given string.
    """
    result = 0
    len_s = len(s)
    if len_s > 1:
        sorted_s = sorted(s)
        set_of_chars = set(sorted_s)
        num_of_odd_occurrences = 0
        for char in set_of_chars:
            if sorted_s.count(char) % 2 > 0:
                num_of_odd_occurrences += 1
        if num_of_odd_occurrences == 1:
            result = 0
        elif num_of_odd_occurrences > 1:
            result = num_of_odd_occurrences - 1
    return result
