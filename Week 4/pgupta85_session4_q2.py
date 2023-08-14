#!/usr/bin/env python3

"""
Name: Pratik Narendra Gupta
Program: Software Engineering - 3rd year

Question 2

# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

check = True # check variable to check if all test cases pass
def rotten_oranges(grid):
    m = len(grid)
    n = len(grid[0])

    # find all rotten oranges
    rotten = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                rotten.append((i, j))

    # find all fresh oranges
    fresh = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                fresh.append((i, j))

    # if there are no fresh oranges, return 0
    if len(fresh) == 0:
        return 0

    # if there are no rotten oranges, return -1
    if len(rotten) == 0:
        return -1

    # if there are no fresh oranges and there are rotten oranges, return -1
    if len(fresh) == 0 and len(rotten) > 0:
        return -1

    # initialize the queue with the rotten oranges
    queue = []
    for i in range(len(rotten)):
        queue.append(rotten[i])

    # initialize the visited set with the rotten oranges
    visited = set()
    for i in range(len(rotten)):
        visited.add(rotten[i])

    # initialize the count variable to 0
    count = 0

    # while the queue is not empty
    while len(queue) > 0:

            # increment the count variable by 1
            count += 1

            # for each rotten orange in the queue
            for i in range(len(queue)):

                # remove the rotten orange from the queue
                rotten_orange = queue.pop(0)

                # get the neighbors of the rotten orange
                neighbors = get_neighbors(rotten_orange, grid)

                # for each neighbor of the rotten orange
                for j in range(len(neighbors)):

                    # if the neighbor is a fresh orange
                    if grid[neighbors[j][0]][neighbors[j][1]] == 1:

                        # if the neighbor has not been visited
                        if neighbors[j] not in visited:

                            # add the neighbor to the queue
                            queue.append(neighbors[j])

                            # add the neighbor to the visited set
                            visited.add(neighbors[j])

                            # set the neighbor to a rotten orange
                            grid[neighbors[j][0]][neighbors[j][1]] = 2

    # if there are fresh oranges, return -1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                return -1

    # return the count variable
    return count - 1

def get_neighbors(rotten_orange, grid):
    m = len(grid)
    n = len(grid[0])
    neighbors = []
    if rotten_orange[0] - 1 >= 0:
        neighbors.append((rotten_orange[0] - 1, rotten_orange[1]))
    if rotten_orange[0] + 1 < m:
        neighbors.append((rotten_orange[0] + 1, rotten_orange[1]))
    if rotten_orange[1] - 1 >= 0:
        neighbors.append((rotten_orange[0], rotten_orange[1] - 1))
    if rotten_orange[1] + 1 < n:
        neighbors.append((rotten_orange[0], rotten_orange[1] + 1))
    return neighbors

def test_function(test_case):
    grid = test_case[1]
    solution = test_case[2]
    example = test_case[0]

    print(example)
    print("Input: ")
    for i in range(len(grid)):
        print(grid[i])

    output = rotten_oranges(grid)

    print("Output: " + str(output))

    if output == solution:
        print("Status: Pass")
    else:
        print("Status: Fail")

    print()


def main():
    example = "Example 1: Given in the question"
    grid = [[2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]]

    solution = 4
    test_function(test_case=[example, grid, solution])

    example = "Example 2: Given in the question"
    grid = [[2, 1, 1],
            [0, 1, 1],
            [1, 0, 1]]
    solution = -1
    test_function(test_case=[example, grid, solution])

    example = "Example 3: Single rotten orange at the top left corner"
    grid = [[2, 1]]
    solution = 1
    test_function(test_case=[example, grid, solution])

    example = "Example 4: Single rotten orange at the top left corner"
    grid = [[2, 1, 1]]
    solution = 2
    test_function(test_case=[example, grid, solution])

    example = "Example 5: Single rotten orange at the top left corner"
    grid = [[2], [1], [1], [1]]
    solution = 3
    test_function(test_case=[example, grid, solution])

    example = "Example 6: No rotten oranges"
    grid = [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]]
    solution = -1
    test_function(test_case=[example, grid, solution])

    example = "Example 7: No fresh oranges"
    grid = [[2, 2, 2],
            [2, 2, 2],
            [2, 2, 2]]
    solution = 0
    test_function(test_case=[example, grid, solution])

    example = "Example 8: Testing Dignoally Adjacent Oranges"
    grid = [[2, 2, 2],
            [2, 2, 0],
            [2, 0, 1]]
    solution = -1
    test_function(test_case=[example, grid, solution])

if __name__ == '__main__':
    main()

    if check:
        print("All Tests Passed")
    else:
        print("Some Tests Failed")


