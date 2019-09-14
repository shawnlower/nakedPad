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

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmitName = this.handleSubmitName.bind(this);

  }

  componentDidMount() {
    console.log("main editor", this.MainEditor);
    this.PageName.focus()
    this.PageName.select()
  }

  handleChange(event) {
    this.setState({name: event.target.value});
  }

  handleSubmitName(event) {
    event.preventDefault();
    this.MainEditor.focus();
  }

  render() {
    return <div className='Page'>

      <form
        onSubmit={this.handleSubmitName}
      >
        <input
          className='PageName'
          onChange={this.handleChange}
          ref={(me) => this.PageName = me}
          type="text"
          value={ this.state.name }
        />
      </form>
      <Editor
        defaultValue={ this.state.text }
        ref={(editor) => this.MainEditor = editor}
      />
      </div>
  }

}

export default Page;
