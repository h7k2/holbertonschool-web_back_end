📘 Python - Async Comprehension

This project introduces asynchronous generators, async comprehensions, and parallel execution using asyncio.
You will learn how to create async sequences, collect asynchronous data, and measure performance when running tasks concurrently.

🚀 Learning Objectives

By the end of this project, you should be able to explain:

What an asynchronous generator is and how to write one

How to use async comprehensions

How to type-annotate async generators and coroutines

How to run multiple async tasks in parallel with asyncio.gather

🛠️ Requirements

Python 3.9 (Ubuntu 20.04)

pycodestyle 2.5

All files must:

start with #!/usr/bin/env python3

end with a new line

contain proper documentation (module + function docstrings)

be fully type-annotated

Allowed editors: vi, vim, emacs

📂 Tasks Overview
0. Async Generator

Write a coroutine async_generator() that:

loops 10 times

waits 1 second asynchronously each time

yields a random number between 0 and 10

Used to produce asynchronous values that other coroutines can consume.

1. Async Comprehension

Write a coroutine async_comprehension() that:

imports async_generator()

uses an async comprehension to collect 10 values:

[i async for i in async_generator()]


returns the list of 10 numbers.

This demonstrates how to consume asynchronous iterators in one clean Python expression.

2. Run Time for Four Parallel Comprehensions

Write a coroutine measure_runtime() that:

runs async_comprehension() four times in parallel using:

asyncio.gather(...)


measures the total runtime

returns the elapsed time as a float

Because all four are executed concurrently, the total time is ~10 seconds, not 40.

📑 Files Included
0-async_generator.py
1-async_comprehension.py
2-measure_runtime.py
README.md

📘 Summary

This project teaches how to:

create asynchronous data streams

use async comprehensions to collect async values

leverage concurrency to improve execution time

apply proper documentation and type hinting

A solid introduction to modern Python asynchronous programming.
