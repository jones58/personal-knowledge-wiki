To run javascript in vs code  (using code runner extension) - just do ``cmd-shift-p`` and type run code and it will come up in output 

8 types of variable in Javascript:
- `undefined`
- `null`
- `boolean`
- `string`
- `symbol`
- `bigint`
- `number`
- `object`

In JavaScript all variables and function names are case sensitive.
```let variable='some string'```
```let```can be reassigned
```const``` is a constant that can't be reassigned or changed - it's read only

or can just write ``var x = "";`` where x is variable name - but this can be easily overridden so best not to use in big codebase. When you override with let it tells you. 

``++`` operator - using this operator, we write ``x++;`` which is equivalent to ``x=x+1;``
likewise ``--`` operator:  ``x--;`` is same as ``x=x-1;``
``+=`` operator - ``x+=5;`` is same as ``x=x+5``
similarly, -=operator ``x-=5;`` is same as ``x=x-5``
also, ``*=`` operator ``x*=5;`` is same as ``x=x*5``
similarly ``/=`` operator ``x/=5`` is same as ``x=x/5``

These work like this because everything to right of equals sign is evaluated first. 
remainder operator - `%` eg. ``5 % 2= 1;``

when you need a quote or double quote within a string ``
``"this is a string"`` you use \ backslash to escape the quote. So, ``"this is a string \"with a quote\""`` - it is always ``\"`` whether at start or end of quote 

Single and double quotes work same in javascript, but you've got to have it start and end with same one. Sometimes you mix so you can have quoted text in the string. Can also do this when using ``<a>`` tags nested in strings. 

There are other forms of the escape character too - 
`\'` - single quote
`\"` - double quote
`\\` - backslash
`\n` - newline
`\t` - tab
`\r` - carriage return
`\b` - backspace
`\f` - form feed

``+`` operator used with strings is called concatenation operator
can also use ``+=`` operator to concatenate

you can put variables between strings using ``+`` concatenation operator or ``+=`` operator

Write ``.length`` after a string to get the character count of a string. 
and ```example.length``` to get length of string attached to the example variable

use bracket notation to get character in a string. Starts counting at 0 as in most programming languages, rather than one. 

string values are immutable so can't change [0] value, can only reassign the whole string. 

In order to get the last letter of a string, you can subtract one from the string's length, so ``[x.length-1]``

Use array to store several bits of data in one place
array, e.g. ``x=['a','b', 'c']``
no "" for numbers

can also nest arrays within arrays, known as a multidimensional array
access array data using indexes, using square bracket notation.  ``x=[["a",1],["b",2]]``. NB square brackets arround array. 

individual data in arrays can be changed - mutable, unlike characters in strings. 

you can acess arrays within arrays using the notation, e.g. ``x[0][0]``

`.push()` takes one or more parameters and "pushes" them onto the end of the array
`.unshift()` to add element to start of array - just like push. 

`.pop()` is used to pop a value off of the end of an array - this can then be stored as a variable

`.shift()` to remove first value of array

written like ``var1.shift(var2 here)``
where var1 is variable to change and var2 is variable to add


can write reusable code called functions, 
e.g. ``function functionName() {console.log("Hello World");}``
invoke function by writing: ``functionName()``

```console.log``` to print result 

parameters are placeholders for values to come later, so could be like ``x=[param1,param2]``

``function functionWithArgs(param1, param2) {console.log(param1+param2)}``
``functionWithArgs(2,4)``
outputs: 6 

You can use a `return` statement to send a value back out of a function - e.g. ``return x + 3``
Vending machine analogy - u get something out of a function to use in other parts of code.

variables declared outside functions are global 
variables inside functions are local - only visible in that function

you can have both local and global variables with the same name - local will overwrite the global one

undefined values are when there isn't a return statement - just get an edit to the global variable

queue - data structure where items are kept in order - new items are at back of queue and old items at the front

boolean values  - true or false 

if statements tell javascript whether to play code

``if (condition is true) {statement is executed}``
then afterwards write what to do if not true (false), and another curly bracket

many comparison operators, like equality operator (``==``) which compares two things and if they're the same, gives true or false if not

Javascript can compare two different data types (for example, `numbers` and `strings`) with the equality operator, using type conversion. 
But it does not do this with the strict equality operator (``===``) - there they have to be exact

Can use ``typeof`` operator to get type of a variable - like 1 is number and '1' is string. 

The inequality operator (``!=``)
The strict inequality operator (`!==`)
``>`` greater than operator
``>=`` greater than or equal to operator
``<`` less than operator
`<=` The less than or equal to operator 

The logical and operator (`&&`) returns `true` if and only if the operands to the left and right of it are true.

The logical or operator (`||`) returns `true` if either of the operands is `true`.











**floating point** number is a decimal
when try to add/multiply etc. any two strings together you get ``NaN`` (not a number)

in javascript everything is case-sensitive, and for variable names we use camelCase - thisIsCamelCase. First word is lowercase and all subsequent words start with uppercase. Look like camel humps. kebab-case and other examples for other coding languages. 

Naming variables: 

Good to be specific with variable names, especially if you want it to be clear that a boolean is expected, e.g.  saying ``isLightOn`` rather than ``light``. Easier when reading back code or showing to others. Some basic rules: 
-   makes clear what **data type** is being held
-   conveys the purpose of the value being held
-   is descriptive without being too long and difficult to read

An **expression** is any code that resolves to a single value

A piece of data used by an operator is called an **operand** - e.g. ``4*5``,  4 and 5 are operands. 
using operators to get a calculation is an example of evaluation. 

**exponentiation** operator, `**` - 2**3 = 2 to power of three 


`example.replace` to change the variable, then ('x', 'y') after to change part of  the string x to y. 
`Math.round()` rounds to nearest integer
`example.toString()` makes number a string

``total += i`` adds i to total in forLoop

forLoop is 3 expressions that run over and over

``for (_expression 1_; _expression 2_; _expression 3_) {  
  // _code block to be executed_  
}``
where expression 1 is first statement, expression 2 is conditional statement, such as x>y, and expression 3 is executed every time after code block executed (often incremental)



when doing array filtering, syntax is important! Can often change values and use an existing function

index number for arrays - 0,1,2 etc. for a, b and c in array. 

with objects,  example.pizza  and  example['pizza']  are the same thing










