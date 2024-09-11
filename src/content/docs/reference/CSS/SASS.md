---
title: SASS
---

SASS can help write stylesheets that are both readable and maintainable.

`npm install sass`

- either .sass file or .scss (which is more common).

-SCSS

    - superset of css, so you can use all the same rules and syntax.
    - Variables
     - can write dollar sign variables, e.g. $color: red; which can be referenced as `$color` in code.
    - Nesting
       - avoids duplicating class names
       - use &: to nest focus, hover, active etc., e.g.
       ```scss
       .btn {
            &:focus {}
            &:hover {}
            &:active {}
        }
        ```
    - Mixins
        - use @mixin to define reusable blocks of code
        -
        ```scss
        @mixin flex-column {
            display: flex;
            flex-direction: column;
            background: gray;
            }
        .card {
            @include flex-column;
            }
        .aside {
            @include flex-column;
            }
        ```
        - can also add variables with this, like so:
        ```scss
        @mixin flex-column($color) {
            display: flex;
            flex-direction: column;
            background: $color;
            }
        ```
    - Functions
        - can write if else blocks.
            - ```scss
            @function color($color) {
                @if $color == red {
                    @return red;
                } @else {
                    @return black;
                }
            }
            $color: color(red);
            ```
        - can extract into function, like so:
            ```scss
            @function color($color) {
                @if $color == red {
                    @return red;
                } @else {
                    @return black;
                }
            }
            $color: color(red);
            ```
        - can also use `@each` to loop through values, like so:
            ```scss
            @each $color in red, green, blue {
                .item-#{$color} {
                    background: $color;
                }
            }
            ```
        - SASS has some built in functions, like lighten and darken for colours and round for numbers:
            ```scss
            $base-color: green;

            .card {
                background: darken($base-color, 25%);
            }
        - Partials
            - Partials are SASS files that contain snippets of CSS that you can include in other SASS files
            - Partial filenames start with an underscore, e.g. _partial.scss
            - Use @import to include partials in other files
            - Partials help organize and modularize your stylesheets
            - e.g:

              ```scss
                // _colors.scss
                $primary-color: #3498db;
                $secondary-color: #2ecc71;

                // main.scss
                @import 'colors';

                body {
                    background-color: $primary-color;
                }
                ```

### Reference Links:

- [100 second guide](https://www.youtube.com/watch?v=akDIJa0AP5c)
- [SASS docs](https://sass-lang.com/documentation/)
- [Key Concepts](https://sass-lang.com/guide/)
- [Using SASS and Tailwind with PostCSS](https://www.elian.codes/blog/21-04-13-writing-your-own-components-with-tailwind-sass/)
- [SASS Guidelines](https://sass-guidelin.es/)
