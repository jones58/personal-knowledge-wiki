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
@mixin box-shadow($x, $y, $blur, $c){ 
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

