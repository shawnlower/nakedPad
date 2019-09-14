import React from 'react';

import './header.css';

class Header extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      date: new Date(),
      numUpdates: 0,
    }
  }

  render() {
    return <div className='Header'>
      <div><h1>Editor</h1></div>
      <div>
        <span>Time: { this.state.date.toLocaleTimeString() }</span>
      </div>
    </div>
  }
}

export default Header;
