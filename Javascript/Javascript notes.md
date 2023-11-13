## Javascript notes

You can do frontend, backend, mobile apps - pretty much every area of development you can use javascript for.

### Web browser

Each web browser has an embedded Javascript engine.

engine reads ("parses") code and converts ("compiles") to machine code.

The compiled code then runs in the browser.

## Linking JS to HTML

can write in head or at bottom of body.

If in head, got to use `defer`, e.g.

`  <script src="myscript.js" defer></script>`

## Properties and Methods

Properties

- qualities of our data - values that we can work with or change

Methods

- actions - do something to / with the data

## Naming in Javascript

In javascript everything is case-sensitive, and for variable names we use camelCase - thisIsCamelCase. First word is lowercase and all subsequent words start with uppercase. Look like camel humps. kebab-case and other examples for other coding languages.

## Template Literals

- Make sure you wrap your statement in backticks ''
- Wrap the varaible inside ${variable}. E.g.

``console.log(`My name is ${firstName}.`);``

Line break in Javascript with: `\n`

## Comments

- Use `//` for single line comments
- Use `/* */` for multi line comments

///

## Running Javascript

To run javascript in vs code just click play button in top right.

NB scripts go to bottom of body in HTML, like so: `<script src="scripts/main.js"></script>`

## Primitive Data Types

8 primitive data types in js:

- `undefined`
- `null`
- `boolean`
- `string`
- `symbol`
- `bigint`
- `number`
- `object`

bigint is a big integer, number with more than 15 digits - e.g. `9007199254740991n`

Symbols are used to create unique identifiers, e.g. `Symbol('name')` or `Symbol.for('name')` to create a unique symbol.

## Variable declarations

Let - variable that can be changed.

Const - variables you don't want the value to be changed, keep it constant.

var - sets variable. Avoid using for now.

## Operators

`++` operator - using this operator, we write `x++;` which is equivalent to `x=x+1;`
likewise `--` operator: `x--;` is same as `x=x-1;`
`+=` operator - `x+=5;` is same as `x=x+5`
similarly, -=operator `x-=5;` is same as `x=x-5`
also, `*=` operator `x*=5;` is same as `x=x*5`
similarly `/=` operator `x/=5` is same as `x=x/5`

These work like this because everything to right of equals sign is evaluated first.
remainder operator - `%` eg. `5 % 2= 1;`

`+` operator used with strings is called concatenation operator
can also use `+=` operator to concatenate

you can put variables between strings using `+` concatenation operator or `+=` operator

## String methods

Write `.length` after a string to get the character count of a string.
and `example.length` to get length of string attached to the example variable

use bracket notation to get character in a string. Starts counting at 0 as in most programming languages, rather than one.

string values are immutable so can't change [0] value, can only reassign the whole string.

In order to get the last letter of a string, you can subtract one from the string's length, so `[x.length-1]`

## Escape characters

when you need a quote or double quote within a string `
`"this is a string"`you use \ backslash to escape the quote. So,`"this is a string \"with a quote\""`- it is always`\"`` whether at start or end of quote

Single and double quotes work same in javascript, but you've got to have it start and end with same one. Sometimes you mix so you can have quoted text in the string. Can also do this when using `<a>` tags nested in strings.

There are other forms of the escape character too -
`\'` - single quote
`\"` - double quote
`\\` - backslash
`\n` - newline
`\t` - tab
`\r` - carriage return
`\b` - backspace
`\f` - form feed

## Arrays

Use array to store several bits of data in one place
array, e.g. `x=['a','b', 'c']`

can also nest arrays within arrays, known as a multidimensional array
access array data using indexes, using square bracket notation. `x=[["a",1],["b",2]]`. NB square brackets arround array.

individual data in arrays can be changed - mutable, unlike characters in strings.

you can acess arrays within arrays using the notation, e.g. `x[0][0]`

## Array Methods

`.push()` takes one or more parameters and "pushes" them onto the end of the array
`.unshift()` to add element to start of array - just like push.

`.pop()` is used to pop a value off of the end of an array - this can then be stored as a variable, so can do `popped = arrayName.pop()`

`.shift()` to remove first value of array - this can then be stored as a variable, so can do `shifted = arrayName.shift()`

can be written like `var1.shift(var2 here)` where var1 is variable to change and var2 is variable to add

`example.replace` to change the variable, then ('x', 'y') after to change part of the string x to y.
`Math.round()` rounds to nearest integer
`example.toString()` makes number a string

Can be written as `toLocaleString()` when needs to meet local number format (like local date)

and `.toString(radix)` can output to different formats - like 2 is binary, 8 is octal and 16 is hexadecimal format.

.join() to join elements of array together. e.g. `x.join(' ')` will make a string with each element separated by a space.

.sort() to sort array in ascending order, e.g.

```js
x.sort((a, b) => a - b);
```

this will sort the array in ascending order, numerically.

for letters we can just use sort, e.g.

```js
x.sort();
```

## Functions

can write reusable code called functions,
e.g. `function functionName() {console.log("Hello World");}`
invoke function by writing: `functionName()`

`console.log` to print result

parameters are placeholders for values to come later, so could be like `x=[param1,param2]`

`function functionWithArgs(param1, param2) {console.log(param1+param2)}`
`functionWithArgs(2,4)`
outputs: 6

You can use a `return` statement to send a value back out of a function - e.g. `return x + 3`
Vending machine analogy - u get something out of a function to use in other parts of code.

variables declared outside functions are global
variables inside functions are local - only visible in that function

you can have both local and global variables with the same name - local will overwrite the global one

undefined values are when there isn't a return statement - just get an edit to the global variable

queue - data structure where items are kept in order - new items are at back of queue and old items at the front

if statements tell javascript whether to play code

`if (condition is true) {statement is executed}`
then afterwards write what to do if not true (false), and another curly bracket

many comparison operators, like equality operator (`==`) which compares two things and if they're the same, gives true or false if not

Javascript can compare two different data types (for example, `numbers` and `strings`) with the equality operator, using type conversion.
But it does not do this with the strict equality operator (`===`) - there they have to be exact

Relying on loose equality, which uses the `==` operator, is risky and can make our code behave unpredictably - always use the strict equality operator `===`

all comparison operators return a boolean `true` or `false` operator

`>` greater than operator
`>=` greater than or equal to operator
`<` less than operator
`<=` The less than or equal to operator

The logical and operator (`&&`) returns `true` if and only if the operands to the left and right of it are true, otherwise resolves to false.

The logical or operator (`||`) returns `true` if either of the operands is `true`. Also known as the pipe.

logical not operator `!` or bang operator
`! true = false
`! false = true

The inequality operator (`!=`)
The strict inequality operator (`!==`) - nb one equals missing compared to others

**floating point** number is a decimal
when try to add/multiply etc. any two strings together you get `NaN` (not a number)

Can test whether something is NaN (not a number) with `isNaN(x)` where x is the number. GIves true or false, e.g. `let answer = isNaN(x)`

Naming variables:

Good to be specific with variable names, especially if you want it to be clear that a boolean is expected, e.g. saying `isLightOn` rather than `light`. Easier when reading back code or showing to others. Some basic rules:

- makes clear what **data type** is being held
- conveys the purpose of the value being held
- is descriptive without being too long and difficult to read

An **expression** is any code that resolves to a single value

A piece of data used by an operator is called an **operand** - e.g. `4*5`, 4 and 5 are operands.
using operators to get a calculation is an example of evaluation.

**exponentiation** operator, `**` - `2**3` = 2 to power of three

String literal - adding different strings together easily
variables inside expressed with `${}` and all converted to strings.
for string literals, encased in backticks

String property to access more info about a variable
e.g length, we use dot syntax
`const exampleLength = example.length`

`const lastCharacter = blogPost[blogPost.length - 1]` often use length to get last value in a string

String methods - things that can be performed on data
ie. `.toUpperCase()` and `.toLowerCase()` (as they're functions, you need brackets)

always remember to use let or const when defining variable for first time

Can use `Console.log()` for debugging
Can use `typeof` operator to get type of a variable - like 1 is number and '1' is string. Combine with `console.log()` to print to console

if want to calculate within console.log with type of (typeof (variable one + variable two)) - note extra brackets.

single line comment in javascript - `//`
multuple line comment - ``/_ comment here _/

right click, run code in vscodium

in javascript, pseudocode is plain english writing in comments that breaks down the steps needed to code

error messages help to debug

- syntax error - something written wrong, like forgotten speech marks around a string.
- reference error - trying to reference a variable that isn't available, ie not declared
- type error - trying to do something which isn't right for that type of value - i.e. change number to uppercase

truthy values are not true but evaluate as true in boolean contexts - any number (except 0), any string, objects and arrays

falsy values evaluate to false - - `false` , `0`, an empty **string** `''`, `NaN`, `undefined`, `null`

We can check for to see if a variable has a falsy value with a simple conditional:

```javascript
if (!variable) {
  // When the variable has a falsy value the condition is true.
}
```

if else statements generate fork - if can't evaluate first statement as true, `else`... next one
syntax is `if..."else if"...else`
basically just chain if statements together

## Conditional (Ternary) operator

```javascript
condition ? expressionIfTrue : expressionIfFalse;
```

can chain them by putting : in between as many times, e.g.

```javascript
return age < 16 ? "children" : age < 50 ? "young man" : "old man";
```

This is often a better way of writing if else statements, e.g.

```js
function findGreater(a, b) {
  if (a > b) {
    return "a is greater";
  } else {
    return "b is greater or equal";
  }
}
```

can be rewritten as :

```js
function findGreater(a, b) {
  return a > b ? "a is greater" : "b is greater or equal";
}
```

can then chain like so:

```js
function findGreaterOrEqual(a, b) {
  return a === b
    ? "a and b are equal"
    : a > b
    ? "a is greater"
    : "b is greater";
}
```

##  Switch statements

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

If a negative **number** is used as an index, then the index is counted from the _end_ of the array - `-1` would be the position of the _last_ item in the array.

## Array Methods

- `.slice()` - use to extract information from an array into new array. The first argument is the array **index** that the slice should start; the second argument is the array index the slice should go up to, but not include. ie, .slice(0, 2) - will read first and second values, up to but not including third
- .splice () - The **`splice()`** method changes the contents of an array by removing or replacing existing elements and/or adding new elements [in place](https://en.wikipedia.org/wiki/In-place_algorithm). It can take two variables - index position and number of elements to remove. Or it can take three variables, where third is element to add. Can be as many numbers here as you want Returns a new array.
- .flat () - The **`flat()`** method creates a new array with all sub-array elements concatenated into it, in effect flattening all nested arrays into a single array.
- .includes() - determines whether an array includes a certain value, gives `true` or `false`
- .indexOf() - returns first index at which a value is present, or -1 if it's not present
- .reverse () - reverses the order of elements in array

## Loops and Iterations

### For loops

```javascript
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

Can't use .length property on numbers - so have to convert it to string first: so instead of `.toString`, write as `.toString().length`

You can also nest loops, e.g. just use j inside i

```js
for (let i = 0; i < arr.length; i++) {
for (let j = 0; j < arr[i].length; j++) {
    console.log(arr[i][j]);
```

## While loops

while loop executes statement when test condition is true.
e.g.

```javascript
while (n < 5) {
  n++;
  console.log("n = " + n);
}
```

## Do while loops

Executes until the test condition is false - so will run at least once

```Javascript
do {
i++;
console.log("i = " + i);
}
while (i < 5);
```

can write in `if ( condition) continue`, continue takes back to start of the loop, whereas
`break` stops it

## Objects

`const variable = { key : value } `
often called key value pair. common between them. e.g. key:value, key:value.

NB sometimes will look like a key value pair but won't be e.g. `x:y` - this one can do `.split(":")` and then `[0]` or `[1]` for x and y. For this will need to convert to string first cos can only split string.

can use dot notation to search, e.g. `variable.key`

if it has spaces, then have to use bracket notation as variable `["key with spaces"]`

sometimes the key is stored in a variable - ie not predetermined. this is a dynamic key

can assign properties to objects and reassign, e.g. `variable.key = "something"`
if using dynamic key, use bracket notation
nb don't use let ... for this

as well as assigning and reassigning values to properties can delete. e.g. `delete variable.key` or set value to `null`

objects can be nested within other objects, using `{ }` inside followed by usual `key : value` then access as `variable.key.key`

Can write functions within objects and then call them, e.g.

```
const person = {
  firstName: "John",
  lastName: "Doe",
  id: 5566,
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
};
```

this is known as an object method. When we call it we write `person.fullName()`

## This keyword

The this keyword is used to refer to the current object. In a method, `this` refers to the owner object.

In global use, `this` refers to the global object (usually window in a browser or global in Node.js).

In a function, `this` refers to the object that the function is a method of. For example, if you have an object myObject and you call myObject.myMethod(), `this` in this inside myMethod refers to myObject.

- In an event handler, `this` refers to the element that triggered the event - e.g. onClick()

- In a constructor function (used with the new keyword), `this` refers to the newly created instance of an object.

- arrow functions don't have their own `this` keyword - `this` refers to the global object.

Example use of this keyword in an object function:

```javascript
const alarm = {
  weekdayAlarm: "Get up at 7:00am.",
  weekendAlarm: "Sleep in! It's the weekend!",
  checkAlarm: function (day) {
    if (day === "Saturday" || day === "Sunday") {
      return this.weekendAlarm;
    } else {
      return this.weekdayAlarm;
    }
  },
};
console.log(alarm.checkAlarm("Saturday"));
```

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
remember escape keys! 'Anne's' written as 'Anne\'s'

## For...of loops

Same as above, just loop through key values instead of key names
In arrays for in will just give the indexes, while for of will give the values.

```js
for (const value of variableName) { code to be executed}
```

can also be used on arrays, like so:

```js
const array1 = ["a", "b", "c"];

for (const element of array1) {
  console.log(element);
}
```

## Functions

invoke a function by writing `functionName()`
functions can have more than one parameter
use `return` to return a value which can be used elsewhere and changed
`Return` is last part of code in function - can't run any more code after that

in a for loop, use answer = false or answer = true and then return answer instead of just doing return false or return true, cos that will overwrite for each entry, each time the loop runs

`break` to exit a for loop when answer is found - i.e. first odd number

`%` - remainder operator

in javascript `...` is known as the spread operator - `...myArray ` means all the values in an array are passed into function as individual elements.

Math.floor() - round down
Math.ceiling() - round up

NB must put return...function at end of function
NB when putting new key and value in an object, must put key in " "
NB when adding keys to object, should be 'seat': not 'seat: ' basically colon shouldn't be in quote marks
NB when put return in a loop it stops it looping - don't do it!

## Events

`document.querySelector("html").addEventListener("click", function () {
`alert("Ouch! Stop poking me!");
``});

## Arrow functions

Arrow functions differ in that they don't have a name in the same way and they don't use the `function` keyword. They also cannot be hoisted - must be defined before use.

e.g.

```js
const myFunc = () => {
  const myVar = "value";
  return myVar;
};
```

can be simplified further - since no function body and only a return value we can omit the keyword return and brackets cos return is implicit in arrow function.

```js
const myFunc = () => "value";
```

You can pass arguments into arrow functions:

```js
const doubler = (item) => item * 2;
doubler(4);
```

if just one item, can get rid of brackets:

```js
const doubler = (item) => item * 2;
```

Can also pass two values, like so:

```js
const multiplier = (item, multi) => item * multi;
multiplier(4, 2);
```

## Anonymous functions

`function ()` this is an anonymous function cos it doesn't have a name

these anonymous functions are useful when don't need to name functions to use elsewhere, epecially when passing function as argument to another function

so e.g.:

```js
const myFunc = function () {
  const myVar = "value";
  return myVar;
};
```

## Switch statements

Use Switch statements to test one value against multiple options.
E.g.

````js
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
````

NB when you set a variable, it should be =0, = "" depending on what you want it to be. Will default to string if not set. So something will end up being NaN even if numbers are added to it.

Can also use a lookup object rather than switch or if else chain. Most useful when input data is limited to certain range of values.

## Arrays

when defining new empty array - can write
`let arr = new Array()` or `let arr = []`
you can check if array is empty or not with .length, e.g.
``if (arr.length === 0){console.log("array is empty")}

We can manipulate strings with `.padStart()` which pads the start of the string with another string until it reaches a given length. e.g. padding text with 0 until it reaches the length of 4: `text.padStart(4,"0");`

## Number objects

There are other ways to convert numbers to strings:

- `.toFixed()` - specifies the number of decimal places, e.g. `3.1415.toFixed(2)` will make it `3.14`
- `.toExponential()` - writes it as exponential, e.g. `100,000.toExponential()` becomes `1.0e+5`, 1 and 5 zeroes. The number in the brackets is as above, the precision of the decimal places.
- `.toPrecision()` - controls total number of digits, e.g. `123.4563.toPrecision(6)` becomes `123.456`

We can turn this string back into a number with either:

- `parseInt()` - converts to integer
  - `ParseInt(string, radix)` - which turns string into a number with radix (like binary etc.)
- `parseFloat()` - converts to decimal - can also be written as just `+` in front of a string
  For each - the number goes in the (), not as a .

## Checking Objects for Properties

Use `.hasOwnProperty`, e.g.
`object.hasOwnProperty(property)` will return true or false

or can use `in` - `property in object` will return true or false

## Recursion

Recursion states that a function can be expressed in terms of itself, a function within function

e.g.

```js
function solve(a, b) {
  if (a === 0 || b === 0) {
    return [a, b];
  } else if (a >= 2 * b) {
    a = a - 2 * b;
    return solve(a, b);
  } else if (b >= 2 * a) {
    b = b - 2 * a;
    return solve(a, b);
  } else {
    return [a, b];
  }
}
```

NB when using recursion we must use return when calling the function - e.g. `return solve(a, b);` here.

In recursion, it keeps going until it reaches a base case, e.g. here the base case is when a = 0 or b = 0.

## Generating random numbers

Use `Math.random()` to create a random decimal between 0 and 1. Can be 0 but can't be 1.

From there can make a random number less than 20 by using `Math.floor(Math.random() * 20);`
`Math.floor()` rounds number down to nearest whole number

can do this between a range of two number using min and max values, like so:

`Math.floor(Math.random() * (max - min + 1)) + min`

## Prevent object mutation

Use `Object.freeze(objectName)` - this will stop any variables in the object being redeclared

## Console

Can just right click, inspect, on any web element to open dev tools for that element

can do `console.log()` a value to print it to the console
`console.clear()` to clear the console
and `console.warn()` to print a warning message along with warning icon

can write like this if want to reference a value:``console.log(`Net working capital is: ${netWorkingCapital}`);``

## Copy with the spread operator

```js
let thatArray = [...thisArray];
```

copy with just `...`

Can add arrays within other arrays using spread operator too, like so:

```js
let thatArray = ["basil", "cilantro", ...thisArray, "coriander"];
```

## indexOf

`.indexOf()` to check for presence of element in array, will return the index of that element or -1 if not present. E.g. `fruits.indexOf('pears')`

## Generate an Array of All Object Keys with Object.keys()

Use `Object.keys([ArrayName])` to generate a new array of all the keys in an object. Won't have specific order because generating from an object

## Convert values to Boolean

`!!value ` will evaluate as true or false

There are 6 falsy values in JS: ```

```js
false
undefined
null
NaN
0
"" (empty string)
```

## Using Sort Operator

`.sort()` will sort an array of values based on their unicode values, in ascending order. This not always useful cos numbers 5, 62 etc. would be ordered like that cos only takes first number. So we use a compare function within the sort:
`arr.sort((a, b) => a - b);`

## Default parameters

Use default parameters to trigger default behaviour if a variable not specified, e.g.

```js
const greeting = (name = "Anonymous") => "Hello " + name;
```

Will give hello Annonymous unless name is otherwise specified

Can also be written in normal functions as so:

```js
function greeting(name = "Anonymous") {
  return "Hello " + name;
}
```

## Rest parameter

Represent an indefinite number of arguments in a function. Useful to define any length of array, e.g.

```javascript
function sum(...numbers) {
  let total = 0;
  for (let number of numbers) {
    total += number;
  }
  return total;
}
console.log(sum(1, 2, 3, 4)); // Output: 10
```

## Spread operator

Used to expand or "spread" elements from an array using `...`

## setTimeout and setInterval

`SetTimeout` executes a function or a piece of code once after a delay. e.g.

```javascript
setTimeout(() => {
  console.log(
    "This will be executed after 1000 milliseconds (1 second)."
  );
}, 1000);
```

`setInterval` function is used to repeatedly execute a function or a piece of code at a specified interval. e.g.

```javascript
setInterval(() => {
  console.log(
    "This will be executed every 1000 milliseconds (1 second)."
  );
}, 1000);
```

Will keep repeating until `clearInterval()` is called with the corresponding interval Id or the program ends. e.g.

```javascript
const intervalId = setInterval(intervalFunction, 1000);
clearInterval(intervalId);
```

## Closures

Closures are functions that can access variables from outside of their scope, even when the function has finished executing.

Often used to encapsulate private variables.

stored in heap memory rather than stack memory (long term vs short term)

e.g.

```js
function encapsulatedState(x) {
  let state = 10;
  return function () {
    state += x;
    return state;
  };
}
```

See also:
[[Regular-expressions]]
