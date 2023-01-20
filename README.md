# Bracket Balance Challenge

----
This repository contains Python scripts that solve the bracket balance challenge. The challenge involves determining if 
a given string of brackets is balanced, and if not, adding the necessary brackets to make it balanced.

## Scripts

1. **stack-class.py** - This script contains an implementation of a stack data structure using a Python class.
A stack is a Last In First Out (LIFO) data structure. This implementation includes the following methods:
* **'\__init\__(self)'** : Initializes an empty stack.
* **'is_empty(self)'** : Returns True if the stack is empty, False otherwise.
* **'size(self)'** : Returns the number of elements in the stack.
* **'push(self, item)'** : Pushes an item onto the top of the stack.
* **'pop(self)'** : Removes and returns the item at the top of the stack. If the stack is empty, returns None 
* **'peek(self)'** : Returns the item at the top of the stack. If the stack is empty, returns None.

This script can be useful as a building block for other data structures or algorithms that use a stack.

2. **deque.py** - This script shows how to use the deque data structure from the collections module as a stack. 
The deque class provides a thread-safe double-ended queue, which can be used as a stack with the following methods:
* **append(item)** : Pushes an item onto the top of the stack.
* **pop()** : Removes and returns the item at the top of the stack. If the stack is empty, raises an IndexError.

This script shows that you can use deque as a stack by using the append method to push an item onto the top of the 
stack and the pop method to remove and return the item at the top of the stack. The stack[-1] will give the top 
element without removing it.

3. **is_balanced.py** - This script contains a function called is_balanced() which takes in a string as an argument and 
returns a boolean value indicating whether the string is bracket balanced or not. The function uses a stack to check if 
the given string is balanced. It iterates through each character in the string and performs the following checks:
* If the character is an opening bracket, it pushes it onto the stack.
* If the character is a closing bracket, it checks if the stack is empty. If it is, it returns False as there is no 
matching opening bracket.
* If the stack is not empty, it compares the last element of the stack with the current closing bracket. If they are 
not matching, it returns False.
* If the brackets match, it removes the last element from the stack.

At the end, if the stack is empty, it returns True, indicating that the string is balanced. If the stack is not empty, 
it returns False.

This script can be useful to check if a given string is bracket balanced. It can be used as a part of a larger program 
to validate user input or to check the syntax of a programming language.

4. **insert_missing_bracket.py** - This script contains a function called insert_missing_bracket() which takes in a 
string as an argument and returns the same string with any missing brackets inserted in the appropriate places.
The function uses a stack to iterate through each character in the string and insert any missing brackets. It performs 
the following checks:
* If the character is an opening bracket, it pushes it onto the stack and adds it to the result string.
* If the character is a closing bracket, it checks if the stack is empty. If it is, it adds the bracket to the result 
string without an opening bracket.
* If the stack is not empty, it compares the last element of the stack with the current closing bracket. If they 
match, it removes the last element from the stack and adds the bracket to the result string. If they do not match, 
it adds the corresponding opening bracket to the result string and removes the last element from the stack.
* If the character is not a bracket, it adds it to the result string without any change.

At the end, it adds any remaining opening brackets in the stack to the result string with the corresponding 
closing bracket.

This script can be useful to insert the missing brackets to make a given string bracket balanced. It can be used as 
a part of a larger program to validate user input or to check the syntax of a programming language.

5. '**insert_missing_bracket_v2.py**' : This script contains a function called '**insert_missing_brackets()**' which 
takes in a string as an argument and returns the same string with any missing brackets inserted in the appropriate places.
This function uses dictionaries to map opening and closing brackets, and performs the same checks as the previous script. 
The main difference is that it uses dictionaries to check for matching brackets, rather than using a series of if-else 
statements. This can make the code more readable and easier to maintain.

This script can be useful to insert the missing brackets to make a given string bracket balanced. It can be used as a 
part of a larger program to validate user input or to check the syntax of a programming language. It is an alternative 
solution to the previous version, which uses if-else statements.

## Usage

To use the scripts, you will need to have Python 3 installed on your machine. Once you have cloned this repository, 
you can navigate to the root directory of the repository in your command line and run the scripts by calling '**python 
script_name.py**'. For example, to run the '**is_balanced.py**' script and check if the string '**"(())"**' is bracket 
balanced, you would run the following command:

    python is_balanced.py "(())"

This would return '**True**' indicating that the string is balanced.

Similarly, to use the '**insert_missing_brackets()**' function and get a bracket balanced version of the string 
**"(()"**, you would run the following command:

    python insert_missing_brackets.py "(()"

This would return **"(())"** which is a balanced version of the original string.

## Note

In summary, this repository contains a set of Python scripts that help in solving the bracket balance challenge. 
The scripts include:

1. An implementation of a stack data structure using a Python class
2. An example of using a deque as a stack
3. A function to check if a given string is bracket balanced
4. A function to insert missing brackets to make a string bracket balanced using if-else statements
5. A function to insert missing brackets to make a string bracket balanced using dictionaries for mapping the 
opening and closing brackets.

These scripts are provided as a starting point and may need to be modified or extended for specific use cases. 
Feel free to use and modify the scripts as needed for your own projects.
