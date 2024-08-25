/* No.1: Write a function that can…

Return the string “I am a function” :scream:
Hint: this function doesn’t need to be passed any arguments!

Should return something like:

"I am a function" */

function printMe (){
  console.log('I am a function')
}

/*
No.2: Write a function that can…

Take a number as an argument, and return a new value that is 1 less than the argument. 

For example, if I called your function like so

yourFunction(23);

it should return

22 */

function oneLess (num){return num -1}
oneLess(23)





/*
No.3: Write a function that can…

Speak back to you! :wave: Whatever argument you pass to your function, it should simply return that argument back.

So

argumentRepeater("Lemon");

should return

"Lemon"
*/ 

function repeatArgument(argument){return argument}
repeatArgument("Lemon")

/*
No.4: Write a function that can…

Take two numbers as arguments, and return the sum of them 

For example, if you call your function like this:

addTwoNumbers(12, 56);

should return

68 */ 

function addTwoNumbers(num1, num2){return num1 + num2}
addTwoNumbers(12, 56)




/*
No.5: Write a function that can…

Say who it was written by! :sunglasses:

Your function should take a name as an argument, and return the string “This function was written by ____”

So

yourFunction("Charlie");

should return

"This function was written by Charlie"

Hint: the “+” key may come in handy… */ 

function  whoWroteThis (name){return "This function was written by " + name}
whoWroteThis("Charlie")

/*
No.6: Write a function that can…

Take 4 numbers as arguments. It should take the sum of the first two arguments, multiply it by the sum of the last two arguments, and return the result :+1:

So

yourFunction(2, 3, 6, 4);

should return

50

Hint: using multiple variables inside the statement of your function might make things easier…
*/ 

function(num1, num2, num3, num4){return (num1 + num2) * (num3 +num4)}


/*
No.7: Write a function that can…

Take a string as an argument, and return the length (how many characters) of that string. :straight_ruler:

So

yourFunction("How long is this string?");

should return

24

Hint: This freeCodeCamp challenge may help you if you’re stuck, or try reading up in the MDN docs
*/ 


function howLongIsThisString(string){return string.length}

/* 
No.8: Write a function that can …

Take a number as an argument and returns half that number

So

yourFunction(42)

should return

21

and

yourFunction(11)

should return

5.5
*/ 

function halfNumber(num){return num/2}


/* 
No.9: Write a function that can …

Take two numbers as arguments.

If both arguments are equal, return the string "The first and second arguments are equal"
If the arguments are not equal, return the string "The first argument ___ does not equal the second argument ___ ".

So

yourFunction(1, 1)

should return

"The first and second arguments are equal"

and

yourFunction(1, 2)

should return

"The first argument 1 does not equal the second argument 2"

Hint: You’ll need to use an if statement…
*/

function areTheyEqual(arg1, arg2){
    if (arg1 === arg2){return "The first and second arguments are equal"}
else {return "The first argument " + arg1 + " does not equal the second argument " + arg2}
     }

/*
No.10: Write a function that can …

Take two numbers as an argument and returns the smallest one.

So

yourFunction(11, 2)

should return

2

and

yourFunction(1, -111)

should return

-111 */ 

function findSmallestOne(num1, num2){return Math.min(num1, num2)}

/*

No.11: Write a function that can …

Take three numbers and returns true if the numbers are ascending in size, and false otherwise.

So

yourFunction(1, 4, 9)

should return

true

and

yourFunction(4, 1, 10)

should return

false

*/ 

function areTheyAscending(num1, num2, num3){
    if ((num1 < num2) && (num2 < num3)) {return "true"} 
    else {return "false"}
  }


/*
No.12: Write a function that can …

Concatenate two strings.

So

yourFunction('hi ', 'there')

should return

'hi there'
*/ 
function concatenateTwo (arg1, arg2){return arg1 + arg2}


/*
No.13 Write a function that can …

Take an array and a number and return the element of the array at that index. If the number is not a valid index, return null.

So

yourFunction([7, 3, 5], 2)

should return

5

and

yourFunction([0, 5, 3], 9)

should return

null

Hint: you will need to find the length of the array first, remember zero indexing…

*/

function findNumber(arr,num){
    if (num >= arr.length) {return null}
    else {return arr[num]}
  }


/*
No.14 Write a function that can …

Take an object, a string, and another value.

If the object contains a key that matches the string, return the value corresponding to that key.

If the object does not contain a key that matches the string, return the third argument.

So

yourFunction({ name: 'felicia', age: 23 }, 'age', 0)

should return

23

and

yourFunction({ name: 'felicia', age: 23 }, 'nickname', 'none')

should return

'none'
*/ 

function findValue(obj, string, value){
    if (obj[string] !== undefined) {return obj[string]}
    else {return value}
}

/*
No.15 Write a function that can …

Take an object whose values are all numbers, and return the sum of those numbers

So

yourFunction({ a: 12, b: -4, c: 0.4 })

should return

8.4
*/ 

function addNumbers (obj){
    let total = 0
    for (const key in obj){total+=obj[key]}
    return total
}

addNumbers ({ a: 12, b: -4, c: 0.4 })

/* COMPLETE :) */