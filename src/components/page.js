import React from 'react';

import { Editor } from 'slate-react';
import Html from 'slate-html-serializer'
import Keymap from "@convertkit/slate-keymap"
import Plain from 'slate-plain-serializer';

import ItemModal from './ItemModal.js';
import './page.css';
import { rules } from '../lib/slate.js';
import { RenderPlugin } from '../lib/render.js';

class Page extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: 'Untitled Document',
      value: Plain.deserialize("Initial Value"),
      showItemModal: false,
    }

      this.html = new Html({ rules });

    this.onChange = this.onChange.bind(this);
    this.handleSave = this.handleSave.bind(this);
    this.handleSubmitName = this.handleSubmitName.bind(this);
  }

  componentDidMount() {
    this.PageName.focus()
    this.PageName.select()
    this.plugins = [
      Keymap({
        "mod+b": (event, editor) => { this.editor.toggleMark("bold"); event.preventDefault() },
        "mod+i": (event, editor) => { this.editor.toggleMark("italic"); event.preventDefault() },
        "mod+u": (event, editor) => { this.editor.toggleMark("underline"); event.preventDefault() },
        "mod+k": (event, editor) => this.createLink(event, editor),
      }),
      // Rendering Plugin
      RenderPlugin()
    ]
  }

  onChange({ value }) {
    console.log('onChange', value)
    this.setState({ value });
  }

  handleSubmitName(event) {
    event.preventDefault();
    this.editor.focus();
  }

  createLink(event, editor) {
    event.preventDefault();
    console.log(`Creating link from ${this.state.value.fragment.text}`, event, this.state.value.fragment, editor);
    if (this.state.value.selection.isExpanded) {
      const href = window.prompt('Enter the URL of the link:');
      this.editor.wrapInline({
        type: 'link',
        data: { href: href },
      });
      // this.setState({showItemModal: true});
    }
  }

  handleSave(event) {
    const doc = this.html.serialize(this.state.value);
    console.log(this.state.value.document, doc);
  }


  render() {
    return (
      <div className='Page'>
        <ItemModal
          item={this.state.value.fragment.text}
          show={this.state.showItemModal}
          handleClose={() => this.setState({showItemModal:false})}
        />
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
        <button onClick={this.handleSave}>Save</button>
        <Editor
          onChange={this.onChange}
          plugins = {this.plugins}
          ref={(editor) => this.editor = editor}
          value={ this.state.value }
        />
      </div>
    )
  }
}


export default Page;
