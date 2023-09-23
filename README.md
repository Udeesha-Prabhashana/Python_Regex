# Regex Pattern Matcher

This program is designed to match regular expressions (regexes) with specific features: patterns that start with `^`, patterns that end with `$`, and patterns that include `.` to match one character. The program takes a pattern and a text as inputs via the terminal and provides the output on the terminal.

## Features

- `^` - Matches patterns that start with the given pattern.
- `$` - Matches patterns that end with the given pattern.
- `.` - Matches exactly one character.

## How to Use

1. Run the program using a Python interpreter.
2. Enter the pattern when prompted.
3. Enter the text when prompted.
4. The program will provide output indicating whether the pattern matches the text and at which index.

## Functions

### `string_matching(pat, txt)`

This function implements the naive string matching algorithm. It matches the given pattern `pat` with the text `txt` and returns the starting index of the first occurrence of the pattern in the text. If no match is found, it returns `-1`.

### `che_starts(pat, txt)`

This function checks whether the text starts with the given pattern. It returns the starting index (0-based) if the text starts with the pattern; otherwise, it returns `-1`.

### `che_ends(pat, txt)`

This function checks whether the text ends with the given pattern. It returns the starting index (0-based) of the matching pattern if found at the end of the text; otherwise, it returns `-1`.

### `che_matching(pat, txt)`

This function checks patterns that include the special character `.`. It matches the given pattern `pat` with the text `txt` and returns a list of starting indices of all occurrences of the pattern in the text. If no match is found, it returns `-1`.

### `preprocessor(pat, txt)`

This function preprocesses the given regex pattern and text. It checks for the presence of special characters (`^`, `$`, `.`) in the pattern and calls the corresponding functions to perform the matching. It then prints the result indicating whether a match was found and, if applicable, the indices of the matches.

### `main()`

This function takes user input for the pattern and text, and then calls the `preprocess` function to perform the matching and display the result.

## Examples
Here are some example patterns and texts you can try:

1. Pattern: abc, Text: frabcdefg
   Output: Pattern found at index 2

2. Pattern: ^abc, Text: abcdefg
   Output: Pattern found at index 0

3. Pattern: def$, Text: abcdef
   Output: Pattern found at index 3

4. Pattern: a.c, Text: wabcdecd
   Output: Pattern found at index 1


## Why Use Naive String Matching Algorithm?

The naive string matching algorithm is used for this pattern matching because it provides a straightforward and easy-to-understand approach. It systematically compares each character of the pattern with each character of the text to identify matches. While more advanced algorithms like KMP or regex engines provide better performance for larger texts and patterns, the naive algorithm suffices for small-scale applications and serves as a good starting point for understanding string matching concepts.
