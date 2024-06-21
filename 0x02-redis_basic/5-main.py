#!/usr/bin/env python3
""" Main file to test (web.py) caching module """
import redis
import time
get_page = __import__('web').get_page

r = redis.Redis()

url = "http://slowwly.robertomurray.co.uk"

# First request (cache miss)
content = get_page(url)
print(f"First request: {content}")

# Second request (cache hit)
content = get_page(url)
print(f"Second request: {content}")

# Wait for cache to expire (10 seconds)
time.sleep(10)

# Third request (cache miss)
content = get_page(url)
print(f"Third request: {content}")

# Check how many time the URL was accessed
print(r.get(f"count:{url}"))
