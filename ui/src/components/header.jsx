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
        <ul>
          <li>Time: { this.state.date.toLocaleTimeString() }</li>
          <li>Doc ID: {this.state.doc_id}</li>
        </ul>
      </div>
    </div>
  }
}

export default Header;
