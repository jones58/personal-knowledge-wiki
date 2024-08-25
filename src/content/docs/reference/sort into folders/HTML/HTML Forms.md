https://www.w3schools.com/html/html_forms.asp

When writing form, use `for = ""` to link label with the input element

fieldset used to group form elements, then within that can use legend to label the group

````html
<fieldset>
‹legend›
Student registration
‹/legend>
<form action="">
‹label for="fname"›First Name</label>
<input type="text" id="fname" />‹br />
‹label for="email">Email</label>
‹input type="email" /><br />
‹ label for="gender">Gender: </label>
</fieldset>```


<fieldset>
	<legend>
	Student registration
	</legend>
	<form action="">
	<label for="fname"›First Name</label>
	<input type="text" id="fname" /><br />
	<label for="email">Email</label>
	<input type="email" /><br />
	<label for="gender">Gender: </label>
</fieldset>



``input type ="submit"`` to make a button
``‹input type-"password" placeholder="Enter Password" />`` to add password
``‹input type="checkbox" /≥``   checkbox
``‹input type="date" />`` - date
``‹input type="month" />`` - month
``‹input type="file" />`` - upload file
``<input type="number"/>`` - number
``<input type="range" />`` - slider for a range
``<input type = "reset" value = "clear all"/>`` will reset form data

``<textarea name="|"|| id="" cols="40" rows="30" maxlength ="10"></textarea>``


Create a dropdown list with:
```html
<select name="Country" id=""> I
<option value="UK">UK</option>
<option value="USA">USA</option>
<option value="Germany">Germany</option>
</select>
````

In database - it will only show the values.
