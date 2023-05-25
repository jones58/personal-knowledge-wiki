To run javascript in vs code  (using code runner extension) - just do ``cmd-shift-p`` and type run code and it will come up in output 

NB scripts go to bottom of body in HTML, like so: <script src="scripts/main.js"></script>

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


`example.replace` to change the variable, then ('x', 'y') after to change part of  the string x to y. 
`Math.round()` rounds to nearest integer
`example.toString()` makes number a string


Can be written as ``toLocaleString()`` when needs to meet local number format (like local date)

and ``.toString(radix)``  can output to different formats - like 2 is binary, 8 is octal and 16 is hexadecimal format. 


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

Relying on loose equality, which uses the `==` operator, is risky and can make our code behave unpredictably - always use the strict equality operator `===` 

all comparison operators return a boolean ``true`` or ``false`` operator

``>`` greater than operator
``>=`` greater than or equal to operator
``<`` less than operator
`<=` The less than or equal to operator 

The logical and operator (`&&`) returns `true` if and only if the operands to the left and right of it are true, otherwise resolves to false. 

The logical or operator (`||`) returns `true` if either of the operands is `true`.

logical not operator ``!`` or bang operator 
``! true = false
``! false = true

The inequality operator (``!=``)
The strict inequality operator (`!==`) - nb one equals missing compared to others 

**floating point** number is a decimal
when try to add/multiply etc. any two strings together you get ``NaN`` (not a number)

Can test whether something is NaN (not a number) with ``isNaN(x)`` where x is the number. GIves true or false, e.g. ``let answer = isNaN(x)``


in javascript everything is case-sensitive, and for variable names we use camelCase - thisIsCamelCase. First word is lowercase and all subsequent words start with uppercase. Look like camel humps. kebab-case and other examples for other coding languages. 

Naming variables: 

Good to be specific with variable names, especially if you want it to be clear that a boolean is expected, e.g.  saying ``isLightOn`` rather than ``light``. Easier when reading back code or showing to others. Some basic rules: 
-   makes clear what **data type** is being held
-   conveys the purpose of the value being held
-   is descriptive without being too long and difficult to read

An **expression** is any code that resolves to a single value

A piece of data used by an operator is called an **operand** - e.g. ``4*5``,  4 and 5 are operands. 
using operators to get a calculation is an example of evaluation. 

**exponentiation** operator, `**` - ``2**3`` = 2 to power of three 

String literal - adding different strings together easily 
variables inside expressed with `${}` and all converted to strings. 
for string literals, encased in backticks 

String property to access more info about a variable
e.g length, we use dot syntax
const exampleLength = example.length

``const lastCharacter = blogPost[blogPost.length - 1]`` often use length to get last value in a string

String methods - things that can be performed on data
ie. `.toUpperCase()` and `.toLowerCase()` (as they're functions, you need brackets)

always remember to use let or const when defining variable for first time

Can use ``Console.log()`` for debugging
Can use ``typeof`` operator to get type of a variable - like 1 is number and '1' is string.  Combine with ``console.log()`` to print to console

if want to calculate within console.log with type of  (typeof (variable one + variable two)) - note extra brackets. 

single line comment in javascript - ``//``
multuple line comment - ``/* comment here */

right click, run code in vscodium

in javascript, pseudocode is plain english writing in comments that breaks down the steps needed to code

error messages help to debug
- syntax error - something written wrong, like forgotten speech marks around a string. 
- reference error - trying to reference a variable that isn't available, ie not declared
- type error - trying to do something which isn't right for that type of value - i.e. change number to uppercase


truthy values are not true but evaluate as true in boolean contexts - any number (except 0), any string, objects and arrays 

falsy values evaluate to false - -   `false` , `0`, an empty **string** `''`, `NaN`,   `undefined`, ``null``

We can check for to see if a variable has a falsy value with a simple conditional:

```javascript
if (!variable) {
  // When the variable has a falsy value the condition is true.
}
```

if else statements generate fork - if can't evaluate first statement as true,  ``else``... next one
syntax is ``if..."else if"...else``
basically just chain if statements together 

## Ternary operator 

```javascript
condition ? expressionIfTrue : expressionIfFalse
```
can chain them by putting : in between as many times, e.g. 
```javascript
return age < 16 ? "children" : age < 50 ? "young man" : "old man";
```



## Switch statements 

```switch (expression) {
  case value1:
    // code to execute if expression matches value1
    break;
  case value2:
    // code to execute if expression matches value2
    break;
  default:
    // code to execute if expression does not match any of the cases
}
```


if multiple cases have same result, you can write as 
case 1: 
case 2: 
	code to execute


if using lots of expressions and && operators etc, and it's not working, then put them in () so it's clear what's happening and nothing gets processed wrong. 

with slices: 
If a negative **number** is used as an index, then the index is counted from the _end_ of the array - `-1` would be the position of the _last_ item in the array.

The first argument is the array **index** that the slice should start; the second argument is the array index the slice should go up to, but not include. ie, .slice(0, 3) - is 1st - 3rd but not 4th value. 


## Other Array Methods

- .splice () - The **`splice()`** method changes the contents of an array by removing or replacing existing elements and/or adding new elements [in place](https://en.wikipedia.org/wiki/In-place_algorithm).
- .flat () - The **`flat()`** method creates a new array with all sub-array elements concatenated into it, in effect flattening all nested arrays into a single array. 
- .includes() - determines whether an array includes a certain value, gives `true` or `false`
- .indexOf() - returns first index at which a value is present, or -1 if it's not present 
- .reverse () - reverses the order of elements in array


## For loops

```
for (start; stop; step) {
  // code to execute
}
```

start expression, e.g let i=10; 
stop expression, e.g. i <3; - when this is no longer true, loop stops. 
step expression, eg. i++ , i+1, add one each time loop is run 
code could be console log

NB. the step expression runs at the end of the step, when the code has executed. 

NB got to have for.. 

for loops can be used with arrays, giving one example of iteration 

can use if statements within for loops

even numbers: 
```
let numbers = [2, 4, 5, 6, 9, 10, 11, 12]

// Start writing your code below

for (let i=0;i<numbers.length; i++){

if (numbers[i]%2===0)

console.log(numbers[i])

}
```

Can't use .length property on numbers - so have to convert it to string first: so instead of ``.toString``, write as ``.toString().length``


## Objects 

``const variable = { key : value } ``
often called key value pair. common between them. e.g. key:value, key:value. 

NB sometimes will look like a key value pair but won't be e.g. ``x:y`` - this one can do ``.split(":")`` and then ``[0]`` or ``[1]`` for x and y. 

can use dot notation to search, e.g. ``variable.key``

if it has spaces, then have to use bracket notation as variable ``["key"]``

sometimes the key is stored in a variable - ie not predetermined. this is a dynamic key

can assign properties to objects and reassign, e.g. ``variable.key = "something"``
if using dynamic key, use bracket notation
nb don't use let ... for this 

as well as assigning and reassigning values to properties can delete. e.g. ``delete variable.key`` or set value to ``null`` 

objects can be nested within other objects, using ``{ }`` inside followed by usual ``key : value``  then access as ``variable.key.key``

## For...in loops

``for (const key in variableName) { code to be executed}

We can use variable keys and bracket notation to dynamically access the value of keys: 
```javascript
for (let key in obj) {
  const value = obj[key];
```

We do this when we don't know he name of the keys and want to access the values inside them

NB must have the const in for in loops

nb you can have for loops inside for in loops

when accessing a property in objects, got to write is as string, " " "
remember escape keys!  'Anne's' written as 'Anne\'s'

## For...of loops

Same as above, just loop through key values instead of key names
In arrays for in will just give the indexes, while for of will give the values. 

## While loops 
while loop executes statement when test condition is true. 
e.g. 
```javascript
while (n<5){
n++;
console.log("n = " +n);
}
```

## Do while loops
Executes until the test condition is false - so will run at least once

``` Javascript
do { 
i++;
console.log("i = " + i);
}
while (i < 5);
```

can write in ``if ( condition) continue``, continue takes back to start of the loop, whereas 
``break`` stops it


## Functions

invoke a function by writing ``functionName()``
 functions can have more than one parameter 
 use ``return`` to return a value which can be used elsewhere and changed 
 ``Return`` is last part of code in function - can't run any more code after that

in a for loop, use answer = false or answer = true and then return answer instead of just doing return false or return true, cos that will overwrite for each entry, each time the loop runs



``break`` to exit a for loop when answer is found - i.e. first odd number 

``%`` - remainder operator


in javascript ``...`` is known as the spread operator - ``...myArray `` means all the values in an array are passed into function as individual elements. 

Math.floor() - round down
Math.ceiling() - round up 


NB must put return...function at end of function
NB when putting new key and value in an object, must put key in " "
NB when adding keys to object, should be 'seat': not 'seat: ' basically colon shouldn't be in quote marks 
NB when put return in a loop it stops it looping - don't do it! 

## Events

``document.querySelector("html").addEventListener("click", function () {
``alert("Ouch! Stop poking me!");
``});

``function ()`` this is an anonymous function cos it doesn't have a name
	can also be written as `() =>`  - an arrow function 



## Switch statements 

Use Switch statements to test one value against multiple options. 
E.g. 
```js
switch (fruit) {
  case "apple":
    console.log("The fruit is an apple");
    break;
  case "orange":
    console.log("The fruit is an orange");
    break;
}```

``case`` uses strict equality === operator  and ``break`` stops the function if runs through that bit (i.e. if fruit is apple, console logs then breaks(ends) the function) 

Sometimes can't use case for everything so have to set ``default`` like ``else`` in else if : e.g 
```js
switch (num) {
  case value1:
    statement1;
    break;
  case value2:
    statement2;
    break;
...
  default:
    defaultStatement;
    break;
}
```

NB when you set a variable, it should be =0, = "" depending on what you want it to be. Will default to string if not set. So something will end up being NaN even if numbers are added to it.


## Arrays 
when defining new empty array - can write  
``let arr = new Array()`` or ``let arr = []``
you can check if array is empty or not with .length, e.g. 
``if (arr.length === 0){console.log("array is empty")}


We can manipulate strings with ``.padStart()`` which pads the start of the string with another string until it reaches a given length. e.g. padding text with 0 until it reaches the length of 4: ``text.padStart(4,"0");``



## Number objects 

There are other ways to convert numbers to strings: 
- ``.toFixed()`` - specifies the number of decimal places, e.g. ``3.1415.toFixed(2)`` will make it ``3.14``
- ``.toExponential()`` - writes it as exponential, e.g. ``100,000.toExponential()`` becomes ``1.0e+5``, 1 and 5 zeroes. The number in the brackets is as above, the precision of the decimal places.
- ``.toPrecision()`` - controls total number of digits, e.g. ``123.4563.toPrecision(6)`` becomes ``123.456``

We can turn this string back into a number with either: 
- ``parseInt()`` - converts to integer
- ``parseFloat()`` - converts to decimal
	- can also be written as just ``+`` in front of a string
For each - the number goes in the (), not as a . 

