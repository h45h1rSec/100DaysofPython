# Python Docstrings are the string literals that appear RIGHT AFTER the definition of a function, method, class, or module. (Docstrings are not limited to functions)

def NumberSquared(Number):
    '''Takes in a number and returns the square of it''' #Not a comment!
    print(Number**2)

NumberSquared(5)

print(NumberSquared.__doc__) #Prints the docstring!


##########################################
# Python Enhancment Proposal (PEP)

# PEP8 provides a guideline and best practice for python code, written in 2001 by Guido Van Rossum, Barry Warsaw and Nick Coghlan.
# It's focus was to make the program consistent, readable and maintainable.


# PEP 8 is a style guide for Python code, outlining conventions for writing readable and maintainable code. It was authored by Guido van Rossum, Barry Warsaw, and Nick Coghlan and was first released in 2001. The primary goal of PEP 8 is to enhance the readability of Python code and make it consistent across the wide range of projects.

# Here are some key points covered by PEP 8:

# Indentation: Use 4 spaces per indentation level. It's important to be consistent with spaces to maintain readability.

# Whitespace in Expressions and Statements: Avoid extraneous whitespace in the following situations:

# Immediately inside parentheses, brackets, or braces.
# Between a trailing comma and a following close parenthesis.
# Imports: Imports should usually be on separate lines and should be grouped in the following order:

# Standard library imports.
# Related third-party imports.
# Local application/library specific imports.
# Whitespace in Expressions and Statements: Avoid extraneous whitespace in the following situations:

# Immediately inside parentheses, brackets, or braces.
# Between a trailing comma and a following close parenthesis.
# Comments: Comments should be complete sentences, and a space should be added after the hash mark. Inline comments should be avoided.

# Naming Conventions: Follow consistent naming conventions:

# Modules should have short, lowercase names.
# Class names should be in CamelCase.
# Function and variable names should be in lowercase, with words separated by underscores.
# Function and Method Arguments: Don't use mutable types (like lists or dictionaries) as default values for function or method arguments.

# Limiting Line Length: Limit all lines to a maximum of 79 characters for code and 72 for docstrings.

# Whitespace Between Functions and Classes: Use two blank lines between functions or classes.




import this #Guide poem for python...