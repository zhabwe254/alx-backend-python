# Async Comprehension Project

This project focuses on asynchronous programming in Python, specifically using async generators and comprehensions.

## Requirements

### General
* Allowed editors: `vi`, `vim`, `emacs`
* All files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/env python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Code should use the `pycodestyle` style (version 2.5.x)
* The length of files will be tested using `wc`
* All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
* Documentation should be a real sentence explaining the purpose of the module, class, or method
* All functions and coroutines must be type-annotated

## Tasks

### 0. Async Generator
* File: `0-async_generator.py`
* Write a coroutine called `async_generator` that takes no arguments
* The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10
* Use the `random` module

### 1. Async Comprehensions
* File: `1-async_comprehension.py`
* Import `async_generator` from the previous task
* Write a coroutine called `async_comprehension` that takes no arguments
* The coroutine will collect 10 random numbers using an async comprehension over `async_generator`
* Return the 10 random numbers

### 2. Run time for four parallel comprehensions
* File: `2-measure_runtime.py`
* Import `async_comprehension` from the previous file
* Write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`
* `measure_runtime` should measure the total runtime and return it
* Notice that the total runtime is roughly 10 seconds, explain it to yourself

## Repository Information
* GitHub repository: `alx-backend-python`
* Directory: `0x02-python_async_comprehension`
