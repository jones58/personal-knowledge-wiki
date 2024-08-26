---
title: Sass
---

## Variable names

In Sass, variables start with a `$` followed by the variable name.
e.g.

```scss
$main-fonts: Arial, sans-serif;
$headings-color: green;
```

and

```scss
h1 {
  font-family: $main-fonts;
  color: $headings-color;
}
```

## Nesting

Can nest in sass, e.g. :

```scss
article {
  height: 200px;

  p {
    color: white;
  }

  ul {
    color: blue;
  }
}
```

## Mixin

Mixin is a group of CSS declarations that can be reused throughout the style sheet. Kind of like functions for CSS.

```scss
@mixin box-shadow($x, $y, $blur, $c) {
  -webkit-box-shadow: $x $y $blur $c;
  -moz-box-shadow: $x $y $blur $c;
  -ms-box-shadow: $x $y $blur $c;
  box-shadow: $x $y $blur $c;
}
```

where ($x, $y, $blur, $c) are parameters

and then call it with

```scss
div {
  @include box-shadow(0px, 0px, 4px, #fff);
}
```

where you can state the parameters. This means that everytime you want to write out webkit... etc. you don't have to write it all.

## If and Else

can use if and else just as in Javascript:

```scss
@mixin text-effect($val) {
  @if $val == danger {
    color: red;
  } @else if $val == alert {
    color: yellow;
  } @else if $val == success {
    color: green;
  } @else {
    color: black;
  }
}
```

## for loops

similar to for loops in javascript.

either `@for` "start through end" or "start to end"

- "start **to** end" excludes end number
- "start **through** end" includes end number

e.g.

```scss
@for $i from 1 through 12 {
  .col-#{$i} {
    width: 100%/12 * $i;
  }
}
```

## each

each is like for loop but it iterates over each item in list or map
example in list:

```scss
@each $color in blue, red, green {
  .#{$color}-text {
    color: $color;
  }
}
```

and for map:

```scss
$colors: (
  color1: blue,
  color2: red,
  color3: green,
);

@each $key, $color in $colors {
  .#{$color}-text {
    color: $color;
  }
}
```

the $key variable helps us read the different values - the colors here.

## while loops

similar to js while loops - keep going until reaches a value

```scss
$x: 1;
@while $x < 13 {
  .col-#{$x} {
    width: 100%/12 * $x;
  }
  $x: $x + 1;
}
```

## partials and file types

Partials are small bits of css in separate files. File type for sass files is generally .scss

partials start with `_` - which tells Sass it is css segment and not sass to be converted into css

to bring code from partial into another sass file - use `@import`
e.g.

```scss
@import "mixins";
```

nb don't need \_ or file extension to call it.

## extend

`@extend` lets us add values from one class to another, without rewriting everything out:
