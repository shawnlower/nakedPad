import React from 'react';

import * as s from './App.css';
import Header from './components/header.jsx';
import Page from './components/page.js';
import Footer from './components/footer.jsx';

// Bootstrap
import * as bootstrap from 'bootstrap/dist/css/bootstrap.min.css';

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
