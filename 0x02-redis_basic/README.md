# 0x02. Redis basic

## Overview
This project explores fundamental Redis functionalities for caching and tracking in Python. It includes implementations for storing and retrieving data, counting method calls, storing lists, and creating an expiring web cache.

## Files

| File Name   | Description |
|-------------|-------------|
| `exercise.py` | Contains the `Cache` class with methods for storing data, retrieving data with type conversion, counting method calls, and storing call history as lists in Redis |
| `web.py`     | Implements a web caching function `get_page(url)` using Redis. It caches HTML content from URLs with expiration and tracks access counts |
| `x-main.py`    | Test scripts to demonstrate and validate functionalities of `exercise.py` (1-4) and `web.py` (5) |
