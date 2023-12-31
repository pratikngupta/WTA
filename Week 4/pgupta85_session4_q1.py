#!/usr/bin/env python3

"""
Name: Pratik Narendra Gupta
Program: Software Engineering - 3rd year

Question 1
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or
move outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""

check = True  # check variable to check if all test cases pass


def longest_increasing_path(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(row, col):
        if dp[row][col] != -1:
            return dp[row][col]

        max_path = 1
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                max_path = max(max_path, 1 + dfs(new_row, new_col))

        dp[row][col] = max_path
        return max_path

    max_path = 0
    dp = [[-1 for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            max_path = max(max_path, dfs(row, col))

    return max_path


def test_function(test_case):
    # testing case given in the question
    print(test_case[0])
    matrix = test_case[1]
    # print the matrix in a more readable format
    for row in matrix:
        print(row)
    expected_output = test_case[2]
    output = longest_increasing_path(matrix)
    print("Input: matrix = ", matrix)
    print("Output: ", output)
    if output == expected_output:
        print("Status: Pass")
    else:
        print("Status: Fail")
        check = False
    print()


def main():
    test_function(test_case=("Testing case given in the question", [[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4))
    test_function(test_case=("Testing case given in the question", [[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4))
    test_function(test_case=("Example 3:", [[1]], 1))
    test_function(test_case=("Example 4:", [[1, 2]], 2))
    test_function(test_case=("Example 5:", [[1], [2]], 2))
    test_function(test_case=("Example 6:", [[1, 2], [3, 4]], 3))
    test_function(test_case=("Example 7:", [[1, 2], [4, 3]], 4))


if __name__ == "__main__":
    main()
    if check:
        print("All tests passed")
    else:
        print("Some tests failed")
