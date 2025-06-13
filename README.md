# BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

## Description

BookBot is a Python program that analyzes novels and prints a comprehensive statistical report of word and character usage found within the text. This tool helps you understand the composition of literary works by providing detailed metrics about the content.

## Features

- **Statistical Report**: Generates a formatted report showing:
  - Total word count
  - Character frequency sorted by occurrence (most frequent first)
  - Clean output focusing only on alphabetic characters

## Usage

Run the program from the command line by providing the path to a text file:

```bash
python3 main.py <path_to_book>
```

### Example

```bash
python3 main.py frankenstein.txt
```

## Sample Output

```
============ BOOKBOT ============
Analyzing book found at frankenstein.txt...
----------- Word Count ----------
Found 77986 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
...
============= END ===============
```

## Project Structure

- `main.py` - Main program entry point and report generation
- `stats.py` - Statistical analysis functions for word and character counting
