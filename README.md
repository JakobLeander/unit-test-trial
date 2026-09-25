# Unit Test Practice

This project contains small Python helper functions for practicing unit testing. The unit tests are intentionally left for you to write.

## Setup

Create the virtual environment if it does not already exist:

```bash
python3 -m venv .venv
```

Activate it on Linux or macOS:

```bash
source .venv/bin/activate
```

Install the development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

## Usage

Import `PracticeHelpers` from `helpers.py`:

```python
from helpers import PracticeHelpers

helpers = PracticeHelpers()
print(helpers.add_numbers(2, 3))
```

## Available Helpers

- `add_numbers`: Adds two numbers.
- `is_even`: Checks whether an integer is even.
- `reverse_text`: Reverses a string.
- `count_vowels`: Counts vowels in a string.
- `factorial`: Calculates a factorial and rejects negative values.
- `find_maximum`: Finds the largest number and rejects empty lists.
- `remove_duplicates`: Removes duplicate strings while preserving order.
- `celsius_to_fahrenheit`: Converts Celsius to Fahrenheit.
- `is_palindrome`: Checks whether text reads the same forwards and backwards.
- `word_frequency`: Counts case-insensitive words in a string.
- `is_prime`: Checks whether an integer is prime.
- `calculate_average`: Calculates the average of a non-empty list of numbers.
- `clamp`: Restricts a value to a minimum and maximum range.
- `fibonacci`: Generates a Fibonacci sequence with a requested number of values.
- `is_anagram`: Checks whether two strings contain the same normalized characters.
- `count_words`: Counts whitespace-separated words in a string.
- `calculate_percentage`: Calculates what percentage one value is of another.
- `rotate_list`: Rotates list values by a requested number of positions.

Try testing normal inputs, boundary values, empty inputs, invalid inputs, and mixed or unexpected values.

Run the test suite with:

```bash
python -m pytest
```