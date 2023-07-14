# Given a string, find the longest palindromic substring.


# Define a helper function that checks whether a given string is a palindrome. This function will take a string as input and return a boolean value indicating whether the string is a palindrome or not.

import numpy as np


def is_palindrome(input_string):
    return input_string == input_string[::-1]


def longest_palindrome(s):
    n = len(s)
    if n < 2:
        return s

    # Create a table to store palindrome information
    is_palindrome = [[False] * n for _ in range(n)]

    # Initialize variables to track the longest palindrome substring
    start = 0
    max_length = 1

    # Every individual character is a palindrome of length 1
    for i in range(n):
        is_palindrome[i][i] = True

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            is_palindrome[i][i + 1] = True
            start = i
            max_length = 2

    # Check for palindromes of length greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                is_palindrome[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length

    # Extract the longest palindromic substring
    longest_palindrome = s[start:start + max_length]

    return longest_palindrome


# Test cases
input_string = "babad"
print("Input string:", input_string)
result = longest_palindrome(input_string)
print("Longest palindromic substring:", result)
print()

input_string = "cbbd"
print("Input string:", input_string)
result = longest_palindrome(input_string)
print("Longest palindromic substring:", result)
print()

input_string = "forgeeksskeegfor"
print("Input string:", input_string)
result = longest_palindrome(input_string)
print("Longest palindromic substring:", result)
print()
