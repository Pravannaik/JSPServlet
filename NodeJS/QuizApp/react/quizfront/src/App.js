import React, {useState} from 'react';
import './App.css';
import {BrowserRouter, Link, Switch, Route} from 'react-router-dom'
import QuizApp from './components/QuizApp'
import axios from 'axios';

function App() {

  return (
    <>
      <BrowserRouter>
        <div>
          <div className="header">
            <img src="./logo.png" className="ImgHeader" alt="myPic" />
          </div>
          <Switch>
            <Route exact path="/" component={Welcome}/>
            <Route path="/details" component={Details}/>
            <Route path="/instructions" component={Instructions}/>
            <Route path="/quiz" component={QuizApp}/>
          </Switch>
        </div>
      </BrowserRouter>
    </>
  );
}

const Welcome = () => {
  return (
    <>
      <div className="WelcomeApp">
            <div className="bodySec">
              <h1>WELCOME</h1>
              <h3>TO THE</h3>
              <h1>QuizzoW</h1>
            </div>
            <div>
              <Link to="/details"><button className="WelcomeButton">Get Started</button></Link>
            </div>
          </div>
    </>
  )
}

const Details = () => {

  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState(""); 
  const [email, setEmail] = useState("");

  const submitData = () => {
    axios.post('http://localhost:3001/data', {firstName : firstName, lastName : lastName, email : email}).then(() => {
      alert("Successfully Insert")
    })
  }

  return (
    <>
      <div className="DetailApp">
         <div className="DetailHeader">
            Enter Your Personal Details
         </div>
         <div className="DetailBody">
            <label>First Name</label>
            <input type="text" name="firstName" onChange={(val) => {setFirstName(val.target.value)}}/>
            <label>Last Name</label>
            <input type="text" name="lastName" onChange={(val) => {setLastName(val.target.value)}}/>
            <label>Email</label>
            <input type="text" name="email" onChange={(val) => {setEmail(val.target.value)}}/>
         </div>
          <div>
            <Link to="/instructions"><button onClick={submitData} className="DetailsButton">Submit</button></Link>
          </div>
      </div>
    </>
  )
}


const Instructions = () => {
  return (
    <>
      <div className="InstApp">
        <div className="InstHeader">
          Instructions
        </div>
        <div className="InstBody">
          <ol>
            <li>Questions are of Multiple Choice.</li>
            <li>There are total 10 Questions.</li>
            <li>Each Questions carries one mark.</li>
            <li>No Negative marking for Wrong Answers</li>
            <li>Minimum 4 points required to pass the Quiz.</li>
            <li>There is a timer for a Quiz.</li>
            <li>For each Question you get 10 seconds.</li>
            <li>The time will start the moment you click the Start Test button.</li>
          </ol>
        </div>
          <div>
            <Link to="/quiz"><button className="InstButton">Start Test</button></Link>
          </div>
      </div>
    </>
  )
}

export default App;
