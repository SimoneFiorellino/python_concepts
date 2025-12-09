"""
Assigning local_var = GLOBAL_VAR creates a faster local alias to the same object without copying it. 
Local lookups are quicker and make the function’s dependency explicit while still referring to the original global value.
"""

import time
import math

class Timer:
    def __init__(self, label=""):
        self.label = label

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        end = time.perf_counter()
        print(f"{self.label}: {end - self.start:.6f} seconds")


# ----- "Big" global data -----
N = 100000
GLOBAL_LIST = [i * 0.001 for i in range(N)]


def compute_with_global():
    total = 0.0
    for _ in range(250):          # outer loop to amplify cost
        for x in GLOBAL_LIST:     # global lookup in inner loop
            total += math.sin(x) * math.cos(x)
    return total


def compute_with_local_alias():
    local_list = GLOBAL_LIST            # alias, no copy
    total = 0.0
    for _ in range(250):
        for x in local_list:            # local lookup in inner loop
            total += math.sin(x) * math.cos(x)
    return total


def compute_with_local_copy():
    local_list = GLOBAL_LIST.copy()     # real copy (extra cost)
    total = 0.0
    for _ in range(250):
        for x in local_list:
            total += math.sin(x) * math.cos(x)
    return total


# Warm-up to avoid first-run weirdness
compute_with_global()
compute_with_local_alias()
compute_with_local_copy()

with Timer("Global in loop"):
    compute_with_global()

with Timer("Local alias in loop"):
    compute_with_local_alias()

with Timer("Local COPY in loop"):
    compute_with_local_copy()
