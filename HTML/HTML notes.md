 - <!--  --> is an **HTML comment**.
 - href= hypertext reference
- Syntax for the For attribute in label, <label for = “”> text </label>
- Don’t need required=”yes” attribute in input, just put required. 
- Add a pattern attribute to the password input element to require the input match. pattern=[a-z0-5]{8,} 8 letter letter or numbers
- Link using: ```<a>href="URL">text here </a>```
- notes: em is a CSS unit relative to the font size of the parent element, while rem is a CSS unit relative to the font size of an html element. 
- div tags are very generic layout elements while fieldset is a layout element specifically for a set of form fields.
- Meta tags are self closing. 
- The HTML span element is a generic inline container for inline elements and content. It is **used to group elements for styling purposes (by using the class or id attributes), A better way to use it when no other semantic element is available**.
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


See also [[Media queries notes]]
