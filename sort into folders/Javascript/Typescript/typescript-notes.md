---
title: Typescript Notes
---

# Typescript

- Has typechecking
- It is a superset of Javascript and can be used anywhere JS is used.
- Requires compilation before use
  - transpilation
- Helps fix bugs for large projects
- Run tsc in the terminal to transpile typescript files to javascript
- tsc uses es5.
- tsc --init to create a tsconfig.json
  - target - can be changed depending on where deploying to.
- tsc --watch to watch for changes
- can set type for an array and have to do this for empty arrays e.g. let numbers: number[] = [];

New built in types:

- any - can be anything. This means you don't get type safety, so best to avoid. Can use it to turn off errors.
- unknown
- never
- enum - used to create a list of values, e.g. enum Direction {North, South, East, West}, where north becomes 0, south becomes 1 etc. It sets automatically. If change first one can change other two automatically. Using with const will generate more optimised js code.
- tuple - An array with fixed length where each element has a type.Often useful for two values, like key value pairs.

Don't always have to specify the variable type, like number etc.

Functions - can annotate them to add type for easy compilation.
e.g. function add(n1: number, n2: number) {
return n1 + n2;
}

Objects - can annotate them to add type for easy compilation.
e.g. const person: {
name: string;
age: number;
} = {
name: 'Max',
age: 30,
};

## Type aliases

Type aliases are used to create custom types.
e.g. type Point = {
x: number;
y: number;
};
can then write const point: Point = {
x: 1,
y: 2,
};
later down the line, and use in multiple pleaces.

## Union Types

Union types are used to return multiple types in different ways.

e.g. function printAge(age: number | string) {
if (typeof age === 'string') {
console.log('Your age is: ' + age);
} else {
console.log('Your age is: ' + age);
}
}

Can use this to make a function that can return either a number or a string as a number, so parseInt etc.

## Intersection Types

Intersection types are used to combine multiple types.

e.g. type Draggable = {
drag: () => void;
};
type Resizable = {
resize: () => void;
};
e.g. type UIWidget = Draggable & Resizable;

## Literal Types

Literal types are used to restrict values to very exact and specific values.

e.g. type Quantity = 50 | 100;
let quantity: Quantity = 100;

## Nullable types

Nullable types are used to make a property optional.

e.g. function printName(name: string | null) {
if (name) {
console.log("Your name is: " + name);
} else {
console.log("No name was provided!");
}
}

Can also pass undefined as an option by changing to string | null | undefined.

printName(null);

## Optional Chaining

Optional chaining is used to make a property optional.
e.g.

const fetchedUserData = {
id: 'u1',
name: 'Max',
job: { title: 'CEO', description: 'My own company' },
};
console.log(fetchedUserData?.job?.title);

This will only fetch data if it exists.

[Roadmap to fill in as learn](https://roadmap.sh/typescript)
