"""
Errors in Python
Name Errors

A NameError is reported by the Python interpreter when it detects a variable that is unknown.

This can occur if a variable is used before it has been assigned a value or if a variable name is spelled differently than the point at which it was defined. The Python interpreter will display the line of code where the NameError was detected and indicate which name is found that was not defined.

Here’s an example of a NameError error message:

File "script.py", line 1, in <module>
    print(score)
NameError: name 'score' is not defined

This error is suggesting that the variable score was never defined in the program. Oops.

Some common name errors are:

    Misspelling a variable name.
    Forgetting to define a variable.

Instructions
1.

In script.py, another teammate Alex wrote a Who Wants to Be A Millionaire question and four options. If the answer is an uppercase or lowercase “A”, then the score goes up.

Run the program to check it out.

In case you were wondering, the \n escape sequence simply prints a new line in the terminal.
2.

Oh no, there are two NameError errors!

Can you find them both?

There will be an error message when the program is run:

Traceback (most recent call last):
  File "script.py", line 13, in <module>
    print("C.", option3)
NameError: name 'option3' is not defined

In script.py, on line 13, a variable option3 is not defined.

Can you find the other bug? 🐛

Note: Usually the error is on the exact line indicated by the interpreter, or the line of code just before it; however, if the problem is incorrectly nested braces, the actual error may be at the beginning of the nested block.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!
"""
