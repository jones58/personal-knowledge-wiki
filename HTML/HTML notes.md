
 - Write ! to write boilerplate code in html - this is an emmet abbreviation
 - cmd - /  will make a comment in html 
 - to write a paragraph of lorem ipsum just write lorem and press return
 - Block element takes up the whole line - like heading or paragraph
 - Inline element will only take the space they need, like image
 - href= hypertext reference
- Syntax for the For attribute in label, <label for = “”> text </label>
- Don’t need required=”yes” attribute in input, just put required. 
- Add a pattern attribute to the password input element to require the input match. pattern=[a-z0-5]{8,} 8 letter letter or numbers
- Link using: ```<a>href="URL">text here </a>```
- notes: em is a CSS unit relative to the font size of the parent element, while rem is a CSS unit relative to the font size of an html element. 
- div tags are very generic layout elements while fieldset is a layout element specifically for a set of form fields.
- Meta tags are self closing. 
- The HTML span element is a generic inline container for inline elements and content. It is used to group elements for styling purposes (by using the class or id attributes), A better way to use it is when no other semantic element is available. 


- Meta content: ```width=device-width, initial-scale=1``` helps with accessibility.
- Submit a form to a certain place: ```form method="post" action="webaddress.org"```
- ```Input type=”date”``` for dates in forms
- Notes: The name attribute is used when sending data in a form submission. Different controls respond differently. For example, you may have several radio buttons with different id attributes, but the same name. When submitted, there is just the one value in the response - the radio button you selected.
- Src for bringing in images, href for linking external sites. 
- If you want to add google font, has to be linked in head of html and applied in CSS. 
- The thead and tbody elements are used to indicate which portion of your table is the header, and which portion contains the primary data or content.
- <a href=“www.google.com”>hello I’m a link</a>
- to auto open link in new tab - add ```target =“_blank”``` to anchor opening tag 
- Add title = “….” To get hover over message when hover over, eg click to find out more. This is also known as a tooltip.
- ``<img src=“image link>`` 
- Images don’t have closing tags cos can’t put anything in it 
- To make line break - ``<br>``- no closing tag cos can’t put anything in it (it’s not a container
- ``<span>`` elements are used as blank boxes with no default styles and inherit their style from the 
element they're inside of (e.g. h1 etc.)
- all span elements inside h1 is written as h1 span or h1>span i think
- a styles.css can be applied to many different html pages :) 
- for planning site, box wireframes are useful and can make boxes that contain other boxes. Html is boxes inside boxes. 
- What comes first in code comes first on page. 
- Can put as many boxes inside boxes as you want. 
- HTML boxes expand to fit what you put inside them and to fill the available space. 
- The `style` attribute is used to add styles to an element, such as color, font, size, and more, e.g. ```<p style=color:red>text here<p>```
	- ``<_tagname_ style="_property_:_value;_">``
	- Used to apply css properties in html. 
- ``<hr>`` makes a horizontal rule in the html.
- ```<pre>``` element - denotes preformatted text. Keeps line breaks and spaces of what's inside and puts text in a fixed width font. 
- ``<b>`` wrapped around makes text bold
- ``<strong>`` wrapped around denotes text as strong, usually displayed as bold
- ``<i>`` wrapped around makes text italic
- ``<em>`` wrapped around denotes text as emphasised, usually displayed as italic

- To click on nav bar to get to one section, set `<a href="#sectionid">`, where section id is the id set for that section. also for the a elements, set to ``cursor:pointer;`` in CSS. 

- HTML uses ``<abbr>`` for abbreviations - written as ``<abbr title="World Health Organisation">WHO</abbr>``

HTML comments: ``<!-- This is a comment -->`` - NB you can use comments to hide things temporarily, e.g. for debugging. 

To use an image as a link, just put the `<img>` tag inside the `<a>` tag. 

With [HTML image maps](https://www.w3schools.com/html/html_images_imagemap.asp) you can define clickable areas on an image.

Use HTML ``<picture>`` tag to set different images for different screen sizes. This can save data and make images load quicker, especially where they're not needed in high resolution (e.g. mobile phone)

The `<param>` tag is used to define parameters for an ``[<object>]`` element. Can do things like autoplay videos or audio.  


## HTML lists 
- ul for unordered lists, ol for ordered lists. 
-  can write type of list as number or letter with type and which it starts with with start
 ```html
```<ol type="a" start="10">
	<li>HTML</li>
	<li>CSS</li>
	<li>Javascript</li>
	</ol> 
```

Type = "disc" This is the default style. In this style, the list items are marked with bullets.
Type = "circle" In this style, the list items are marked with circles.
Type = "square" |In this style, the list items are marked with squares.
Type = "none" In this style, the list items are not marked. 

These can be applied to ordered and unordered lists, whereas with i, a, 1 etc. can only be applied to ordered lists: 

Type = "1" This is the default type. In this type, the list items are numbered with numbers.
Type = "I" In this type, the list items are numbered with upper case roman numbers.
Type = "i" In this type, the list items are numbered with lower case roman numbers.
Type = "A" In this type, the list items are numbered with upper case letters.
Type "a"  In this type, the list items are numbered with lower case letters.
- dl for descriptions lists, with dt and dd for define term and define description

## block vs inline 
- Block is a full width element that starts on new line. E.g. ``<div>``
- Inline element doesn't do that, and just fits in with other elements on same line. E.g. ``<span>``

## head elements 
- ``<base>`` used to set the base url for links on a page, use with href and/or target. 

Use a ``<figure>`` element to mark up a photo in a document, and a ``<figcaption>`` element to define a caption for the photo

Can easily create buttons, use: ``<button type="button">Click Me!</button>`` and then style them with CSS. 

``<audio>`` elements - use mp3 is best for compatibility


## Titles 

``h1 - h6``  for headings. 

## HTML Tables 

https://www.w3schools.com/html/html_tables.asp  is good resource on this 

- Use ``table border="1"`` to make it look like a proper table
- Then set table rows to give it rows (NB you don't set columns)
- Then use either ``th`` or ``td`` to give table head or table data within that row
- Then next row and so forth. 
- Can add images within ``td`` tags. 
- Use rowspan or colspan to edit width/height of table elements - e.g. can take up two rows, or two columns. See example below. 

<table border="1">

<tr>

<th>First name</th>

<th>Surname</th>

<th>Description</th>

<th>Picture</th>

</tr>

<tr>

<td>James</td>

<td>Bond</td>

<td>International Spy</td>

<td>

<img

width="100"

height="100"

src="https://imgs.search.brave.com/EXxrxxMV6LzwwODBSyDJXB-ZgKAaGJ1U59HuDtbx6ik/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5ncS1tYWdhemlu/ZS5jby51ay9waG90/b3MvNjMzNzBmN2Fh/NDA2ZmM0OTM5OTY2/ZWRhLzE6MS9wYXNz/L0phbWVzLWJvbmQt/V2F0Y2hlcy5qcGc"

/>

</td>

</tr>

<tr>

<td>Daniel</td>

<td>Craig</td>

<td>Actor</td>

<td>

<img

width="100"

height="100"

src="https://imgs.search.brave.com/9aTltuF2CHtk90VfoVeT-FsoAWn8vIo_MMeOCNGdN8k/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/MDA3LmNvbS93cC1j/b250ZW50L3VwbG9h/ZHMvMjAyMi8xMS9Q/VF9iZWluZ19ib25k/LTQ1Mng2NzguanBn"

/>

</td>

</tr>

<tr>

<td>Thomas</td>

<td>The Tank Engine</td>

<td>He's a train</td>

<td>

<img

width="100"

height="100"

src="https://imgs.search.brave.com/SmZKpetiKKv-S8w0YjdZMA38U8GksgFhIP9dD1cEdjg/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tLm1l/ZGlhLWFtYXpvbi5j/b20vaW1hZ2VzL00v/TVY1QlpXWXdNek14/WTJZdE0yRmxaaTAw/WTJVeExUa3dNemN0/TURka1pHWXpORGxr/TlRJMlhrRXlYa0Zx/Y0dkZVFYVnlOelUx/TnpFM05UZ0AuanBn"

/>

</td>

</tr>

</table>

```html
<table border="1">

<tr>

<th>First name</th>

<th>Surname</th>

<th>Description</th>

<th>Picture</th>

</tr>

<tr>

<td>James</td>

<td>Bond</td>

<td>International Spy</td>

<td>

<img

width="100"

height="100"

src="https://imgs.search.brave.com/EXxrxxMV6LzwwODBSyDJXB-ZgKAaGJ1U59HuDtbx6ik/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5ncS1tYWdhemlu/ZS5jby51ay9waG90/b3MvNjMzNzBmN2Fh/NDA2ZmM0OTM5OTY2/ZWRhLzE6MS9wYXNz/L0phbWVzLWJvbmQt/V2F0Y2hlcy5qcGc"

/>

</td>

</tr>

<tr>

<td>Daniel</td>

<td>Craig</td>

<td>Actor</td>

<td>

<img

width="100"

height="100"

src="https://imgs.search.brave.com/9aTltuF2CHtk90VfoVeT-FsoAWn8vIo_MMeOCNGdN8k/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/MDA3LmNvbS93cC1j/b250ZW50L3VwbG9h/ZHMvMjAyMi8xMS9Q/VF9iZWluZ19ib25k/LTQ1Mng2NzguanBn"

/>

</td>

</tr>

<tr>

<td>Thomas</td>

<td>The Tank Engine</td>

<td>He's a train</td>

<td>

<img

width="100"

height="100"

src="https://imgs.search.brave.com/SmZKpetiKKv-S8w0YjdZMA38U8GksgFhIP9dD1cEdjg/rs:fit:860:0:0/g:ce/aHR0cHM6Ly9tLm1l/ZGlhLWFtYXpvbi5j/b20vaW1hZ2VzL00v/TVY1QlpXWXdNek14/WTJZdE0yRmxaaTAw/WTJVeExUa3dNemN0/TURka1pHWXpORGxr/TlRJMlhrRXlYa0Zx/Y0dkZVFYVnlOelUx/TnpFM05UZ0AuanBn"

/>

</td>

</tr>

</table>
``` 

<table border="1">

<tr>

<td rowspan="2">State of health</td>

<td colspan="2">Fasting value</td>

<td>After eating</td>

</tr>

<tr>

<td>Minimum</td>

<td>Maximum</td>

<td>2 hours after eating</td>

</tr>

<tr>

<td>Healthy</td>

<td>70</td>

<td>100</td>

<td>Less than 140</td>

</tr>

</table>

```html
<table border="1">

<tr>

<td rowspan="2">State of health</td>

<td colspan="2">Fasting value</td>

<td>After eating</td>

</tr>

<tr>

<td>Minimum</td>

<td>Maximum</td>

<td>2 hours after eating</td>

</tr>

<tr>

<td>Healthy</td>

<td>70</td>

<td>100</td>

<td>Less than 140</td>

</tr>

</table>
```




