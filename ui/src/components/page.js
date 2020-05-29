import React from 'react';
// import escapeHtml from 'escape-html';

// import Keymap from "@convertkit/slate-keymap"

// import ItemModal from './ItemModal.js';
import './page.css';
// import { rules } from '../lib/slate.js';
// import { RenderPlugin } from '../lib/render.js';

import { NakedPadApi } from '../services/nakedpad_api/nakedpad_api.js';
import { NPEditor } from '../lib/editor'

class Page extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
        name: 'Untitled Document',
        doc_id: null,
        showItemModal: false,
        value: [{
          type: 'paragraph',
          children: [{ text: 'A line of text in a paragraph.' }],
        }],
    }

    this.api = new NakedPadApi();

    this.onChange = this.onChange.bind(this);
    this.updateValue = this.updateValue.bind(this);
    this.handleSave = this.handleSave.bind(this);
    this.handleSubmitName = this.handleSubmitName.bind(this);

  }

  componentDidMount() {
    this.PageName.focus()
    this.PageName.select()
    this.plugins = [
      // Keymap({
      //   "mod+b": (event, editor) => { this.editor.toggleMark("bold"); event.preventDefault() },
      //   "mod+i": (event, editor) => { this.editor.toggleMark("italic"); event.preventDefault() },
      //   "mod+u": (event, editor) => { this.editor.toggleMark("underline"); event.preventDefault() },
      //   "mod+k": (event, editor) => this.showItemModal(event, editor),
      //   "mod+o": (event, editor) => { this.showLoadModal(event, editor); event.preventDefault() },
      // }),
      // Rendering Plugin
      // RenderPlugin()
    ]
  }

  onChange({ value }) {
    // Called whenever the editor changes (selection, text, etc)
    this.setState({ value });
  }

  handleSubmitName(event, target) {
    // Called when the 'name' form is submitted; i.e. by pressing enter, or focusing out
    console.log('handleSubmitName', event, target)
    event.preventDefault();
    if (this.editor) {
      this.editor.focus();
    } else {
      console.warn("No editor to focus!", this)
    }
  }

  updateValue(value) {
    // Update the document value
    this.setState({ value: value });
  }

  showItemModal(event, editor) {
    event.preventDefault();
    console.log(`Creating link from ${this.state.value.fragment.text}`, event, this.state.value.fragment, editor);
    this.setState({showItemModal: true});
  }

  showLoadModal(event, editor) {
    event.preventDefault();
    console.log(`Load Modal: not implemented.`);
  }

  handleSave(event) {
    const doc = this.html.serialize(this.state.value);
    console.log('handleSave: ', this.state.value.document, doc);

    console.log(this.api);
    this.api.save(this.state.doc_id,
                  this.state.name,
                  doc).then(doc_id => {
      // Update the document ID
      if (doc_id !== this.state.doc_id) {
        this.setState({doc_id: doc_id});
        console.log(`Updated Document ID to ${doc_id}`);
      }
    });
    
  }


  render() {
    return (
      <div className='Page'>
        {/* <ItemModal
          text={"this.state.value.fragment.text"}
          show={this.state.showItemModal}
          editor={this.editor}
          value={this.state.value}
          handleClose={ () => this.setState( { showItemModal: false }) }
          updateValue={this.updateValue}
          href={ this.state.href }
        /> */}
        <form
          onSubmit={this.handleSubmitName}
          onBlur={this.handleSubmitName}
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
        <NPEditor />
      </div>
    )
  }
}

export default Page;
