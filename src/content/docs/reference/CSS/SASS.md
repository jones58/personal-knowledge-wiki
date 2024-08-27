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
        - can write if else blocks.

### Reference Links:

- [100 second guide](https://www.youtube.com/watch?v=akDIJa0AP5c)
- [SASS docs](https://sass-lang.com/documentation/)
- [Key Concepts](https://sass-lang.com/guide/)
