You can add Bootstrap to any app by adding the following code to the top of your HTML:

```html
<link
  rel="stylesheet"
  href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
  integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
  crossorigin="anonymous"
/>
```

Bootstrap will figure out how wide your screen is and respond by resizing your HTML elements - hence the name responsive design.

no need to design for mobile and desktop.

Bootstrap uses a 12-column grid system.

can wrap all html elements in div with class of fluid container, to fit to full width of container.

Fortunately, with Bootstrap, all we need to do is add the `img-responsive` class to your image. Do this, and the image should perfectly fit the width of your page.

add class of `text-center` to centre text

## Buttons

Bootstrap has predefined styles and colors for buttons.

`btn` and `btn-default` to style button - better than default html

`btn-block` to take up 100% of available space

`btn-primary` for main color - actions you want user to take

`btn-info` for info buttons, optional actions

`btn-danger` for dangerous/destructive actions - e.g. deleting an image on site.

## column width

`col-md-*` sets column width for medium screen (e.g. laptop)

where \* is number of columns wide the element is

`col-xs-*` for extra small screen (like extra small mobile phone screen)

so normally you set up a row and then split that into columns `<div class="row">`

`well` class to give visual sense of depth for columns: `<div class="well"></div>`

## Span

By using the inline `span` element, you can put several elements on the same line, and even style different parts of the same line differently.

you can use span element or i element for use with icons - e.g. from font awesome

## forms

`"form-control"` class gives 100% width to form element that it's applied to

not every class has css - sometimes set class so easier to select it with jQuery
