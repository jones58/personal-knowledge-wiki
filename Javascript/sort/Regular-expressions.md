Match parts of strings by creating patterns to help matching. 

Multiple methods, one of which is ``.test()`` which applies regex to string and returns true or false, e.g. 

```js
let testStr = "freeCodeCamp";
let testRegex = /Code/;
testRegex.test(testStr);
```

you can use the or operator to search for more than one thing: e.g. `/yes|no|maybe/` is yes or no or maybe

flag that ignores case - the `i` flag - add this to end of the regex, e.g. ``/Code/i``

Can also use the ``.match()`` method, which is opposite of ``.test()`` method and returns the actual match of the regex. e.g. 
```js
let ourStr = "Regular expressions";
let ourRegex = /expressions/;
ourStr.match(ourRegex);
```
will return `["expressions"]`

Use the global search -  ``g`` flag to search/extract pattern more than once. 

NB can have multiple flags, so e.g. ``/Code/ig``

Can use wildcard character to match any one character, e.g. `/hu./` matches  `hug`, `huh`, `hut`, and `hum`

Use character classes to match group of characters inside ``[]`` square brackets - e.g. `/b[aiu]g/` matches bag big and bug but not bog. 

match a group of characters with -, e.g ``[a-e]`` matches letters a to e. 

can also search for range of numbers, and combine with letters like so: ``let myRegex = /[a-z0-9]/ig;``

create a set of characters you don't want to match with negated character sets - using caret character ``^``
e.g. `/[^aeiou]/gi` matches all non-vowels

``+`` - Match characters that occur one or more times with (has to be consecutive). 
``*`` -  Match characters that occur zero or more times (e.g. ``/go*/`` matches "goal", "gut", but not "over".) 

## Lazy matching
 so far, has been greedy matching returns the longest possible string which matches the pattern. Lazy matching gives smallest possible with the ``?`` character. e.g. `/t[a-z]*?i/` on titanic returns ``["ti"]`` not ``[titani]`` as it would be without the ``?`` . 


Can also use ``^`` outside of character set square brackets, just to see if something is first in string. 

```js
let firstString = "Ricky is first and can be found.";
let firstRegex = /^Ricky/;
```
Can use ``$`` at end to see if at end of string: 

```js
let theEnding = "This is a never ending story";
let storyRegex = /story$/;
```

shorthand character class for alphanumeric characters is ``\w`` which is equal to `[A-Za-z0-9_]`
opposite of alphanumeric characters can be represented as ``\W`` which is equal to `[^A-Za-z0-9_]`

can look for just numbers/digits with ``\d`` which is equal to `[0-9]`
to look for non-digits, us `\D` which is equal to `[^0-9]`


The character class `[ \r\t\f\n\v]` represents a set of characters that includes whitespace and control characters. Let's break down the individual components:

- (space): Matches a regular space character.
- `\r` (carriage return): Matches the carriage return control character, which is commonly used in certain text file formats.
- `\t` (tab): Matches the tab control character, which is used for indentation or spacing purposes.
- `\f` (form feed): Matches the form feed control character, which is used for page breaks or similar purposes.
- `\n` (newline): Matches the newline control character, which is typically used to start a new line in text.
- `\v` (vertical tab): Matches the vertical tab - rarely used but can be present in certain text files. 



`\s` is a shorthand character class that searches for whitespace, as well as carriage return, tab, form feed, and new line characters.
``\S`` will search for everything except whitespace, carriage return, tab, form feed, and new line characters. 


Search for lower and upper range of patterns with quantitity specifiers, which go in ``{}`` curly brackets, e.g. ``/a{3,5}h/`` to match a occuring 3-5 times in string. 
if you only want to specify lower number - just omit larger one, like so: ``/a{3,}h/``
if you want to specify only one number - omit comma, so ``/a{3}h/``

Check for zero or one of an element, basically an optional element using ``?``, e.g. ``
``/colou?r/`` will match both color and colour, the u is optional. 

## Lookaheads

Lookaheads to look for pattern ahead. Can be positive and negative.
Postive lookead will check to see if pattern is there but won't match it `(?=...)` where ``...`` is the thing you want to check,e.g. ``a``
Negative lookahead will check to see if pattern is not there ``(?!...)`` where ``...`` is the thing you want to check isn't there 

Better use of lookaheads is to check two or more patterns in string, e.g. ``let checkPass = /(?=\w{3,6})(?=\D*\d)/;``



Found this bit of Regex very difficult: 
``let myRegex = /(Franklin|Eleanor) (([A-Z]\.?|[A-Z][a-z]+) )?Roosevelt/;``

## Capture Groups 

Find repeated patterns using Capture Groups, which enclose repeated bit in paratheses - so repeated alphanumeric sequence ``\w+`` becomes ``/(\w+)/`` 
substring matched is saved to temporaty variable, accessible via the backslash and number of capture group - e.g. ``\1`` . auto numbered by position of opening paretheses (left to right) starting at 1. 
e.g. this shows a repeating word, that repeats three times `
``let repeatRegex = /(\w+) \1 \1/;``


Can replace text you match with capture group, using ``.replace()`` on string. e.g. 
```js
let wrongText = "The sky is silver.";
let silverRegex = /silver/;
wrongText.replace(silverRegex, "blue");
```

this would return ``the sky is blue.``
can also access capture groups with dollar sign + number of capture group. 




Regular Expressions explained by Fireship: https://www.youtube.com/watch?v=sXQxhojSdZM 

Regex cheatsheet: https://fireship.io/lessons/regex-cheat-sheet-js/ 

Regexr to understand and test regex: https://regexr.com/


`\b`: This is a word boundary assertion that ensures the pattern occurs at the end of a word. It prevents a match if the pattern is followed by another alphanumeric character.