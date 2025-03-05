import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import TodoCart from './components/TodoCard'
import "./Style.css"; 
// import './index.css'
// import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    {/* <App /> */}
    <TodoCart></TodoCart>
  </StrictMode>,
)
