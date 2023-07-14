# Longest Palindromic Substring
This repository contains a Python program that finds the longest palindromic substring in a given input string. It utilizes dynamic programming to efficiently determine the longest palindromic substring.
## Prerequisites:
To run the program, you need to have Python installed on your system. The program is written in Python 3.
## Usage:
1. Clone the repository to your local machine or download the program.py file.
2. Open a terminal or command prompt and navigate to the directory where the file is located.
3. Run the program by executing the following command:
  ```css
  python program.py
  ```
4. The program will execute and display the longest palindromic substring for each test case.

## Program Explanation
The program is structured into two functions: `is_palindrome` and `longest_palindrome`.

The `is_palindrome` function is a helper function that takes a string as input and checks whether it is a palindrome by comparing it with its reversed version. It returns `True` if the string is a palindrome and `False` otherwise.

The `longest_palindrome` function takes an input string and finds the longest palindromic substring within it. It utilizes a dynamic programming approach to efficiently determine the palindrome information for all possible substrings. The function initializes a boolean table `is_palindrome` to store the results of palindrome checks. It then iterates over the string to identify palindromes of length 1 and 2. After that, it checks for palindromes of length greater than 2, using the information from previously calculated palindromes. Finally, it extracts and returns the longest palindromic substring found.

The program includes some test cases at the end, demonstrating the usage of the `longest_palindrome` function. You can modify these test cases or add your own to verify the correctness of the program.

## Example Output
Below is an example of the output you can expect when running the program:
  ```mathematica
    Input string: babad
  Longest palindromic substring: bab

    Input string: cbbd
  Longest palindromic substring: bb

    Input string: forgeeksskeegfor
  Longest palindromic substring: geeksskeeg
  ```

The program correctly identifies the longest palindromic substrings for the given test cases.



Feel free to explore the code and use it as a reference for finding the longest palindromic substring in a string. If you have any questions or suggestions, please feel free to reach out.
