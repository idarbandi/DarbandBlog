import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { BrowserRouter as Router, Route, Routes as Switch } from 'react-router-dom';
import Header from './components/header';
import Footer from './components/footer';
import SignUp from './components/register';
import LogIn from './components/login';
import LogOut from './components/logout';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Router>
    <React.StrictMode>
    <Header/>
      <Switch>
        <Route exact path="/" element={<App/>} />
        <Route path="/register" component={<SignUp/>} />
        <Route path="/login" element={<LogIn />} />
        <Route path="/logout" element={<LogOut />} />
      </Switch>
    <Footer/>
    </React.StrictMode>
  </Router>
);
