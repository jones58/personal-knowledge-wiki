
- Three main ways to format content with CSS: 
	- [[CSS Flexbox]]
	- [[CSS Grid]]
	- [[CSS Float]]
- /\*  \*/  is a CSS comment
- Two classes selected: .class, .class not .class .class
- Notes:” flex-end is a value that can be assigned to the justify-content property and will align all the flex items to the right end of the container”
- Don’t use font-color, just use color. 
- X > y {  targets y elements within x elements. 
- Common pattern for screen reader only text:
	-```position: absolute;
	width: 1px; 
	height: 1px;
	padding: 0;
	margin: -1px;
	overflow: hidden;
	clip: rect(0, 0, 0, 0);
	white-space: nowrap;
	border: 0;``` 
- Set size of a textarea, rows= and cols= attributes. And placeholder= attribute. 

Don’t forget the for attribute with labels ! When used together with the `<label>` element, the for attribute specifies which form element a label is bound to.

Input type=”submit” value=”submit” for submit button !

To make a link, use a element wrapped around text. As in `<a href=www.google.com>Google</a>`

Get rid of underline – set text-decoration:none; 

Style elements on hover, use element.hover { }

Use flexbox, justify-content:space-between; align-items:center;


Align text, use text-align:… 

Use flexbox to wrap content - flexwrap:wrap; 

To get automatically centred, use margin:auto

` `If don’t want style for a list, use list-style:none.  

Justify-content:center to get in centre. 

To select x and y in css, use x,y {

To select all elements, use \* selector. 

Justify to end of flex box – justify-content:flex-end; 

Select class, put . before it 

Shift from top, set top:-225px etc. 

Fill viewport – width:100vw

CSS tricks is good for flexbox 

padding+margin: When three values are specified, the first one applies to the top, the second to the right and left, the third to the bottom. When four values are specified, they apply to the top, right, bottom, and left in that order (clockwise).

Property : property value ;

Can use as many property pairs as you want to style an element. 

Width, height, background-color, font-family, font-size

Inline styles - style using style attribute, eg. ``<Div style=“color:red”> in the html doc, is very messy tho so don’t do it. 
Or with rulesets, eg. Div {Color:red} where select the element. Can do in the html doc, eg. Div {Color:red} and with ``<style type=“text/css”> div {Color:red} </style>`` in the head element. This is not a good idea tho, best to do in separate css document. 

Use class=“x”, in elements and then .x {} . Is the selector.  
Eg. <h1 class=“x”> </h1> 
`[attribute="value"]` selector targets any element with an attribute of specific value. So can go `x [attribute="value"`] to target x class with specific attribute and value

the key difference between `tr[class="total"] and ``tr.total`` is that the first will select `tr` elements where the _only_ class is `total`. The second will select `tr` elements where the class _includes_ `total`.

vertical-align:top or bottom for text vertical, text-align: for horizontal (left and right)



Elements with a higher `z-index` value will appear to be layered on top of elements with a lower `z-index` value

`border-radius: 50%`; to make more circular


to add multiple classes to an element: <div class="class1 class2 class3"></div>

meta tag ends />

The `::before` selector creates a pseudo-element which is the first child of the selected element, while the `::after` selector creates a pseudo-element which is the last child of the selected element.




trick to see elements and their size, use: 
``* {border: 1px solid black;}
and then remove this at the end when finished editing

The `flex-direction` property has four possible values:
1.  `row`: This is the default value. It arranges flex items horizontally in a row from left to right.
2.  `column`: It arranges flex items vertically in a column from top to bottom.
3.  `row-reverse`: It arranges flex items horizontally in a row from right to left.
4.  `column-reverse`: It arranges flex items vertically in a column from bottom to top.

To set flex direction, also need ``display:flex;`` set to make it flexbox container 





Here are some of the most common values for `justify-content`:

1.  `flex-end`: This value aligns the items to the end of the container, which is typically the right side in a left-to-right language such as English.
2.  `center`: This value centers the items within the container horizontally.
3.  `space-between`: This value distributes the items evenly along the main axis of the container, with the first item aligned to the start and the last item aligned to the end. The remaining items are spaced out evenly between them.
4.  `space-around`: This value distributes the items evenly along the main axis of the container, with equal spacing between each item and the container edges.
5.  `space-evenly`: This value distributes the items evenly along the main axis of the container, with equal spacing between each item and the container edges, as well as between each pair of adjacent items.
6.  `stretch`: This value stretches the items to fill the container along the main axis, which can be useful when the items have different widths or when you want to fill any remaining space in the container.

Each of these values can be used with the `justify-content` property in CSS to achieve different horizontal alignment styles for flex items within a flex container.

When "flex-wrap: wrap" is applied to a flex container, it allows the flex items to wrap onto multiple lines if there is not enough space within the container to fit them all on one line.

The `loading` attribute on an `img` element can be set to `lazy` to tell the browser not to fetch the image resource until it is needed

meta and img self closing, end in /> v important! 


use the minmax function to set minimum and maximum sizes


The `object-fit` property tells the browser how to position the element within its container. In this case, `cover` will set the image to fill the container, cropping as needed to avoid changing the aspect ratio.

CSS Grid: this game is fun: https://cssgridgarden.com/ 

CSS Grid you can align the content of grid items with `align-items` and `justify-items`. `align-items` will align child elements along the column axis, and `justify-items` will align child elements along the row axis.

Often use ``box-sizing: border-box;`` to make boxes work better. Can also do ``border: 1px solid black;`` to make it more obvious where boxes are, then remove this towards end. 


To make video or image fill whole page: ``
 ``display: block;
  ``width: 100%;``

To make a form's input say "submit" instead of submit query, add this to input: 
``value="Submit"``

Remove horizontal and vertical scrollbars with: ``overflow:hidden;``

to target all descendents of an element ``.element * { }


empty string: `` '' ''`` which can be used as a value, e.g. color. 


The `:root` selector is used to define global CSS variables, also known as CSS custom properties. Global variables defined with `:root` are available throughout the entire document, making it easy to set and modify values that apply to the entire page.

For example, if you wanted to define a global variable for the primary color of your website, you could use the `:root` selector like this:
```css
:root {
  --primary-color: #007bff;
}
```


flip the x-axis when rotating an element: ``scaleX(-1)

border-radius shorthand = top left, top right, bottom right, bottom left

for other four value shorthand, like margin and padding = top value, right value, bottom value, left value

the `:active` selector is a pseudo-class that targets an element while it is being activated by the user. This typically refers to the moment when a user clicks on a link or a button, but it can also apply to other types of user interactions, such as when a user taps on an element on a touchscreen device.

indicate can't move something/use cursor on it: ``cursor:not-allowed;``

Using margin can tend to look strange when scrolling, best to use padding. 

Use css float property to let image float to left or right. 

CSS uses : where HTML uses = 


```css
```/* class selector */
• paragraph{
background-color: aqua;
}
/* tag selector */
h1{
background-color: coral;
｝
/* group selectors */
• heading3, • paragraph1, h2{
background-color: blue;
}
/* universal selector - select all elements */
* {
font-size: xx-large;
}

/* element.class  - elements with a class */
p. text{
background-color: blueviolet;
}
```


By default HTML elements will have a style - set by user agent stylesheet. This can be overwritten. 

Two main types of font: 
google fonts (web fonts) - 
web safe fonts - ones that come with most operation systems. 


Better to download fonts and compress them (if needed) to make website faster. 

``font-variant: small-caps;``
``font-style: italic;
``text-transform: uppercase;
``text-align: center;
``line-height: 30px;``
``letter-spacing: 2px;
``word-spacing: 5px;
``text-decoration: underline
``text-indent: 90px;

can also apply with 
``font: 30px bold Roboto; 
to apply multiple variables at once

for rgb values: 
can have between 0-255
for hsl values: 
hsl between 0-100

hsla - a is the transparency, e.g. ``background-color: hsla (250, 48%, 48%, 0.7)``

alpha can also be used with rgba 

most of the time opacity property will be better than using alpha 


## Backgrounds 

apply to body element to get in background for whole page

```css
background-image: url('/Image/download.jpg');
background-repeat: no-repeat; 
background-attachment: fixed; /* fixed position for the background image, rather than scrolling*/
background-size: cover; /* this will fill the element background */
background-position:top 30px right 20px; /* this will set position of background image*/
```
``repeat-y `` to repeat vertically
``repeat-x`` to repeat horizontally

cover will fill the space

can do a lot with backgrounds in css, e.g. multiple background images (use commas between different urls) or set repeat of the background image in different sections of the site. E.g.:  
```css
 background: url(star.png) no-repeat left center,
    url(star.png) repeat-y right center;
}```
this will have one of the image in left center, and repeated along y axis (vertically) on right side (aligned to center). Can then edit this with padding. 


## Borders

can use ``border-top``, ``border-right`` etc. to change border on difference sizes
``border-radius: 50%`` to make circle

``border-top-right-radius: ;`` to just round the corner on one corner

## Margin and padding

``/* margin: top right bottom left; */
``margin: 10px 5px 10px 5px;``
``text-align: justify;``


## Overflow 
``overflow: scroll`` - displays scrollbars, whether the content overflows the container or not.
``overflow:hidden`` - hide any content that overflows the container. 
`overflow: auto;` - show scrollbars only if content overflows container. 

##  Inline block 

can use ``display: inline-block`` to make an inline block element that can change its width and height

## Links

Styling links with CSS: 
``a:link`` - a normal link - unvisited link
``a:visited`` - a link that the user has visited
``a:hover`` - a link when the user mouse over it
``a:active`` - a link when you click it

``text-decoration:none`` to remove underline on text

increase padding on a element if want to make it look more like a button with background-color, etc. 


``text-align: justify;`` to align text justified

## Position

``position: static`` - the default property 
``position: relative`` - positioned relative to normal position. 
``position: absolute`` - takes element out of top-down document flow and allows to adjust relative to container
``position: fixed`` - position relative to viewport. Will always stay in same position on screen when scroll. Fix to top of viewport: position:fixed and top=0. 
``position: sticky`` - allows an element to scroll with the page until a specified position (e.g., `top: 50px`) is reached, at which point it becomes fixed in place, creating a "sticky" effect. It's commonly used for elements like navigation menus or sidebars that should stay visible while scrolling.

When an element is manually positioned, you can shift its layout with `top`, `left`, `right`, and `bottom`. 


## Z-index 

Highest z-index will display on top
By default all elements have z-index of 0
Can give ``z-index: -1 ``, or 1,2,3 etc. 


## Navigation bars

 can use ``<nav>`` and`` <ul>`` with ``<li>`` inside and set: ``list-style-type:none

use display:block to put stuff on different lines


## Media Queries 

Always changing breakpoints, get used to googling them based on which websites it will be used on. Mobile first design 

Example: @media (max-width: 600px){ 
} 

when debugging, if it doesn't look good on a screen size - use media queries


Take a mobile-first approach with media queries too - do the mobile look before desktop. 


Using the `max-width` and `min-width` properties.


https://www.w3schools.com/cssref/css3_pr_mediaquery.php
https://css-tricks.com/a-complete-guide-to-css-media-queries/
https://css-tricks.com/snippets/css/media-queries-for-standard-devices/


# Selectors

They're good to help you filter through your HTML. Don't necessarily need to use them if easiest to use classes or IDs, just as good to use them in that way. 

More info here: https://learn.shayhowe.com/advanced-html-css/complex-selectors/

## Pseudo-Elements

Only applies to a specific part of your element

::before
word before another one 

::after 
word after another one 

::first letter 
first letter 

::first line 
first line 

::selection
element selected by a user
## Pseudo-Classes

tells element how to behave in a certain setting:
:link - unclicked link
:visited - clicked link
:hover - hover  
:first child - first child in list / elements in a parent element
:last child - last child in list / elements in a parent element
input: enabled - enabled input elements
input: disabled - disabled input elements

## nth-child Selector

A pseudo class that selects children within parent elements

:nth child (odd) - this is odd elements in a parent element
:nth child (even) - this is even elements in a parent element

Can use maths in with this one

## Attribute Selectors

Select either attribute, attribute=value, or attribute with value containing string, ending in string, starting in string etc. 

```css 
  
/* Select anchor <a> elements with a href attribute */

a[href] {

font-family: "Courier New", Courier, monospace;

}

  

/* Style anchor <a> elements with a target attribute exactly equal to "_blank" */

a[target="_blank"] {

background-color: #ffee58;

font-weight: bold;

text-decoration: underline;

}

  

/* Style anchor <a> elements with a target attribute exactly equal to "_self" */

  

a[target="_self"] {

background-color: #ffee58;

font-style: italic;

text-decoration: overline;

}

  

/* Style anchor <a> elements with a title attribute containing the string "Tesco" */

a[href*="tesco"] {

border: 5px solid blue;

color: blue;

}

/* Style anchor <a> elements with a title attribute containing the string "Asda" */

  

a[href*="asda"] {

border: 5px solid green;

color: green;

}

  

/* Style anchor <a> elements with a lang attribute containing the string "fr" */

a[lang|="fr"] {

background-image: linear-gradient(

to right,

#0055a4 0%,

#0055a4 33.33%,

#ffffff 33.33%,

#ffffff 66.66%,

#ef4135 66.66%,

#ef4135 100%

);

}

  

/* Style anchor <a> elements which contain space-separated list of words, one of which is Fruit */

a[title~="Fruit"] {

border: 5px solid red;

}
```

## Parent and child 

.parent {} for parent elements and .child{} for child elements (elements that contain other elements and elements inside other elements)

## CSS Units 

em - relative to font size of the parent element
rem - relative to font size of the root element (html). by default is 16px. 
vh - relative to 1% of the height of the viewport
vw - relative to 1% of the width of the viewport
% - relative to parent element
viewport = the browser window size

## CSS Variables 

Can use so it's easier to change the variable colour, but can also use to change units

To declare a variable in CSS, you can use the `--` prefix followed by a name for the variable and its value. 

e.g. `--myfirstvariable: blue` then ``var(--myfirstvariable)`` to call the variable 

we store it in ``:root { }`` in css to make it a global variable. 
Can make local variable by just defining in one block/element

## CSS Transitions 

We can use keyframe and transition.

To create a transition effect, you must specify two things:
-the CSS property you want to add an effect to
-the duration of the effect

e.g. ``transition: width 1s;``

Uses active selectors like ``:hover`` etc. 

e.g. 
``transition-duration: 1s;``
``transition-timing-function:ease-in-out;``
``transition-delay: 0ms;``

more details on this: 
https://www.joshwcomeau.com/animation/css-transitions/

## CSS Animations

The `@keyframes` at-rule is used to define the flow of a CSS animation. Within the `@keyframes` rule, you can create selectors for specific points in the animation sequence, such as `0%` or `25%`, or use `from` and `to` to define the start and end of the sequence.

The `animation-name` property links `@keyframes` rule to a CSS selector/element - e.g. a ``heading``.

The `animation-duration` property sets how long an animation should take to complete. either in `s` or `ms`

The `animation-iteration-count` property is used to show how many times an animation should run, either a numnber or set to ``infinite``. 

The `animation-timing-function` property is used to set rate at which animation should run. Usually ``linear`` but there are other options too, like ``ease-in-out``

The animation-timing-function property can have the following values:
• ``ease`` - Specifies an animation with a slow start, then fast, then end slowly (this is default)
• ``linear`` - Specifies an animation with the same speed from start to end
• ``ease-in`` - Specifies an animation with a slow start
• ``ease-out`` - Specifies an armation with a slow end
• ``ease-in-out`` - Specifies an animation with a slow start and end
• ``cubic-bezier (n,n,n,n)`` - Lets you define your own values in a cubic-bezier function

``animation-direction`` to change direction of animation


Can also use ``animation`` property to set these all at once: the `animation-name`, `animation-duration`, `animation-timing-function`, and `animation-iteration-count` properties in that order.

``animation-delay:`` sets time in s until animation starts 

e.g: 
```css 
* Animation */

.animation {
background-color: brown;
width: 100px;
height: 100px;
animation-name: move;
animation-duration: 2s;
}

@keyframes move {
from {
margin-left: 0px;
}

to {
margin-left: 200px;
}
} ```

this is with from being 0% and to being 100%, but can also set with percentages: 

```css
```@keyframes move {
0{}
20%{
margin-left: 100px; I
｝
40%{
margin-left: 200px;
｝
60%{
margin-left: 200px;
margin-top: 100px;
｝```

## CSS Transform Property

Can skew, scale and translate, rotate. 

**Translate (move)**: `translateX()` and `translateY()` functions move the element horizontally and vertically, respectively. For example:
```css
transform: translateX(50px) translateY(20px);```
    
**Scale**: `scale()` function scales the element in both the X and Y axes. You can specify different values for scaling in the X and Y directions, which allows for non-uniform scaling. For example:
```css
transform: scale(1.5); /* Scales up by 1.5x in both X and Y */ transform: scaleX(2) scaleY(0.5); /* Scales 2x in X and 0.5x in Y */
```
    
**Rotate**: `rotate()` function rotates the element by a specified angle. For example:
```css
```transform: rotate(45deg);`
```


**Skew**: `skewX()` and `skewY()` functions skew the element in the X and Y directions, respectively. For example:
```css
transform: skewX(20deg) skewY(-10deg);
```

**transform-origin** : using ``transform-origin``  to specify the point around which the transformations are applied.



other notes: 
[[common-css-properties.pdf]]
[[CSS Grid]]
[[CSS Float]]
[[CSS Flexbox]]

