import React from 'react';
import { createRoot } from 'react-dom/client';
import * as serviceWorker from './serviceWorker';
import './index.css'
import { Route, Routes, BrowserRouter } from 'react-router-dom';
import App from './App.js';
import Header from './components/header';
import Footer from './components/footer';
import Register from './components/register';
import Login from './components/login';
import Logout from './components/logout';

// Adding StrictMode causes data to  be sent twice ???

const routing = () => {
  return(
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
          <Route path="/logout" element={<Logout />} />
        </Routes>
        <Footer />
      </BrowserRouter>
  )
};

const container = document.getElementById('root');
const root = createRoot(container);
root.render(routing());
serviceWorker.unregister();
