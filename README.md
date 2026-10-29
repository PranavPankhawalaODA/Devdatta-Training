# Solutions to exercises conducted by Devdatta

A collection of standalone Python exercises and demonstrations, organized by
training day. The examples cover basic algorithms, HackerRank and LeetCode
challenges, and common data structures and data-processing patterns.

## Requirements

- Python 3.10 or later
- No third-party packages are required

## Exercises

### D1

| File | Description |
|---|---|
| `D1/anagram_check.py` | Checks whether two strings are anagrams, ignoring case and whitespace. |
| `D1/list_vs_dict_timing.py` | Compares list and dictionary membership lookup times. Uses a 10-million-item dataset, so it can take substantial time and memory to run. |
| `D1/merge_sorted_lists.py` | Reads two ascending lists of numbers and merges them in sorted order. |
| `D1/most_frequent_element.py` | Finds the most frequent whitespace-separated item entered by the user. |

### D2

| File | Description |
|---|---|
| `D2/Hackerrank/groupby_code.py` | Uses `itertools.groupby` to print consecutive digit runs and their lengths. |
| `D2/Hackerrank/itertools_code.py` | Prints combinations of the input characters, in sorted order, for each size from 1 through the requested size. |
| `D2/Hackerrank/itertools_probability.py` | Incomplete exercise scaffold; currently reads input but does not calculate or print a result. |
| `D2/Hackerrank/nested_list.py` | Prints the names of students with the second-lowest score, sorted alphabetically. |
| `D2/leetcode/sqrt.py` | Approximates a square root using Newton's method. |

### D3

| File | Description |
|---|---|
| `D3/lru_cache_demo.py` | Implements an O(1) least-recently-used cache and demonstrates its eviction behavior. |
| `D3/per_user_rate_limiter.py` | Implements a thread-safe per-user request limiter over a rolling time window. |
| `D3/reconcile_id_lists.py` | Separates IDs into shared and list-specific groups while preserving first-occurrence order. |
| `D3/top_5_users_per_day.py` | Counts events per user and day, returning the most active users for each day. |

## Running an exercise

Run a script from the project root with Python. For example:

```powershell
python D1\anagram_check.py
python D3\lru_cache_demo.py
```

Most scripts are interactive or print a small demonstration to the terminal.
The HackerRank exercises generally expect input in the format specified by
their challenge.
