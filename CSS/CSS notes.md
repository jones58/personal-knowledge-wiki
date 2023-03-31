
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

Fix to top of viewport: position:fixed and top=0. 

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

An `absolute` position takes the element out of that top-down document flow and allows you to adjust it relative to its container. 

When an element is manually positioned, you can shift its layout with `top`, `left`, `right`, and `bottom`. 


Elements with a higher `z-index` value will appear to be layered on top of elements with a lower `z-index` value

`border-radius: 50%`; to make more circular


to add multiple classes to an element: <div class="class1 class2 class3"></div>

meta tag ends />

The `::before` selector creates a pseudo-element which is the first child of the selected element, while the `::after` selector creates a pseudo-element which is the last child of the selected element.

The `@media` at-rule, also known as a media query, is used to conditionally apply CSS. Media queries are commonly used to apply CSS based on the viewport width using the `max-width` and `min-width` properties.



trick to see elements and their size, use: 
``* {border: 1px solid black;}
and then remove this at the end when finished editing

The `flex-direction` property has four possible values:
1.  `row`: This is the default value. It arranges flex items horizontally in a row from left to right.
2.  `column`: It arranges flex items vertically in a column from top to bottom.
3.  `row-reverse`: It arranges flex items horizontally in a row from right to left.
4.  `column-reverse`: It arranges flex items vertically in a column from bottom to top.

To set flex direction, also need ``display:flex;`` set to make it flexbox container 


To declare a variable in CSS, you can use the `--` prefix followed by a name for the variable and its value. 

e.g. `--myfirstvariable: blue` then ``var(--myfirstvariable)`` to call the variable 



Here are some of the most common values for `justify-content`:

1.  `flex-end`: This value aligns the items to the end of the container, which is typically the right side in a left-to-right language such as English.
2.  `center`: This value centers the items within the container horizontally.
3.  `space-between`: This value distributes the items evenly along the main axis of the container, with the first item aligned to the start and the last item aligned to the end. The remaining items are spaced out evenly between them.
4.  `space-around`: This value distributes the items evenly along the main axis of the container, with equal spacing between each item and the container edges.
5.  `space-evenly`: This value distributes the items evenly along the main axis of the container, with equal spacing between each item and the container edges, as well as between each pair of adjacent items.
6.  `stretch`: This value stretches the items to fill the container along the main axis, which can be useful when the items have different widths or when you want to fill any remaining space in the container.

Each of these values can be used with the `justify-content` property in CSS to achieve different horizontal alignment styles for flex items within a flex container.

When "flex-wrap: wrap" is applied to a flex container, it allows the flex items to wrap onto multiple lines if there is not enough space within the container to fit them all on one line.