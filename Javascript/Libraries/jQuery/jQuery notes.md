
```html
<script>$(document).ready(function() {}); </script>
```
document ready function to make sure code doesn't run until html is loaded. 

all jQuery functions start with $

`.addClass()` to add class to an element, and 
``.removeClass()

e.g. 
```js
$("#target2").removeClass("btn-default")
```

``.css()`` function : 
change an element's color to blue: 
```js
$("#target1").css("color", "blue");
```

can also change non-css properties of HTML elements. 
`.prop()` - adjust properties of elements 

e.g. disable button: 
```js 
$("button").prop("disabled", true);
```

can change text too. `.html()` lets you add HTML tags and text within an element - completely replacing any other text inside. 

use ``.text()`` to change the text (not tags) of an html element

`.remove()` - will remove an HTML element entirely.

``.appendTo()`` select HTML elements and append them to another element

``.clone()`` to copy HTML element 

can use function chaining - sticking two functions on top of each other. 

`parent()` allows you to acess parent of element you've selected. 
`children()` that allows you to access the children of whichever element you've selected.
