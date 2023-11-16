import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {

  const [animals, setAnimals] = useState([])


return (
  <main>
      <div className ="App">
        <h1>Animal Farm app </h1>
        <input
        type="text"
        placeholder="search"
        onChange = {(e) => console.log(e.target.value)}
        />
          <ul>
          {animals.map((animal) => (
          <Animal key={animal.id} {...animal} />
        ))}
        {animals.length === 0 && 'No animals found'}
        </ul>




      </div>
      </main>
  )
}

function Animal ({type, name, age}){
  return (
    <li>
      <strong>{type}</strong>{name}({age} years old)
    </li>
  )
}

export default App
