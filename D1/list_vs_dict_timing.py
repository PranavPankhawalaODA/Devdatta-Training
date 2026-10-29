import random
import time

# 1. Setup the data sizes
data_size = 10000000
num_lookups = 1000

# Create a list and a dictionary with the same elements
data_list = list(range(data_size))
data_dict = {x: True for x in data_list}

# Generate random keys to look up (some existing, some missing  - to be fair)
lookup_keys = [random.randint(0, data_size * 2) for _ in range(num_lookups)]

# 2. Benchmark List Lookup Time (O(N) linear search)
start_time = time.perf_counter()
for key in lookup_keys:
    # Using 'in' forces the list to scan sequentially
    _ = key in data_list
list_time = time.perf_counter() - start_time

# 3. Benchmark Dictionary Lookup Time (O(1) constant hash lookup)
start_time = time.perf_counter()
for key in lookup_keys:
    # Dictionary uses a hash table for instant lookup
    _ = key in data_dict
dict_time = time.perf_counter() - start_time

# 4. Display Results
print(f"Total time for {num_lookups} lookups in a list of size {data_size}: {list_time:.6f} seconds")
print(f"Total time for {num_lookups} lookups in a dict of size {data_size}: {dict_time:.6f} seconds")
print(f"Dictionary lookup was {list_time / dict_time:.1f}x faster!")
