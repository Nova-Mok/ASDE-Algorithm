# Abhimanyu Chakravyuh Algorithm

This Python script implements an algorithm to determine if Abhimanyu can successfully cross the Chakravyuh in the Mahabharata epic.

## Description

In this scenario, Abhimanyu must cross 11 circles of the Chakravyuh, each guarded by an enemy with different power levels. The algorithm takes into account Abhimanyu's initial power, his ability to skip battles, and his capacity to recharge his power. It also considers special conditions for enemies in the 3rd and 7th circles.

## Features

- Simulates Abhimanyu's journey through 11 circles of the Chakravyuh
- Handles Abhimanyu's power management, including skips and recharges
- Accounts for regenerating enemies in specific circles
- Includes test cases to verify the algorithm's functionality

## Usage

To run the script:

1. Ensure you have Python installed on your system.
2. Save the script as `abhimanyu_chakravyuh.py`.
3. Run the script using the command:

## Function Parameters

The main function `can_abhimanyu_cross_chakravyuh` takes the following parameters:

- `p`: Abhimanyu's initial power
- `a`: Number of times Abhimanyu can skip fighting an enemy
- `b`: Number of times Abhimanyu can recharge his power
- `enemy_powers`: A list of 11 integers representing the power of enemies in each circle

## Test Cases

The script includes two test cases:

1. Abhimanyu with high initial power and more skips/recharges
2. Abhimanyu with lower initial power and fewer skips/recharges

You can modify or add more test cases in the `test_abhimanyu_chakravyuh` function.

## Output

The module will print the result for each test case, indicating whether Abhimanyu can successfully cross the Chakravyuh or not.

## Customization

You can easily add more test cases or modify the existing ones by updating the `test_cases` list in the `test_abhimanyu_chakravyuh` function.

