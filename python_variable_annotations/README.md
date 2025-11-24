Python - Variable Annotations

This project introduces type hinting in Python, a feature added in Python 3 to improve code clarity, tooling support, and static type checking.
You will implement functions and variables using precise annotations and work with advanced types such as unions, callables, tuples, and iterables.

🔍 What You Will Learn

How to annotate variables, parameters, and return types

How to use the typing module (List, Tuple, Union, Callable, Iterable, etc.)

What duck typing means in Python

How to run mypy to validate type correctness

Why type hints improve maintainability in large codebases

🧾 Project Requirements

Python 3.9 on Ubuntu 20.04

Files must be executable

First line: #!/usr/bin/env python3

Code must follow pycodestyle 2.5

All modules, classes, and functions must include proper docstrings

A README.md is mandatory

Length of files will be validated

📌 Mandatory Tasks Overview
0. add(a, b)

Takes two floats → returns their sum (float).

1. concat(str1, str2)

Concatenates two strings.

2. floor(n)

Returns the integer floor value of a float.

3. to_str(n)

Converts a float to its string representation.

4. Define annotated variables

You will explicitly annotate:

an integer

a float

a boolean

a string

5. sum_list(input_list)

Accepts a list of floats → returns their sum as a float.

6. sum_mixed_list(mxd_lst)

Handles a list of ints and floats → returns their sum.

7. to_kv(k, v)

Returns a tuple where:

the first element is the string k

the second is the square of v as a float

8. make_multiplier(multiplier)

Returns a function that multiplies a float by the given multiplier.

9. element_length(lst)

Uses duck typing to annotate an iterable of sequences.
Returns a list of tuples: (item, length_of_item).

🧠 Why This Matters

Type hints are optional in Python, but they dramatically improve:

readability

debugging

IDE autocompletion

large project scalability

error detection before runtime

This project prepares you for more advanced typing concepts used in production code, APIs, and enterprise-level Python development.
