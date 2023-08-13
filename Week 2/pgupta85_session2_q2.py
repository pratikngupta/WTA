#!/usr/bin/env python3
"""
Name: Pratik Narendra Gupta
Program: Software Engineering - 3rd year


Question 2:

Given a string s, determine if it is cool.

A string s is cool if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:
Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
Return true if s is a cool string, otherwise, return false.

Example: 
Input: s = "aabcbc" 
Output: true 
Explanation: "" -> "abc" -> "aabcbc" Thus, "aabcbc" is valid.
"""


# create a function to check for the cool string:

def check_cool_string(s):
    # first we need to check if the string is empty or not
    if len(s) == 0 or s[0] != 'a' or s[-1] != 'c':
        return False

    # creating a stack
    stack = []

    # using for loop to illiterate through every character in string "s"
    for char in s:

        # checking if current character is "c"
        if char == 'c':

            # If current character is c, then check if previous 2 character store in stack is a and b
            if stack and stack[-2:] == ['a', 'b']:

                # If so, then pop them out of the stack, this is equal to removing abc from string as we are not
                # adding c to the stack
                stack.pop()
                stack.pop()

            # if not, then this string is not a cool string, stop the process and return false immediately
            else:
                return False

        # if current char is not "c", then we add them to stack to be compare with when we have "c".
        else:
            stack.append(char)

    # if stack lenght is zero at the end, then string is cool, otherwise it would be false.
    return len(stack) == 0


if __name__ == '__main__':
    # Test examples

    # input 1 and 2 are given in the question
    print("Input 1 (given): abcabc" + "\nOutput: ", check_cool_string("abcabc"))  # Output: True
    print()

    print("Input 2 (given): abccba" + "\nOutput: ", check_cool_string("abccba"))  # Output: False
    print()

    # input 3, 4 and 5 are my own examples
    print("Input 3: aabcbc" + "\nOutput: ", check_cool_string("aabcbc"))  # Output: True
    print()

    print("Input 4: aababccababcabccabcaabcbcbabcabcc" + "\nOutput: ", check_cool_string("aababccababcabccabcaabcbcbabcabcc"))  # Output: True
    print()

    print("Input 5: aababccababcabccabcaabcbcbabcabc" + "\nOutput: ", check_cool_string("aababccababcabccabcaabcbcbabcabc"))  # Output: False

# what is time complexity of this solution?
# Time complexity: O(n) as we are transversing the string just once.

# what is space complexity of this solution?
# Space complexity: O(n) as we are using stack to store the characters of string "s".

# what is the most efficient solution? The most efficient solution is the stack-based solution as it is most
# efficient and we would have to transerse the string just once.
