import React from 'react';

import Plain from 'slate-plain-serializer';
import { Editor } from 'slate-react';

import './page.css';

class Page extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: 'Untitled Document',
      value: Plain.deserialize("Initial Value"),
    }

    this.onChange = this.onChange.bind(this);
    this.handleSubmitName = this.handleSubmitName.bind(this);
  }

  componentDidMount() {
    console.log("main editor", this.MainEditor);
    this.PageName.focus()
    this.PageName.select()
  }

  onChange({ value }) {
    console.log(value)
    this.setState({ value });
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
          onChange={ event => this.setState({name: event.target.value}) }
          ref={(me) => this.PageName = me}
          type="text"
          value={ this.state.name }
        />
      </form>
      <Editor
        value={ this.state.value }
        onChange={this.onChange}
        ref={(editor) => this.MainEditor = editor}
      />
      </div>
  }

}

export default Page;
