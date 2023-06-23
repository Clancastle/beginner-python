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
\ xhh > hex value

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
tuple = (0, 2, 7)
Tuples can contain any data type: int, str, bool
Or can contain a combination of data types:
print(type(tuple))
You are also able to use tuple(('item', 1)) to make a tuple
A tuple is unchangeable, but you can print or loop over it > tuple[0]
As a recap, to access the index of a tuple/list or any array,
0 for the first item, 1 for the second, and so on. to access the last, make the index -1 or -2 for the second last
Something like [-4:-1] returns the fourth last to first last, but excludes first last
You can also do things that you can do with lists, like comprehension, or looping
If statements are possible as well.
Once a tuple is created, you cannot change its values
BUT -- you can convert the tuple to a list, and then change the list, then convert back to a tuple
list = list(tuple) # as it seems, there is another way to use the list() method
list[0] = item
tuple = tuple(list)
Another way you could go about doing this would be adding another tuple to the tuple
That would also be a way of updating the tuple. 
A one item tuple would look like tuple = ('item',) #you have to add a comma
tuple += ('item',)
To remove an item in a tuple, use the same workaround we used to add change a tuple
Or to just delete a tuple use 
del tuple > completely deletes the tuple
When we  assign values to a tuple, we call it packing.
To unpack, we would assign variables.
tuple = (1, 2, 3)
(var1, var2, var3) = tuple 
And that would multi assign the values in the list to the variables
NOTE: That the variables must match the number of values in the tuple,
if not, you must use an asterisk to collect the remaining values as a list
(var1, *var2) = tuple
if the asterisk is placed before the last variable (var2), var2 will contain the remaining values as a list
Else, if the asterisk is somewhere else, python will assign values until the values match the variables left
To loop through a tuple, use for loop, or list comprehension, (that you know of so far)
for i in tuple: print(i) > this prints out each value in the tuple
for i in range(len(tuple)): print(i) > this prints out the indexes of the tuple, including 0
i = 0; while i < len(tuple):; print (i); i += 1

Another thing you can do is tuple1 = tuple * 2 
this duplicates your tuple and makes it a new tuple
You can use these tuple methods 
tuple.count(value)
tuple.index(value)
Keep in mind that there are many more methods in general
and more methods only available to understand for the advanced class

//Set
//Set is an array which is unordered, unchangeable, and unindexed
set = {'item', item1', 'item2'}
sets are unordered, so you cannot be sure in which order they will appear
sets do not allow items with the same value e.x. True, 1 (They are considered the same values)
A set can also contain different data types as you can see from above
You can use these as well - type() len() set() etc
As well as use loops to print out the set. 
Something I think I hadn't mentioned before, is that you can use the in keyword to check if something is in the set
Go back to the section on operators and think to yourself about what you can do
You cannot change a set after its creation, but you can add values. (frozenset)
set.add(value)
set.update(set1) > adds set1 to set, with random order
set.update(list) > you can even add a dictionary or tuple to add to a set, etc
To remove use set.remove(value) > if not found, will raise error
To remove without error if not found, use set.discard()
Also for some fun, why not use set.pop() ? It will remove a random item
to clear or delete the set, use set.clear() / del set

Sets are very interesting, and have some unusual methods:
sets = set.union(set1) > this returns a set with items from both sets: remember, no duplicates
set.update(set1) > inserts all items from set1 into set
set.intersection_update(set1) > keeps only the duplicates found in both sets, in set
set3 = set.intersection(set1) > returns a new set where only the duplicates in both sets are
set3.symmetric_difference_update(set1) > returns set3, and will keep only the elements that are not in both sets
set3 = set2.symmetric_difference(set1) > returns a new set that does the same thing as its counterpart with _update
------- Here is a full list of set methods --------
set.add() > adds value to set
set.clear() > clears set, does not delete it
set.copy() > copies a set
set.difference() > returns a set that contain the items that exist ONLY in the first set
set.difference_update() > removes the items in set that are also in another set
set.discard() > removes item without error
set.intersection() > returns a new set where only the items seen in all sets are kept
set.intersection_update() > updates set by removing all items not found in another set
set.isdisjoint() > returns whether 2 sets have an intersection or not
set.issubset() > returns whether another set contains this set
set.issuperset() > returns whether this set contains another set
set.pop() > removes random value
set.remove() > removes specified value, gives error if not found
set.symmetric_difference() > returns a set with only non duplicates, not found in both sets
set.symmetric_difference_update() > Remove the items that are present in both sets, AND insert the items that is not present in both sets: 
set.union() > returns 2 unified sets
set.update() > update set by adding another set
frozenset() > like calling set, only this frozenset is more like a tuple


//Dictionary
//Is an collection which is ordered and changeable with no duplicate members 
dict = {
    "name": "mosh",
    "brand": "volvo",
    "year": 2001
}
A dictionary values are called keys, and values. key:value pairs
To print a value, refer to the key first. 
print(dict["name"])
The newest 3.7 version of python is ordered dictionary, but if you are working on a older version
your dictionary might be unordered. to fix this, from tkinter import Ordereddict 
or search up on google if that doesnt work out. 
If you have a duplicate in a list, the duplicate key:value pair will overwrite the original one
It is also possible to use dict() to make a dictionary








"""
