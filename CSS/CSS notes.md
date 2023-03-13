
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

Don’t forget the for attribute with labels ! When used together with the <label> element, the for attribute specifies which form element a label is bound to.

Input type=”submit” value=”submit” for submit button !

To make a link, use a element wrapped around text. As in <a href=www.google.com>Google</a>. 

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

Inline styles - style using style attribute, eg. <Div style=“color:red”> in the html doc, is very messy tho so don’t do it. 
Or with rulesets, eg. Div {Color:red} where select the element. Can do in the html doc, eg. Div {Color:red} and with <style type=“text/css”> div {Color:red} </style> in the head element. This is not a good idea tho, best to do in separate css document. 

Use class=“x”, in elements and then .x {} . Is the selector.  
Eg. <h1 class=“x”> </h1> 

[attribute="value"]  selector targets any element with an attribute of specific value. So can go x [attribute="value"] to target x class with specific attribute and value.

the key difference between `tr[class="total"] and ``tr.total`` is that the first will select `tr` elements where the _only_ class is `total`. The second will select `tr` elements where the class _includes_ `total`.

vertical-align:top or bottom for text vertical, text-align: for horizontal (left and right)

An `absolute` position takes the element out of that top-down document flow and allows you to adjust it relative to its container. 

When an element is manually positioned, you can shift its layout with `top`, `left`, `right`, and `bottom`. 


Elements with a higher `z-index` value will appear to be layered on top of elements with a lower `z-index` value

`border-radius: 50%`; to make more circular