# Async Python Project

This project demonstrates the basics of asynchronous programming in Python using the `asyncio` module. It covers the following key concepts:

- `async` and `await` syntax
- Executing an async program with `asyncio`
- Running concurrent coroutines
- Creating `asyncio` tasks
- Using the `random` module

## Project Structure

The project consists of the following tasks:

1. **The basics of async**: Write an asynchronous coroutine `wait_random`.
2. **Execute multiple coroutines at the same time with async**: Write an async routine `wait_n`.
3. **Measure the runtime**: Create a `measure_time` function to measure the execution time of `wait_n`.
4. **Tasks**: Write a function `task_wait_random` that returns an `asyncio.Task`.
5. **Tasks with wait_n**: Modify `wait_n` into `task_wait_n` using `task_wait_random`.

## Requirements

- **General**
  - A `README.md` file, at the root of the folder of the project, is mandatory.
  - Allowed editors: vi, vim, emacs.
  - All files are interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
  - All files should end with a new line.
  - All files must be executable.
  - The length of files will be tested using `wc`.
  - The first line of all files should be exactly `#!/usr/bin/env python3`.
  - Code should use the `pycodestyle` style (version 2.5.x).
  - All functions and coroutines must be type-annotated.
  - All modules should have documentation.
  - All functions should have documentation.

## Files

### 0-basic_async_syntax.py

Defines the `wait_random` coroutine which waits for a random delay between 0 and `max_delay` (default 10) seconds and returns it.

### 1-concurrent_coroutines.py

Defines the `wait_n` coroutine which spawns `wait_random` n times with the specified `max_delay` and returns a list of all the delays in ascending order.

### 2-measure_runtime.py

Defines the `measure_time` function that measures the total execution time for `wait_n(n, max_delay)` and returns `total_time / n`.

### 3-tasks.py

Defines the `task_wait_random` function that returns an `asyncio.Task` for the `wait_random` coroutine.

### 4-tasks.py

Defines the `task_wait_n` coroutine which spawns `task_wait_random` n times with the specified `max_delay` and returns a list of all the delays in ascending order.

## Usage

### Running the Examples

To run the examples, you can use the provided main files:

```sh
./0-main.py
./1-main.py
./2-main.py
./3-main.py
./4-main.py
