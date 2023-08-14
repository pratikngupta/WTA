"""
Name: Pratik Narendra Gupta
Program: Software Engineering - 3rd year

Question 3
There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n),
some houses that has been painted last summer should not be painted again.
A neighborhood is a maximal group of continuous houses that are painted with the same color.
(For example: houses = [1,2,1,3,3,2,1,4,2], neighborhood 1 = [1], neighborhood 2 = [2], neighborhood 3 = [3,3], neighborhood 4 = [4]).
Given an array houses, an m * n matrix cost and an integer target where:
houses[i]: is the color of the house i, 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j+1.
Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods,
if not possible return -1.
"""

check = True # check variable to check if all test cases pass

def minCost(houses, cost, m, n, target):
    memo = {}  # Memoization cache

    # using dfs to find the minimum cost
    def dfs(index, target, preColor):
        if target == -1 or index + target > m:
            return float("inf")
        if index == m:
            return 0
        if (index, target, preColor) in memo:
            return memo[(index, target, preColor)]

        if houses[index] != 0:
            result = dfs(index + 1, target if houses[index] == preColor else target - 1, houses[index])
        else:
            result = min(
                dfs(index + 1, target if j + 1 == preColor else target - 1, j + 1) + cost[index][j] for j in range(n))

        memo[(index, target, preColor)] = result
        return result

    ans = dfs(0, target, -1)
    return ans if ans != float("inf") else -1


def test_case(case):
    example = case[0]
    houses = case[1]
    cost = case[2]
    m = case[3]
    n = case[4]
    target = case[5]
    solution = case[6]
    output = minCost(houses, cost, m, n, target)

    print(example)
    print("House:", houses)
    print("Cost:", cost)
    print("Target:", target)
    print("Output:", output)

    if output == solution:
        print("Status: Pass")
    else:
        print("Status: Fail")
        check = False

    print()


def main():
    test_case(case=(
    "Example 1: Given in the question", [0, 0, 0, 0, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3, 9))
    test_case(case=(
    "Example 2: Given in the question", [0, 2, 1, 2, 0], [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], 5, 2, 3, 11))

    # other test cases to test the solution
    test_case(case=("Example 3: No painting is possible as all as all house are painted", [3, 1, 2, 3],
                    [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]], 4, 3, 3, -1))
    test_case(case=(
    "Example 4: More neighbor than what is possible", [0, 0, 0], [[1, 10, 3], [10, 1, 3], [1, 10, 3]], 3, 3, 4, -1))
    test_case(case=("Example 5: Less color/price than it is possible", [0, 0, 0, 0, 0], [[1, 10, 3]], 3, 3, 5, -1))


if __name__ == '__main__':
    main()
    if check:
        print("All test cases passed")
    else:
        print("Some test cases failed")

# what is the time complexity of the above solution?
# O(m*n*target)

# what is the space complexity of the above solution?
# O(m*n*target)

# can we do better?
# yes, we can use dynamic programming to solve this problem.
# we can use a 3D array to store the results of the subproblems.
