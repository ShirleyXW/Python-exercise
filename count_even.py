"""
Define a function called count_evens.

The count_evens function accepts a non-empty list of integers called readings.

The count_evens function must return a tuple that contains two integers.
The first value in the tuple must be the number of even integers in the list called readings.
The second value must be the sum of the even integers in the list called readings.

You may not modify the list passed as an argument in any way, even temporarily, if you do you
will earn zero marks for this question.

You must provide a full docstring for this function including all pre- and post-conditions.
You must create two useful and different doctests for this function.
No main function is required.
"""


def count_evens(readings):
    first_number = len(readings)
    second_number = sum(readings)
    a_tuple = (first_number, second_number)
    return a_tuple


def main():
    some_list = [0, 2, 4, 6, 8, 10]
    count_evens(some_list)
    print(count_evens(some_list))


if __name__ == "__main__":
    main()
