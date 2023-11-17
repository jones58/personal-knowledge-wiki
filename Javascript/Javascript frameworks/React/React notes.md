# React notes

Uses .jsx, a version of javascript
lets you write html within js and javascript, within { }, e.g.
``{'this is treated as JavaScript code' }

Must be compiled into javascript with a transpiler like Babel.

React is called Electron on desktop and React native on mobile. For web - react.js or just react.

## Building a React App

### Common Build tools

- Create React App
  - `npx create-react-app` creates react app and bundles it with webpack automatically.
  - html element will just have a root div, linked to index.js which tells what to feed in and app.js which has all the html in.
  - `npm start` will run live server with React app.
  - `npm run build` will crerate a build folder which can be uploaded to server.
- Vite

  - `npm init vite my-app`
  - Simplifies and speeds up build process.
  - works for most developers and with multiple frameworks.
  - can add plugins
  - `npm run dev` to run locally.
  - Makes typescript faster.
  - modifying source code will make changes instantly, unlike create react app.
  - `npm run build` to generate build version

- Next.js
- Gatsby

### Files in a typical React app

- `package.json` - dependencies and settings.
- `node_modules` - source code for node dependencies. git ignore and don't touch.
- `public` - where static files are stored
- `src/index.js` -main entrypoint to start app
- `src/App.js` - root component of app.
- `src/App.spec.js` - unit tests for app, to show if app working correctly.
- `src/*.css` - css styling for app.

## Components

- Use React Developer tools extension to see React components in dev tools

- each component has to be children nested in parent element, not just children. e.g. put paragraphs in a div.

N.b need parentheses around multi line jsx:
e.g.

const myElement = ```jsx
<a href="https://www.example.com">

  <h1>Click me!</h1>
</a>
```

## Two ways to create component

### 1. Functional components

```jsx
const DemoComponent = function () {
  return <div className="customClass" />;
};
```

```jsx
const MyComponent2 = () => {
return ‹p›hi</p›;
｝
```

n.b. functions have to start with capital letter - i.e. DemoComponent here

- This lets us make complicated layouts with lots of different components.
- This is most popular method of making components, more popular than below method.

If you want a React component within another function componentn, you define define component and render it as html element within other component's body:

e.g.

```JSX
function App() {
  return <Headline />;
}

function Headline() {
  const greeting = 'Hello Function Component!';

  return <h1>{greeting}</h1>;
}
```

NB can't write class in jsx - have to write className because class is a reserved word in js.

### 2. Class components

- This isn't really used anymore - much easier to define with a function.

```jsx
class Kitten extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <h1>Hi</h1>
    );
```

- It uses `super()` to call the constructor of the parent class, in this case `React.Component`.

- can compose components together by giving custom named parent HTML tag, e.g. in render you can write

```jsx
return (
  <App>
    <Navbar />
    <Dashboard />
    <Footer />
  </App>
);
```

- You can render class components within other elements in the same way. E.g. just nest `<className></className>`

## Props

props - short for properties

Use props to pass data from parent element.

can be string, number, object, or another react component.

Similar to using a global variable in javascript.

put in curly brackets so don't need . notation.

Props are useful because of virtual dom and react fibre engine, which allow it to re-render props when they change.

props go from parent to child.

{props.children} gives inner html of parent component

props passed to class component are available as: `this.props`

## State

- Local variable just within given component
- State is any data that changes over time. Used to update UI when data changes.
- You declare state by setting in the constructor
- State property is an object.
- Declare like this:

```jsx
this.state = {};
```

- can also access with `this.state`
- accessing state in return method means you have to use curly braces {}
- Use setState to change state, e.g.

```jsx
this.setState({
  username: "Lewis",
});
```

- setState takes an object as an argument, which will be merged with the current state

We can also use useState to set state in functional components.

e.g.

```jsx
function App() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  );
```

## Lifecycle and events

mount, update, unmount from component tree

e.g. in class component:

```jsx
class Lifecycle extends React.Component {
  componentDidMount() {
    // Initialize
  }

  componentDidUpdate() {
    // Updated
  }

  componentWillUnmount() {
    // Removed
  }
}
```

You can't do this in functional components, instead you can use `useEffect`:

```jsx
function Lifecycle() {
  useEffect();
}
```

takes function as an argument, then array of dependencies then another function when destroyed, e.g.

```jsx
const [count] = useState(0);

useEffect(() => {

    console.log('count updated!')

    return () => console.log('destroyed!')

}, [count]);

}
```

## Context

- Context is a way to pass data through the component tree without having to pass props down manually at every level.
- Happens on API level with a function called `createContext`.
- e.g. :

```jsx
const ThemeContext = createContext();
```

- use with `useContext`

```jsx
function PropDrilling() {
  const [count] = useState(0);

  return (
    <CountContext.Provider value={count}>
      <Child />
    </CountContext.Provider>
  );
}

function Child() {
  return <GrandChild />;
}

function GrandChild() {
  const count = useContext(CountContext);

  return <div>{count}</div>;
}
```

## Error Boundaries

Not often required but can be useful for debugging and making sure everything is working correctly.

## React Query

- used to fetch data
- e.g. :

```jsx
import { useQuery } from "react-query";
```

## Hooks

React Hooks mean we can have state in Function component.

Watch this: <https://www.youtube.com/watch?v=f687hBjwFcM>

## Comments in jsx

````jsx
```{/*here's a comment*/}
````

## adding to DOM

to add to DOM, use React's rendering API:
`ReactDOM.render(componentToRender, targetNode)`

where variables are componentToRender - ie. component from .jsx and targetNode, the element we want to send the component to. Can use document.getElementByID to select this target element.

for React components (as opposed to JSX) - you have to use the `<component></component>` or `<component/>` syntax - for both class components and functional components

## Tags

all tags have to be closed . all elements can be self closing too, such as `<div>`, can be written as `<div />` or `<div></div>`.

## Conditional rendering

Very common, based on boolean.

You can't write if else statements in JSX. Instead, use:

1.  Outside JSX, in javascript curly brackets e.g.

```jsx
/** Write "Hello" if x is less than 10, otherwise "Goodbye" **/
const x = 5;
let text = "Goodbye";
if (x < 10) {
  text = "Hello";
}
const myElement = <h1>{text}</h1>;
```

Here the javascript runs before the JSX code.

2.  Using Ternary expressions:

```jsx
/** Write "Hello" if x is less than 10, otherwise "Goodbye" **/

const x = 5;
const myElement = <h1>{x < 10 ? "Hello" : "Goodbye"}</h1>;
```

Great when you have two conditions to choose between

3. Logical And

```jsx
/** Write "Hello" if x is less than 10, otherwise "Goodbye" **/
const x = 5;
const myElement = (
  <h1>
    {x < 10 && "Hello"}
    {x >= 10 && "Goodbye"}
  </h1>
);
```

```jsx
{count && 2 === 0 ? <h1>Count is even</h1> }
```

## Loops

Most common way to loop in React is with array map:

```jsx
const data = [
  { id: 1, name: "Fido 🐕" },
  { id: 2, name: "Snowball 🐈" },
  { id: 3, name: "Murph 🐈‍⬛" },
  { id: 4, name: "Zelda 🐈" },
];

function ListOfAnimals() {
  return (
    <ul>
      {data && // Only render if there's data - see 'Conditional Rendering'
        data.map(({ id, name }) => {
          return <li key={id}>{name}</li>;
        })}
    </ul>
  );
}
```

Here the key attribute gives each element a unique identifier so React can keep track of it in case the name value changes.

## Events

Usually use getElementById and event listener in vanilla js, but in React we use event handlers.

```jsx
<button onClick={handleClick}>Click me</button>
```

We can then define the handleClick function and pass it to the onClick attribute.

```jsx
function handleClick() {
  alert("hello");
}
```

We could also do this all in the onClick attribute:

```jsx
return <button onClick={(event) => alert("hello")}> Click </button>;
```

can pass a function as a prop from parent to child too.

## React Bootstrap

Predesigned components in HTML, CSS and Javascript

## Resources

- <https://www.skillshare.com/en/classes/Learn-React-From-Beginner-Concepts-to-Building-a-Full-React-App/196289883/reviews>
- <https://fireship.io/courses/react/>
- <https://react.dev/learn/writing-markup-with-jsx>
- [Vite guide](https://vitejs.dev/guide/)

To read more:

- [Hooks](https://reactjs.org/docs/hooks-intro.html)
- https://www.robinwieruch.de/react-function-component/
- https://react.dev/reference/react/Component
- https://react.dev/learn/passing-props-to-a-component
- https://www.freecodecamp.org/news/jsx-in-react-introduction/

```

```

```

```

```

```

```

```
