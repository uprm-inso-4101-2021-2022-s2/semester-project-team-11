import React from 'react';
import ReactDOM from 'react-dom';
import * as serviceWorker from './serviceWorker';
import './index.css'
import { Route, Routes, BrowserRouter } from 'react-router-dom';
import App from './App.js';
import Header from './components/Header';
import Footer from './components/Footer';

const routing = () => {
  return(
    <React.StrictMode>
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path="/" element={<App />} />
        </Routes>
        <Footer />
      </BrowserRouter>
    </React.StrictMode>
  )
};

ReactDOM.render(routing(), document.getElementById('root'));
serviceWorker.unregister();
