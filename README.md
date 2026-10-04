# Root Power Finder

A simple Python program that searches for a combination of a **root** and **power** whose result matches an integer entered by the user.

For example, if the user enters `81`, the program can identify:

```text
3 ** 4 = 81
```

The project was created as a beginner Python exercise to practice loops, conditional statements, user input, and exponentiation.

## How It Works

The program asks the user to enter an integer and then searches through possible root and power values.

The basic calculation is:

```python
root ** power
```

If the result matches the user's input, the program displays the matching root and power.

For example:

```text
Please enter an integer: 81

The root 3 raised to the power 4 equals the input 81.
```

## Features

* Accepts an integer from the user
* Searches through possible root values
* Tests multiple power values
* Reports the first matching root/power combination
* Displays a message when no matching combination is found

## Requirements

You only need:

* Python 3.x

No external libraries or packages are required.

## Running the Program

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/root-power-finder.git
```

Navigate into the project directory:

```bash
cd root-power-finder
```

Run the Python script:

```bash
python root_power_finder.py
```

## Example

Input:

```text
Please enter an integer: 625
```

Possible output:

```text
The root 5 raised to the power 4 equals the input 625.
```

## What I Learned

This project helped me practice several fundamental Python concepts:

* `input()` for receiving user input
* `int()` for converting input into an integer
* `for` loops
* `while` loops
* `if` statements
* Boolean variables
* Exponentiation using `**`
* Breaking out of nested loops
* Basic algorithmic searching

## Limitations

The current implementation searches only within predefined root and power ranges. Therefore, some valid root/power combinations may not be found if they fall outside those ranges.

The program also returns the **first matching combination** rather than listing every possible combination.

## Future Improvements

Some possible improvements include:

* Search a larger range of roots and powers
* Find and display all valid combinations
* Handle negative integers
* Handle invalid user input more gracefully
* Allow the user to choose the maximum root and power values
* Improve the search algorithm for large numbers

## License

This project is available under the MIT License.
