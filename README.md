# Tech Challenge

Program that computes some basic statistics on a collection of small positive integers. All values will be less than 1,000.

## Getting Started

These instructions will explain the details on how to set up and run the application.

### Prerequisites

* [Python 3](https://www.python.org/downloads/)

### Usage

Import DataCapture class in your script.

`from stats.stats import DataCapture`

This class contains the following methods:

`add(n)` Store element

`build_stats()` Process the values and returns an object with the methods:

	`less(n)` Returns how many numbers are less than the given value

	`between(start, end)` Returns how many numbers are in the given range

	`greater(n)` Returns how many numbers are greater than the given value

### Example

The following snippet shows an example of how can you call the functions.

```
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
stats.less(4) # Returns 2 (only two values 3, 3 are less than 4) 
stats.between(3, 6) # Returns 4 (3, 3, 4 and 6 are between 3 and 6)
stats.greater(4) # Returns 2 (6 and 9 are the only two values greater than 4)
```

### Run tests

`python -m unittest test_stats.py`

## Author

**Roberto Carrillo** - [rcovar00](https://github.com/rcovar00)
