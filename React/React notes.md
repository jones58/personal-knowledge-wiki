uses .jsx, a version of javascript
lets you write html within js and javascript, within { }, e.g. 
``{'this is treated as JavaScript code' }

must be compiled into javascript with a transpiler like Babel

React is called Electron on desktop and React native on mobile. For web - react.js or just react. 

## components
each component has to be children nested in parent element, not just children. e.g. put paragraphs in a div. 

two ways to create component : 

1. functional stateless, using function, e.g. 
```jsx
const DemoComponent = function() {
  return (
    <div className='customClass' />
  );
};
```
n.b. functions have to start with capital letter - i.e. DemoComponent here
This lets us make complicated layouts with lots of different components. 

2. using es6 (javascript) class syntax 
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

It uses `super()` to call the constructor of the parent class, in this case `React.Component`. 



can compose components together by giving custom named parent HTML tag, e.g. in render you can write
```jsx
return (
 <App>
  <Navbar />
  <Dashboard />
  <Footer />
 </App>
```


You can render class components within other elements in the same way. E.g. just nest ``<className></className>``

## comments 
comments, e.g.: 

```jsx
```{/*here's a comment*/}
```

## adding to DOM 

to add to DOM, use React's rendering API: 
`ReactDOM.render(componentToRender, targetNode)`

where variables are componentToRender - ie. component from .jsx and targetNode, the element we want to send the component to.  Can use document.getElementByID to select this target element. 

for React components (as opposed to JSX) - you have to use the ``<component></component>``  or ``<component/>``  syntax - for both class components and functional components

## classes 

Use `className` to set classes within jsx and also use camelCase for naming stuff 

## tags 

all tags have to be closed .  all elements can be self closing too, such as `<div>`, can be written as `<div />` or `<div></div>`.

## Props and state 

props - short for properties
state - local variable just within given component


## React Bootstrap 
Predesigned components in HTML, CSS and Javascript





# Links 

Completed this: https://www.skillshare.com/en/classes/Learn-React-From-Beginner-Concepts-to-Building-a-Full-React-App/196289883/reviews