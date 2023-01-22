import logo from './logo.svg';
import './App.css';
import {BrowserRouter, Routes, Route, Link} from 'react-router-dom'
import Dashboard from './components/Dashboard';
import Main from './components/Main';
function App() {
  return (
    <>
    <BrowserRouter>
    <Routes>
      <Route path='' element={<Dashboard/>}/>
    </Routes>
    <Routes>
      <Route path='/main' element={<Main/>}/>
    </Routes>
    </BrowserRouter>
    </>
  );
}

export default App;
