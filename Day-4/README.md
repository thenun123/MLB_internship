# 📘 Day 4 – Conditional Statements, Loops & Problem Solving

## 🗂️ Folder Structure

```
Day-4/
├── conditional_statements/
│   ├── 01_positive_negative_zero.py
│   ├── 02_even_or_odd.py
│   ├── 03_grade_calculator.py
│   ├── 04_largest_of_three.py
│   └── 05_leap_year.py
├── loops/
│   ├── 01_print_1_to_100.py
│   ├── 02_even_numbers_1_to_100.py
│   ├── 03_sum_1_to_n.py
│   ├── 04_multiplication_table.py
│   └── 05_count_digits.py
├── logic_building/
│   ├── 01_reverse_number.py
│   ├── 02_palindrome_check.py
│   ├── 03_fibonacci_sequence.py
│   ├── 04_prime_check.py
│   └── 05_primes_1_to_100.py
├── mini_challenge/
│   └── number_analysis_tool.py
├── bonus_challenge/
│   └── menu_driven_app.py
└── README.md
```

---

## 🧠 Concepts Learned Today

### ✅ Conditional Statements
| Concept | Description |
|--------|-------------|
| `if` | Execute a block only if a condition is True |
| `if-else` | Choose between two paths |
| `if-elif-else` | Multiple conditions checked in sequence |
| Nested conditions | Conditions inside conditions |
| `and`, `or`, `not` | Logical operators to combine conditions |

### ✅ Loops
| Concept | Description |
|--------|-------------|
| `for` loop | Iterate over a sequence or range |
| `while` loop | Repeat while a condition is True |
| `break` | Exit a loop early |
| `continue` | Skip current iteration and move to next |
| Nested loops | Loops inside loops (used in multiplication tables) |

### ✅ Problem-Solving Approach
1. Understand the problem clearly
2. Write the logic in plain English
3. Break into smaller steps
4. Convert steps into code

---

## 📝 Problems Solved

### Conditional Statements
1. ✅ Check whether a number is positive, negative, or zero
2. ✅ Check whether a number is even or odd
3. ✅ Grade calculator based on marks (A+ to F)
4. ✅ Find the largest among three numbers
5. ✅ Check whether a year is a leap year

### Loops
1. ✅ Print numbers from 1 to 100 (10 per row)
2. ✅ Print all even numbers from 1 to 100
3. ✅ Calculate sum of numbers from 1 to N (with formula verification)
4. ✅ Print multiplication table of a given number
5. ✅ Count the number of digits in a number

### Logic Building
1. ✅ Reverse a number (handles negatives)
2. ✅ Check whether a number is a palindrome
3. ✅ Generate Fibonacci sequence for N terms
4. ✅ Check whether a number is prime (efficient square-root method)
5. ✅ Find all primes between 1–100 (Sieve of Eratosthenes)

### Mini Challenge
✅ **Number Analysis Tool** — Complete analysis of any integer:
- Even or Odd
- Prime check
- Digit count
- Reversed number
- Palindrome check

### Bonus Challenge
✅ **Menu-Driven Math Toolkit** — Runs continuously until user exits:
- Option 1: Prime Number Checker
- Option 2: Fibonacci Series Generator
- Option 3: Palindrome Checker
- Option 4: Multiplication Table Generator
- Option 5: Exit

---

## ⚙️ Sample Output

### Number Analysis Tool
```
==================================================
       🔢  NUMBER ANALYSIS TOOL  🔢
==================================================

Enter an integer to analyze: 121

==================================================
  Analysis Report for: 121
==================================================

  ▸ Even / Odd       : Odd ✅
  ▸ Prime Number     : No ❌
  ▸ Number of Digits : 3
  ▸ Reversed Number  : 121
  ▸ Palindrome       : Yes ✅ (reads same both ways!)

==================================================
         ✅ Analysis Complete!
==================================================
```

### Fibonacci (5 terms)
```
Fibonacci (5 terms):
0 -> 1 -> 1 -> 2 -> 3
```

### Prime Sieve Output (1–100)
```
All Prime Numbers between 1 and 100:
==================================================
   2   3   5   7  11  13  17  19  23  29
  31  37  41  43  47  53  59  61  67  71
  73  79  83  89  97
==================================================
Total prime numbers between 1 and 100: 25
```

---

## 🚧 Challenges Faced

1. **Leap year logic** — Easy to miss the rule that years divisible by 100 are NOT leap years unless also divisible by 400 (e.g., 1900 is not a leap year, but 2000 is).
2. **Prime checking efficiency** — Checking all divisors up to `n` is slow. Switching to checking only up to `√n` makes it significantly faster.
3. **Reversing negative numbers** — Had to handle the sign separately before reversing.
4. **Sieve of Eratosthenes** — Understanding why we start marking from `p*p` (not `2*p`) requires careful thinking about what's already been marked.

---

## 💡 Lessons Learned

- Always think about **edge cases** (zero, negative numbers, single digits).
- The **square root trick** for prime checking is a must-know optimization.
- `range(start, stop, step)` is very powerful — using `range(2, 101, 2)` directly gives all even numbers without an if-check.
- Functions make code **reusable** — the `is_prime()` function was written once and used in three different programs.
- **Modular thinking** (breaking problems into functions) is the foundation of clean, professional code.
- The Sieve of Eratosthenes is far more efficient than checking each number individually when finding all primes in a range.

---

## 📅 Date
**June 24, 2026**

> *"The ability to think through problems is one of the most valuable skills an engineer can develop."*
