import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css';
import Home from "./Components/Home/Home"
import Login from "./Components/Login/Login"
import Signup from "./Components/Signup/Signup";
import Feedback from "./Components/Feedback/Feeback";
import Rooms from "./Components/Rooms/Rooms";


function App() {


  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} /> 
          <Route path="/register" element={<Signup />} /> 
          <Route path="/feedback" element={<Feedback />}></Route>
          <Route path="/rooms" element={<Rooms />}></Route>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
