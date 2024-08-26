---
title: Css Grid
---

Helps us make two dimensional layout, when flexbox only lets us do one dimension. Rows and columns rather than just one or the other in flex.

`gap:` gives space between grid rows and columns

## grid-template-columns and grid-template-rows method

`grid-template-columns:`
`200px 200px` gives two columns of 200px
e.g. auto auto gives two columns based on size of content
`1 fr` will use all available space
`2 fr 1 fr` will mean 2 units of available space on left grid element, and 1 unit to right grid element
`repeat(3, 1fr);` is shorthand for `1 fr 1 fr 1 fr`

`grid-column-start: 1;`
`grid-column-end: 3;` will mean it starts on column 1 and ends on column 3.
Can also be written as `grid-column: 1/3`
or as `grid-column: 1/span 2` will mean it's combination of 2 columns

`grid-template-rows: auto minmax (200px, auto) auto;`
minmax will set minimum and maximum values - where 200px is min and auto is max

## grid-template-areas method

`grid-template-areas: "header header"
`"aside main"`
involves giving`grid-area: x`` where x is name of grid

https://cssgridgarden.com/
https://www.freecodecamp.org/news/css-grid-tutorial-with-cheatsheet/
[[css-grid-poster.pdf]]
https://css-tricks.com/snippets/css/complete-guide-grid/
https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Grids
https://www.w3schools.com/css/css_grid.asp
