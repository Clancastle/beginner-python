"""
//Data Types
text types - str() (string)
number types - integer, float, complex; int() float() complex()
sequence types - list, tuple, range; list()/['a', 'b'], tuple()/('a', 'b'), range(int)
mapping types - dict; dict()/ {a: 1, b: 2}
set types - set, frozenset; set('a', 'b'), frozenset('a', 'b')
boolean types - bool() - #only types are - True, False, None
binary types - bytes, bytearray, memoryview; bytes(), bytearray(), memoryview(bytes())
to confirm type - print(type(value))
int - positive or negative number without decimals
float - positive or negative number with decimals can be with e to indicate ** 10
complex are written as float or int, plus j, as the imaginary part

"""

"""
//Strings
//Strings are unchangeable, but you can declare a variable = string + method, or many methods at once
brackets can be used to access characters in string.
We can also loop through a string. - for loop # len() for length
We can use print('word' in string)
Or an if statement. if 'word' in string:
We can use not, as in, if not in...
We can also slice it, as in string[::] or # [1:2] [:7] [3:] [::-1][::]
This is object oriented programming so we have many methods we can use on strings.
Strings are immutable so you can't change them, but you can assign it to a new variable
before the '.' you put the variable containing the string
string.upper() > turns all letters uppercase
string.lower() > turns all letters lowercase
string.strip() > clears any excess spaces 
string.lstrip() > returns left trim of string
string.rstrip() > returns right trim of string
string.replace(value, value) > replaces value with value ex. b, with a 
string.split(value) > splits a string into a list; default is space
You can do something like  string c = string a + ' ' + string b; ' ' for a space between them
We can add variables and strings with string.format(variable)
Or, something like this var = f" This is a string {variable} {variable2}, or just print it out
To get rid of not being able to do "Yes  "you" are", do this "yes "\you\" are"
\ > escape character 
\\ > backslash
\n > new line 
\r > carriage return
\t > tab
\b > backspace
\f > from feed
\ooo > octal value
\xhh > hex value

string.capitalize() > capitalizes first letter of each word
string.casefold() > converts string to lower case(aggressive)
string.count() > returns the number of times a specific value appears in the string 
string.center() > returns a centered string
string.encode() > returns a encoded version of the string
string.endswith() > returns true if ends with specified value
string.expandtabs() > sets the tab size of string
string.find() > searches for the specified value and returns the index
string.format()  > formats values in a string
string.format_map() > formats values in a string
string.index() > searches for the specified value and returns the index
\ ALL THE IS--- RETURN True IF YES...
.isalnum() > if string is alphanumeric
.isalpha() > if string is in alphabet
.isdecimal() > if string is a decimal
.isdigit() > if string is digits
.isidentifier() > if string is identifier
.islower() > if string is lower case
.isupper() > if string is uppercase
.isnumeric() > if string is numeric
.isprintable() > if string is printable
.isspace() > if string is space only(whitespaces)
.istitle() > if string follows rule of title
.join() > adds values to string
.ljust() > returns left justified version
.maketrans() > returns a table to translate
.partition() > returns 3 tuples from string
.rfind() > searches for value and returns last position of where it was found
.rindex() > searches for value and returns last position of where it was found
.rjust() > returns a right justified version of string
.rpartition() > returns 3 tuples from string
.rsplit() > splits string into list, default is space
.splitlines() > splits the string at line breaks and returns a list
.startswith() > if string starts with value (return true)
.swapcase() > swaps lowercase with upper and vice versa
.title() > converts first letter of each word to upper case
.translate() > returns a translated string
.zfill() > fills the string with a specified number of 0 values at the beginning.
// Boolean values 
True, False, None
if you do print(bool(value)), most of the times it will return True
except anything empty list (),[],{},'',0,None,False = will return False
// Operators
+, -, /, * -- are common, you should know what these do
% > this divide and returns remainder (modulus) e.x. 7 % 2 = 1
** > this is exponentiation (x ** y) x to the power of y
// > floor division (returns without remainder or decimal) 7 // 2 = 2

= > is assignment (assign a variable)
+= > is the same as x = x + value
-= > is the same as x = x - value
/= > is the same as x = x / value
*= > is the same as x = x * value
%= > is the same as x = x % value
//= > is the same as x = x // value
**= > is the same as x = x ** value
|= > is the same as x = x | value
^= > is the same as x = x ^ value
>>= > is the same as x = x >> value
<<= > is the same as x = x << value

== > is equal to 
<= > is less than or equal to
>= > is greater than or equal to
< - is less than
> - is greater than
!= > is not equal to

and > put after statement to add another statement
or > put after statement if you only want one of the statements to be true and the code will run
not > put after expression to show that if a statement is not true, run the code

is > used if variables have the same values e.x. x is y
is not > used to make sure variables do not have the same values

//Following are used in more intermediate and advanced than beginner.
//These are used to compare binary numbers (bits)
& (AND) > is used to set each bit to 1 if both bits are 1
| (OR) > is used to set each bit to 1 if one of two bits is 1
^ (XOR) > is used to set each each bit to 1 if only one of two bits is 1
~ (NOT) > is used to invert all bits
<< (Zero fill left shine) > is used to shift left by pushing zeros from the right and let the leftmost bits fall off
>> (Signed right shift) > is used to shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

//Operator precedence 
//If operators have the same level of precedence, precedence is determined by order
() > Parentheses 
** > Exponentiation
+x, -x, ~x > Unary plus, Unary minus, Bitwise NOT
*, /, //, % > Multiplication, Division (Floored), Modulus
+, - > Addition, Subtraction
<<, >> - Bitwise - left, right shift
& > Bitwise AND
^ > Bitwise XOR
| > Bitwise OR
==, !=, >, <, =>, =<, is, is not, in, not in > (you can see I dont have to explain)
not > logical NOT
and > logical AND
or > logical OR

//Lists 
//Lists are ordered, changeable, and allow duplicate values
list = ['item1', 'item2', 'item3']
to access items in a list, you would do list[0], to access the first value
the second item in the list is index value 1 and so on
We can change the list by calling a list method and executing it
Unlike for strings, we do not have to make another variable to put the changed list in
We can use list.len() to determine its length
A list can contain different data types > [True, 6.86, 'Yes I love him']
To determine what something identifies as, use type(value)
We can also declare a list like this x = list(())
You cna also have a variable a specific part of a list; list2 = list[2:]
Or you can change the values of a list like list[6:8] = ['item', 'items']
You can use list.insert(index, value) to add to a list without replacing at the specific index
list.append() adds the item to the end of the list
list.extend(list2) makes a copy of list2 and adds it to list
list.remove(item) removes the specified item in the list
list.pop(index) removes the specified index of the list if not specified, it removes the last item 
You can also use del list[index] if you dont want to use .remove()
To delete the entire list, use del list or list.clear()
You can also loop though a list using for loops to print each item
You cant loop through a lost straight up, but you can use range(len(list)) to iterate through the list
You can also loop through the list with a while loop, and set a break condition later
while i < len(list):
    print(i)
    i += i
you can also loop through a list with comprehensions
listx = [print(x) for x in list]
List comprehensions are one line if statements.
It does what a for loop is supposed to do, but does it with less lines of code and makes it much easier to understand your code
list = []
listx = [x for x in list if 'x' in x] #and then you print the list comprehension
the syntax would look like 
listx = [expression for item in iterable if condition == True]
you can loop through a list like so; [x for x in list] print(x)
you can do many things, like use range() to loop over, or even make it so every item in list will turn uppercase
something like this; [x if x != 'b' else 'o' for x in list]
There are many methods available for lists like .sort()
which can sort a list alphabetically, or smallest to largest number
You can reverse the list by putting in a parameter reverse=True or do list[::-1] to return list backwards. list[::2] will return every 2nd item in list
You can also experiment on your own to see what works and what doesn't
You can also create a function, and set something like de f(x) return x -7 and put in a parameter list.sort(key=f)
The sort method is case sensitive keep in mind this > list.sort(key=str.lower)
.reverse() > reverses the list as of now
Copying a list is not as simple as list = list1 because the variables will call to the same list
To avoid changing the original list when all we want is a copy, we use .copy() and .deepcopy()
or just use list1 = list(listx)
In order to join or concatenate we use + or .append() or .extend(), use append with a loop, list.append(i)
List = list + list1
Here are all of the list methods.
Keep in mind that there are many other built in methods that are available for all array type to use
.append() > Adds an element at the end of the list
.clear() > Removes all the elements from the list
.copy() > Returns a copy of the list
.count() > Returns the number of elements with the specified value
.extend() > Add the elements of a list (or any iterable), to the end of the current list
.index() > Returns the index of the first element with the specified value
.insert() > Adds an element at the specified position
.pop() > Removes the element at the specified position
.remove() > Removes the item with the specified value
.reverse() > Reverses the order of the list
.sort()	> Sorts the list

//Tuple
//Tuples is an array which are ordered and unchangeable nad allows duplicate items



//Set
//Set is an array which is unordered, unchangeable -> (frozenset), and unindexed

//Dictionary
//Is an collection which is ordered and changeable with no duplicate members 

"""
