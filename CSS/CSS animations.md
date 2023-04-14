The `@keyframes` at-rule is used to define the flow of a CSS animation. Within the `@keyframes` rule, you can create selectors for specific points in the animation sequence, such as `0%` or `25%`, or use `from` and `to` to define the start and end of the sequence.

The `animation-name` property links `@keyframes` rule to a CSS selector/element - e.g. a ``heading``.

The `animation-duration` property sets how long an animation should take to complete. either in `s` or `ms`

The `animation-iteration-count` property is used to show how many times an animation should run, either a numnber or set to ``infinite``. 

The `animation-timing-function` property is used to set rate at which animation should run. Usually ``linear`` but there are other options too, like ``ease-in-out``

Can also use ``animation`` property to set these all at once: the `animation-name`, `animation-duration`, `animation-timing-function`, and `animation-iteration-count` properties in that order.

There are also transitions, for example with :active selectors, can set the following values in a similar way. Doesn't use keyframes at rule. 
e.g. 
``transition-duration: 1s;``
``transition-timing-function:ease-in-out;``
``transition-delay: 0ms;``
