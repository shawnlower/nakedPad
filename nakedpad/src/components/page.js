import React from 'react';

import Plain from 'slate-plain-serializer';
import { Editor } from 'slate-react';
import Keymap from "@convertkit/slate-keymap"

import './page.css';

class Page extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: 'Untitled Document',
      value: Plain.deserialize("Initial Value"),
    }

    this.plugins = [
      Keymap({
          "mod+x": (event, editor) => editor.toggleMark("bold"),
          "mod+i": (event, editor) => editor.toggleMark("italic"),
          "mod+u": (event, editor) => editor.toggleMark("underline"),
          "mod+k": (event, editor) => this.createLink(event, editor),
      })
    ]

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

  createLink(event, editor) {
    event.preventDefault();
    console.log(`Creating link from ${this.state.value.fragment.text}`, event, editor);
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
        onChange={this.onChange}
        plugins = {this.plugins}
        ref={(editor) => this.MainEditor = editor}
        value={ this.state.value }
      />
      </div>
  }
}

export default Page;
