import React from 'react';

import Plain from 'slate-plain-serializer';
import { Editor } from 'slate-react';

import './page.css';

class Page extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: 'Untitled Document',
      text: Plain.deserialize("Initial text"),
    }
  }

  componentDidMount() {
    this.MainEditor.focus();
    console.log(this.MainEditor);
  }

  render() {
    return <div className='Page'>
      <h1>{this.state.name}</h1>
      <Editor
        defaultValue={ this.state.text }
        ref={(editor) => this.MainEditor = editor}
      />
      </div>
  }

}

export default Page;
