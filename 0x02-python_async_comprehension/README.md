# 0x02. Python - Async Comprehension

# Description

This project focuses on Python asynchronous programming, specifically working with asynchronous generators and comprehensions. We explore how to write asynchronous functions, use async comprehensions, and measure the runtime of parallel tasks.

# Learning Objectives

By the end of this project, I should be able to:

- Write an asynchronous generator.
- Use async comprehensions to collect data from an asynchronous generator.
- Type-annotate generators in Python.
- Measure the runtime of multiple asynchronous operations running in parallel.

# Tasks

- **0-async_generator.py**: Defines a coroutine `async_generator()` that asynchronously yields random numbers between 0 and 10.
- **1-async_comprehension.py**: Implements `async_comprehension()` that collects 10 random numbers using an async comprehension over `async_generator()`.
- **2-measure_runtime.py**: Measures the runtime of four parallel instances of `async_comprehension()` using `asyncio.gather`.
