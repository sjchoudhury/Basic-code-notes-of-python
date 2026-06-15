# 🐍 Python Basics — Code Notes

A personal collection of beginner-to-intermediate Python scripts, organized by topic.  
Built while learning Python from scratch — covering core concepts, practice exercises, and small projects.

---

## 📁 Folder Structure

```
python-notes/
│
├── 01_basics/          → Data types, conditions, type conversion, try/except
├── 02_loops/           → for loops, while loops, break, continue, FizzBuzz
├── 03_strings/         → Slicing, library functions, parsing, vowel checks
├── 04_functions/       → Defining functions, return values, recursion, pay problems
├── 05_lists_and_dicts/ → List operations, sorting, duplicates, matrices, dict
├── 06_patterns/        → Star/hash pattern printing using nested loops
├── 07_oop/             → Classes, objects, methods (student, circle, temperature)
└── 08_mini_projects/   → Calculator, number guessing game, month name converter
```

---

## 📂 Contents

### 01_basics
| File | What it covers |
|---|---|
| `hello_world.py` | First Python print statement |
| `data_types.py` | int, float, string — and how to check type |
| `type_conversion.py` | int() and float() conversion |
| `float_to_int.py` | Converting float to int with type display |
| `user_input_string.py` | Taking string input from user |
| `user_input_number.py` | Taking number input and doing arithmetic |
| `conditions_positive_negative.py` | if/elif/else — positive, negative, zero |
| `conditions_multi.py` | Multiple condition branches |
| `nested_conditions.py` | Nested if statements + nested for loop example |
| `logical_operators.py` | `in`, `not in` operators on strings |
| `or_truth_table.py` | OR operator truth table example |
| `try_except_basic.py` | Basic try/except with division |

### 02_loops
| File | What it covers |
|---|---|
| `for_loop_basic.py` | Simple for loop over a list |
| `for_loop_range.py` | range(), step values, loop over list |
| `while_loop_basic.py` | Simple while loop with counter |
| `break_example.py` | Breaking a while loop with keyword |
| `continue_example.py` | Skipping iterations with continue |
| `filter_in_loop.py` | Filtering values in a loop (if inside for) |
| `search_in_loop.py` | Searching for a value in a loop |
| `while_division.py` | While loop with modulo condition |
| `loop_assignment.py` | Running total — loop + try/except |
| `sum_with_loop.py` | Sum of a list + sum of odd numbers |
| `average_with_loop.py` | Average using a for loop |
| `count_elements.py` | Counting number of elements in a list |
| `fizzbuzz.py` | Classic FizzBuzz problem |
| `running_total_try_except.py` | Running total with error handling |

### 03_strings
| File | What it covers |
|---|---|
| `string_basics.py` | String indexing, len(), type checking |
| `string_slicing.py` | Slicing syntax [start:end:step], reverse string |
| `string_library_functions.py` | isupper(), islower(), lower(), upper() |
| `strip_whitespace.py` | lstrip(), rstrip(), strip() |
| `loop_through_string.py` | Iterating over characters, counting letters |
| `parsing_extracting.py` | find() + slicing to extract substrings |
| `string_find_slicing_assignment.py` | Extract float from a formatted string |
| `vowel_checker.py` | Check which characters are vowels |
| `vowel_count.py` | Count vowels in a sentence |
| `remove_vowels.py` | Remove all vowels from a string |

### 04_functions
| File | What it covers |
|---|---|
| `functions_basics.py` | def, parameters, *args, keyword args, return, recursion |
| `default_arguments.py` | Default parameter values |
| `return_value.py` | Function returning a value |
| `factors.py` | Find all factors of a number |
| `factorial.py` | Factorial using while loop |
| `add_two_numbers.py` | Simple addition with user input |
| `rate_per_day.py` | Pay = days × rate |
| `pay_with_overtime.py` | Pay calculation with overtime logic |
| `pay_try_except.py` | Pay calculation with input validation |

### 05_lists_and_dicts
| File | What it covers |
|---|---|
| `list_basics.py` | Creating and printing a list |
| `list_length.py` | Using len() on a list |
| `list_last_element_type.py` | Getting last element and its data type |
| `reverse_list.py` | reversed() function |
| `largest_value.py` | Finding the largest value with a loop |
| `smallest_value.py` | Finding the smallest value |
| `maximum_ternary.py` | Max of two numbers using ternary operator |
| `second_largest.py` | Sort and find second largest |
| `duplicate_elements.py` | Find duplicates using a dictionary |
| `dictionary_basics.py` | Creating and accessing a dictionary |
| `matrix_multiplication.py` | Multiply two 3×3 matrices with nested loops |

### 06_patterns
| File | What it covers |
|---|---|
| `patterns_all.py` | Multiple patterns — hash, number, diamond, space patterns |
| `hash_pattern.py` | Right-triangle hash pattern |
| `star_pattern_with_space.py` | Star pattern with blank line spacing |

### 07_oop
| File | What it covers |
|---|---|
| `student_class.py` | Class with `__init__`, methods, multiple objects |
| `circle_class.py` | Class with math (area, circumference) |
| `temperature_class.py` | Celsius ↔ Fahrenheit conversion class |

### 08_mini_projects
| File | What it covers |
|---|---|
| `calculator.py` | 4-operation calculator with functions |
| `calculator_extended.py` | Calculator + sign checker (extended version) |
| `guess_the_number_game.py` | Random number guessing game with 7 attempts |
| `month_name.py` | Number to month name converter (1–12) |

---

## ⚠️ Known Bugs (for learning reference)

| File | Bug |
|---|---|
| `function1.py` | `greet` is called as `greet` but defined as `grret` — NameError |
| `functionassignmentsol.py` / `q2.py` | Indentation missing inside function body |
| `functionnum.py` | Uses `--` instead of `==` in condition |
| `doubt.py` | Syntax errors — `for i range` missing `in`, and `end(ls)` should be `len(ls)` |
| `largestvalue1.py` | `print('Before', the largest_so_far)` — space in variable name |
| `smallvalue.py` | `small = 1` should be `small = i` inside elif |
| `round-1.py` | `mathdegrees(radians)` should be `math.degrees(radians)` + missing import |
| `week04day02q2.py` | `circumference5()` should be `circumference()` |
| `q1.py` | `hour` variable used but never defined |
| `fizzbuzz.py` | else only attached to second if — Fizz+Buzz case not handled properly |

---

## 🚀 How to Run

```bash
python 01_basics/hello_world.py
```

Requires Python 3.x. No external libraries needed except `random` (built-in) and `math` (built-in).

---

*Uploaded daily as part of a beginner Python learning journey.*
