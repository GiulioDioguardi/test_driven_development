#!/usr/bin/python


def length_of_longest_substring(s):
    """
    Return the length of the longest substring without repeating characters
    in string s
    """
    def compare():
        return max(cur_length, longest_substring)

    longest_substring = 0
    cur_substring = ""
    for c in s:
        if c in cur_substring:
            cur_length = len(cur_substring)
            longest_substring = compare()
            cur_substring = c
        else:
            cur_substring += c
    return compare()
