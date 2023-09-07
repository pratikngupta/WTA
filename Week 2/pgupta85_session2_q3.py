#!/usr/bin/env python3

"""
Name: Pratik Narendra Gupta
Program: Software Engineering - 3rd year


Question 3:

Given two strings s and t, return an array of all the start indices of t's anagrams in s. You may return the answer in any order. 
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 

Example:
Input: 
s = "cbaebabacd"
t = "abc"
Output:
[0, 6]

Example:
Input: 
s = "abab"
t = "ab"
Output:
[0, 1, 2]
"""


## USING ord():
### What is ord()?: It is built-in Python function that returns the Unicode code point for the given Unicode character.
### ord('a') returns 97, and so on...

def find_anagrams(s, t):
    # fist check if the lenght of "s" is less than "t", if this is case then there csn be no anagrams
    if len(s) < len(t):
        return []

    # Initialize the fixed-size array for character counting
    char_count_t = [0] * 26
    char_count_window = [0] * 26

    # I am creating a array to compare string "s" and "t"
    # Count characters in target string t
    for char in t:
        char_count_t[ord(char) - ord('a')] += 1
        # ord() function is used to convert a character to its corresponding integer value. For example,
        # ord('a') returns 97, and so on. We can use this to map each character to a unique index in the fixed-size
        # array.

    # Initialize the list to store the indices of anagrams
    result = []

    # Initialize the start and end pointers of the sliding window
    start = 0
    end = 0

    while end < len(s):
        # Expand the window by adding the character at the end pointer to the char_count_window
        char_count_window[ord(s[end]) - ord('a')] += 1

        # If the window size becomes equal to the target string's length, check for anagrams
        if end - start + 1 == len(t):
            # If the current window's character frequencies match the target's frequencies, it's an anagram
            if char_count_window == char_count_t:
                result.append(start)

            # Shrink the window by moving the start pointer
            char_count_window[ord(s[start]) - ord('a')] -= 1
            start += 1

        end += 1

    return result


if __name__ == '__main__':
    # Test examples

    # Input 1 and 2 are given in the question
    print("Input 1 (given): s = 'cbaebabacd', t = 'abc'")
    print("Output 1: ", find_anagrams("cbaebabacd", "abc"))
    print()

    print("Input 2 (given): s = 'abab', t = 'ab'")
    print("Output 2: ", find_anagrams("abab", "ab"))
    print()

    # input 3, 4 and 5 are my own examples
    print("Input 3: s = 'ghfbcnfhefhhr', t = 'hf'")
    print("Output 3: ", find_anagrams("ghfbcnfhefhhr", "hf"))
    print()

    print("Input 4: s = 'abab', t = 'abab'")
    print("Output 4: ", find_anagrams("abab", "abab"))
    print()

    print("Input 5: s = 'abab', t = 'g'")
    print("Output 5: ", find_anagrams("abab", "g"))
    print()

# What is ord()?: It is built-in Python function that returns the Unicode code point for the given Unicode character.

# What is time complexity of this solution?
# The time complexity of this solution is O(n), where n is the length of the string s.

# What is space complexity of this solution? The space complexity of this solution is O(1), since we are using a
# fixed-size array of length 26 to store the character counts.

# What is the advantage of using ord()? The ord() function is used to convert a character to its corresponding
# integer value. For example, ord('a') returns 97, and so on. We can use this to map each character to a unique index
# in the fixed-size array. This way, we can avoid using a hashmap to store the character counts. This reduces the
# space complexity of the solution from O(n) to O(1).

# What is the disadvantage of using ord()?
# The ord() function is not very intuitive. It is not immediately clear what ord('a') returns.
# This makes the code harder to understand and maintain.
# Also, the ord() function is not available in other programming languages, so this solution is not portable.
