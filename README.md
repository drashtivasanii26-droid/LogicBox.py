# 📊 Logic Box – Pattern Generator and Number Analyzer

 **Author:** Drashti Vasani


A Python-based console application designed to generate simple star patterns and analyze a range of numbers by identifying whether each number is **Even or Odd** and calculating the **sum of all numbers** in the selected range.

---

## 🎯 Project Objectives

* ⭐ **Pattern Generation:** Generate a star pattern based on the number of rows entered by the user.
* 🔢 **Number Analysis:** Analyze numbers within a user-defined range.
* 🔍 **Even/Odd Detection:** Identify whether each number is Even or Odd.
* 🧮 **Sum Calculation:** Calculate the sum of all numbers in the selected range.
* 💻 **Interactive Menu:** Provide a simple console-based menu for user interaction.

---

## ✨ Features & Functionality

### 1. ⭐ Pattern Generator

The program allows the user to enter the number of rows and generates a simple star pattern.

For example, if the user enters `5`:

```text
*
**
***
****
*****
```

The pattern is generated using:

```python
for i in range(1, n + 1):
    print("*" * i)
```

### 2. 🔢 Analyze a Range of Numbers

The program allows the user to enter a starting and ending number.

It then checks every number in the selected range and displays whether the number is **Even** or **Odd**.

Example:

```text
Number 1 is Odd
Number 2 is Even
Number 3 is Odd
Number 4 is Even
Number 5 is Odd
```

### 3. 🧮 Sum of Numbers

The program also calculates the total sum of all numbers within the selected range.

The calculation is performed using:

```python
total = total + num
```

---

## 💻 Technologies Used

* Python 3
* Visual Studio Code
* Git & GitHub

---


---

## 📂 Project Files

```text
Logic-Box/
│
├── Logic_Box.py
├── README.md
└── output.png
```

---

## 🖥️ Sample Output

```text
Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 1
Enter number of rows: 4
*
**
***
****

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 2
Enter the start of the range: 10
Enter the end of the range: 15
Number 10 is Even
Number 11 is Odd
Number 12 is Even
Number 13 is Odd
Number 14 is Even
Number 15 is Odd
Sum of all numbers from 10 to 15 is: 75

Select an option:
1. Generate a Pattern
2. Analyze a Range of Numbers
3. Exit
Enter your choice: 3
Exiting the program. Goodbye!
```

---

