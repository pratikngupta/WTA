#!/usr/bin/env python3

"""
Name: Pratik Narendra Gupta
Program: Software Engineering - 3rd year


Question 1:
Example:
Input:
cartridges = 10
dollars = 10
recycleReward = 2, the amount earned by recycling a single cartridge
perksCost = 2 the amount required for a customer to buy a single perk product combined with a recycled cartridge.
Output:
7
Explanation:
The customer can first recycle 3 cartridges, earning 6 dollars. After this, 7 cartridges and 16 dollars left. The 7 cartridges can be combined with 14 dollars to purchase 14 dollars to purchase 7 perk items.

Example:
Input:
cartridges = 4
dollars = 8
recycleReward = 3, the amount earned by recycling a single cartridge
perksCost = 4, the amount required for a customer to buy a single perk product combined with a recycled cartridge.
Output:
2
Explanation:
The customer can combine cartridges with 8 dollars to buy 2 perk products.

"""


def maximum_perk_products(cartridges, money, recycle_reward, perks_cost):
    total_perks = 0

    # calculate the total perks we can buy with the money and cartridges we have
    for i in range(cartridges):
        # if we have enough money to buy the perks
        if money >= perks_cost:
            cartridges = cartridges - 1
            money = money - perks_cost
            total_perks += 1

        # if we don't have enough money to buy the perks, then we can recycle the cartridges to get more money,
        # make it based on the recycle reward
        elif cartridges >= 2:
            cartridges = cartridges - 1
            money = money + recycle_reward

    return total_perks


if __name__ == '__main__':
    # Test examples
    # input 1 and 2 are given in the question
    print("Input 1: cartridges = 10, money = 10, recycle_reward = 2, perks_cost = 2")
    print("Maximum Perks:", maximum_perk_products(10, 10, 2, 2))  # Output: 7
    print()

    print("Input 2: cartridges = 4, money = 8, recycle_reward = 3, perks_cost = 4")
    print("Maximum Perks:", maximum_perk_products(4, 8, 3, 4))  # Output: 2
    print()

    # input 3, 4 and 5 are my own test examples
    print("Input 3: cartridges = 50, money = 100, recycle_reward = 5, perks_cost = 10")
    print("Maximum Perks:", maximum_perk_products(50, 100, 5, 10))  # Output: 23
    print()

    print("Input 4: cartridges = 0, money = 100, recycle_reward = 5, perks_cost = 10")
    print("Maximum Perks:", maximum_perk_products(0, 100, 5, 10))  # Output: 0
    print()

    print("Input 5: cartridges = 10, money = 10, recycle_reward = 5, perks_cost = 10")
    print("Maximum Perks:", maximum_perk_products(10, 0, 5, 10))  # Output: 3
    print()


# what is the time complexity of this solution?
# O(n)

# what is the space complexity of this solution?
# O(1)

# Describe the approach taken to solve this problem
# I have used a while loop to calculate the total perks we can buy with the money and cartridges we have.
# I have used if and elif statements to check if we have enough money to buy the perks or not.
# If we don't have enough money to buy the perks, then we can recycle the cartridges to get more money,
# make it based on the recycle reward.
# I have used a return statement to return the total perks we can buy with the money and cartridges we have.
