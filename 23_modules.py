# built‑in modules (no installation needed)

import math

a = math.floor(4.95)

b = math.factorial(9)

c = math.ceil(9.99)

d = math.pi

e = math.sqrt(9)

f = math.sin(45)

g = math.cos(45)

h = math.tan(45)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

# --- random ---
import random
print("Random int 1_10:", random.randint(1, 10))
print("Random choice:", random.choice(["red", "blue", "green"]))
print("Random float:", random.random())

# --- datetime ---
import datetime
print("Now:", datetime.datetime.now())
print("Today:", datetime.date.today())

# --- os ---
import os
print("Current directory:", os.getcwd())
print("List files:", os.listdir())
print("Environment PATH exists:", "PATH" in os.environ)

# --- sys ---
import sys
print("Python version:", sys.version)
print("Executable:", sys.executable)
print("Arguments:", sys.argv)

# --- statistics ---
import statistics
nums = [10, 20, 30, 40]
print("Mean:", statistics.mean(nums))
print("Median:", statistics.median(nums))

# --- json ---
import json
data = {"name": "Alex", "age": 20}
json_str = json.dumps(data)
print("JSON string:", json_str)
print("Back to dict:", json.loads(json_str))
print("Keys:", list(json.loads(json_str).keys()))

# --- requests ---
import requests
response = requests.get("https://api.github.com")
print(response.status_code)