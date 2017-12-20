#!/usr/bin/python


def length_of_longest_substring(s):
    longest_substring = 0
    current_substring = ""
    for c in s:
        if c in current_substring:
            current_length = len(current_substring)
            longest_substring = max(current_length, longest_substring)
            current_substring = c
        else:
            current_substring += c
    return max(current_length, longest_substring)
