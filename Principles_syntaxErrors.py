"""
Errors in Python
Syntax Errors

When we are writing Python programs, the interpreter is our first line of defense against errors.

SyntaxError means there is something wrong with the way your program is written — punctuation that does not belong, a command where it is not expected, or a missing parenthesis can all trigger a SyntaxError.

Here’s an example of a SyntaxError error message:

File "script.py", line 1
  print(Hello world!)
                  ^
SyntaxError: invalid syntax

The interpreter will tell us where (the file name and line number) it got into trouble and its best guess as to what is wrong.

After reading the error message, we can assume that the cause for this error is a lack of quotation marks around Hello world!.

Some common syntax errors are:

    Misspelling a Python keyword.
    Missing colon :.
    Missing closing parenthesis ), square bracket ], or curly brace }.

Instructions
1.

In script.py, your coworker Carolyn wrote a Fortune Cookie program that is supposed to print out a possible fortune based on a random number and an if/elif/else statement.

Run the program to check it out.

Here’s the pseudocode that they wrote on the whiteboard:


if fortune == 0:
  # prints one fortune
elif fortune == 1:
  # prints another fortune
elif fortune == 2:
  # prints another fortune
elif fortune == 3:
  # prints another fortune
elif fortune == 4:
  # prints another fortune


And random.randint(a, b) basically spits out a random integer N such that a <= N <= b.
2.

Oh no, there are three SyntaxError errors inside script.py!

Can you find them all?

There will be an error message when the program is run:

File "script.py", line 7
  if fortune == 0
                  ^
SyntaxError: invalid syntax

In script.py, on line 7, a colon : is expected at the end of the if condition.

Can you find the other two bugs? 🕵️‍♀️

Note: Usually the error is on the exact line indicated by the interpreter, or the line of code just before it; however, if the problem is incorrectly nested braces, the actual error may be at the beginning of the nested block.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
"""
