# React notes

uses .jsx, a version of javascript
lets you write html within js and javascript, within { }, e.g.
``{'this is treated as JavaScript code' }

must be compiled into javascript with a transpiler like Babel

React is called Electron on desktop and React native on mobile. For web - react.js or just react.

## Building a React App

### Common Build tools

- Create React App
    - ``npx create-react-app`` creates react app and bundles it with webpack automatically.
    - html element will just have a root div, linked to index.js which tells what to feed in and app.js which has all the html in.
    - ``npm start`` will run live server with React app.
    - ``npm run build`` will crerate a build folder which can be uploaded to server.
- Vite
- Next.js
- Gatsby

### Files in a typical React app

- ``package.json`` - dependencies and settings.
- ``node_modules`` - source code for node dependencies. git ignore and don't touch.
- ``public`` - where static files are stored
- ``src/index.js`` -main entrypoint to start app
- ``src/App.js`` - root component of app.
- ``src/App.spec.js`` - unit tests for app, to show if app working correctly.
- ``src/*.css`` - css styling for app.

## Components

- Use React Developer tools extension to see React components in dev tools

- each component has to be children nested in parent element, not just children. e.g. put paragraphs in a div.

## Two ways to create component

### 1.  Functional components

```jsx
const DemoComponent = function() {
  return (
    <div className='customClass' />
  );
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
```

- You can render class components within other elements in the same way. E.g. just nest ``<className></className>``

## Props

props - short for properties

Use props to pass data from parent element.

can be string, number, object, or another react component.

Similar to using a global variable in javascript.

put in curly brackets so don't need . notation.

Props are useful because of virtual dom and react fibre engine, which allow it to re-render props when they change.

props go from parent to child.

{props.children} gives inner html of parent component

## State

- Local variable just within given component

## Comments in jsx

```jsx
```{/*here's a comment*/}
```

## adding to DOM

to add to DOM, use React's rendering API:
`ReactDOM.render(componentToRender, targetNode)`

where variables are componentToRender - ie. component from .jsx and targetNode, the element we want to send the component to.  Can use document.getElementByID to select this target element.

for React components (as opposed to JSX) - you have to use the ``<component></component>``  or ``<component/>``  syntax - for both class components and functional components

## Tags

all tags have to be closed .  all elements can be self closing too, such as `<div>`, can be written as `<div />` or `<div></div>`.

## React Bootstrap

Predesigned components in HTML, CSS and Javascript

## Hooks

Watch this:  <https://www.youtube.com/watch?v=f687hBjwFcM>

# Fill in [Roadmap](https://roadmap.sh/react) as go along

## Resources

- <https://www.skillshare.com/en/classes/Learn-React-From-Beginner-Concepts-to-Building-a-Full-React-App/196289883/reviews>
- <https://fireship.io/courses/react/>
