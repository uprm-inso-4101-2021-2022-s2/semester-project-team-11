import React from 'react';
import { createRoot } from 'react-dom/client';
import * as serviceWorker from './serviceWorker';
import './index.css'
import { Route, Routes, BrowserRouter } from 'react-router-dom';
import App from './App.js';
import Header from './components/Header';
import Footer from './components/Footer';

// Adding StrictMode causes data to  be sent twice ???

const routing = () => {
  return(
      <BrowserRouter>
        <Header />
        <Routes>
          <Route path="/" element={<App />} />
        </Routes>
        <Footer />
      </BrowserRouter>
  )
};

const container = document.getElementById('root');
const root = createRoot(container);
root.render(routing());
serviceWorker.unregister();
