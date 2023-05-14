## The DOM  (document object model)

```
const paragraphs = document.querySelectorAll("p");
```

This returns all the paragraph (p) elements in the document

built using multiple APIs (Application Programming Interface) that work together

Most web developers will use javascript with the DOM, but it also works with other programming languages like Python.

Can be thought of as a tree - parent child sibling, body head etc. 


almost always starts with ``document``, so is ``document.someMethod()``

1. ``document.getElementById()`` 
e.g. ``document.GetElementById('main heading')``
can set this to equal ``const title``
and then ``console.log(title)``

2. ``document.getElementsByClassName()``
e.g. ``document.getElementsByClassName('list-items')``

4. ``document.getElementsByTagName()``
e.g. ``document.getElementsByTagName('li')``

5. ``document.querySelector()``
 select with CSS selector, e.g. ``("button")``
 selects the first item which matches

5. ``document.querySelectorAll()``
select multiple elements with same CSS selector. returns a NodeList of matching elements



Element is the javascript representation of element on page, once set to variable

You can get the id, className of an element using DOM. 
e.g. 
```
const btn = document.querySelector("button");
console.log(btn.className, btn.textContent, btn.clientHeight);
// "btn--primary", "Hello", 44
```

``element.addEventLister`` allows us to react to user actions

addEventListener requires:
		1. Type - click, submit etc. 
		2. Listener - function run when event happens

```
btn.addEventListener("click", handleClick);
```

some common events:
click  - usually button trigger
keydown - add keyboard controls
change - reacting to updates in an input
submit - get results of submitted form


## updating the DOM 

after user acrtion, can change elements or add new element 
e.g. 
``const btn = document.querySelector("button");
``btn.id = "set-from-js";``
this overrides any other values

can use `element.classList.add` to add multuple class names, or add one without overwriting previous, e.g. 
```
btn.classList.add("btn--primary");
```

remove : ``element.classList.remove``

toggle: ``element.classList.toggle``
if it exists, will remove. If not, will add it

``.hidden`` decides if something is hidden completely in browser, e.g. ``button.hidden = true;``

you can also create new elements in JavaScript



Basic to do list showing DOM manipulation in action
https://codepen.io/oliverjam/pen/zbBxOz 

My forked copy with delete buttons: 
https://codepen.io/jones58/pen/rNqdwYJ


MDN reference here: 
https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction


can add ``deleteButton.addEventListener('click', handleDelete);`` event listeners for elements when you create them. This way don't have to select element separately 
\





## forEach selector 
e.g. buttons.forEach(function buttonClicked(button) {
button.addEventListener("click", handleClick => {
button.style.backgroundColor = "green";
});
