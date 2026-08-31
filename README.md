# LogicBox

**Author:** Drashti Vasani  
**Course/Project:** Python Practical Assignment

A Python-based menu-driven console application designed to practice control structures, loops (`for` and `while`), the `range()` function, and conditional statements.

## Project Objectives

- **Control Structures & Loops:** Implement `for` and `while` loops and range iterations.
- **Menu-Driven Interface:** Provide an interactive console menu allowing users to generate patterns, analyze numbers, or exit the program.
- **Logical Problem Solving:** Check whether numbers are Even or Odd and calculate the sum of numbers in a given range.

## Features & Functionality

### 1. Pattern Generator

- Generates a right-angled triangle pattern using asterisks (`*`).
- Allows the user to enter the number of rows.

**Example:**

```text
*
**
***
****
*****
```

### 2. Number Analyzer

- Takes a starting number and ending number from the user.
- Checks whether each number is Even or Odd.
- Calculates the sum of all numbers in the given range.

**Example:**

```text
Enter The Start Number To Start: 10
Enter The End Number To Stop: 15

Number 10 is Even
Number 11 is Odd
Number 12 is Even
Number 13 is Odd
Number 14 is Even
Number 15 is Odd

Sum of all numbers from 10 to 15 is: 75
```

### 3. Exit

- Allows the user to safely exit the program.
- Displays `Good Bye` when option 3 is selected.

## Menu Options

```text
Selected The Number
1. Generate a pattern
2. Number Analyzer
3. Exit
Enter The Choice of number 1 to 3:::: 
```

## Sample Output

```text
Selected The Number
1. Generate a pattern
2. Number Analyzer
3. Exit
Enter The Choice of number 1 to 3:::: 2

--- Number Analyzer ---

Enter The Start Number To Start: 10
Enter The End Number To Stop: 15

Number 10 is Even
Number 11 is Odd
Number 12 is Even
Number 13 is Odd
Number 14 is Even
Number 15 is Odd

Sum of all numbers from 10 to 15 is: 75

Selected The Number
1. Generate a pattern
2. Number Analyzer
3. Exit
Enter The Choice of number 1 to 3:::: 3

Good Bye
```

## Technologies Used

- Python 3
- VS Code
- Git & GitHub

## How to Run

1. Install Python.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python LogicBox.py
```

## Project Structure

```text
LogicBox/
│
├── LogicBox.py
└── README.md
```

## Author

**Drashti Vasani**