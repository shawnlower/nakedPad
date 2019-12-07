import React from 'react';

import './App.css';
import Header from './components/header.js';
import Page from './components/page.js';
import Footer from './components/footer.js';

// Bootstrap
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {

  return (
    <div className='wrapper'>
      <Header />
      <Page />
      <Footer />
    </div>
  );
}

export default App;
