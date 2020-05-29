import React from 'react';

import { Button } from 'react-bootstrap'
import { Modal } from 'react-bootstrap'

import { Ltp } from '../services/ltp/ltp.js';

class ItemModal extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      items: [],
      href: "http://default.value/",
      linkText: 'Link',
    }

    // this.handleSave = this.handleSave.bind(this)
  }

  componentDidMount() {
    const ltp = new Ltp();
    console.log(ltp);
    ltp.getItems().then(response => {
      console.log("Loaded items: ", response);
      this.setState({ items: response.items });
    });
  }

  componentWillUnmount() {
    console.log("Unmounting...");
  }

  handleSave() {
    // If we don't already have some text selected, use the value from the text box
    return;
    if (!this.props.value.selection.isExpanded) {
      const text = this.state.linkText || 'Link';
      this.props.editor.insertText(text);
      this.props.editor.moveStartBackward(text.length);
    }
    this.props.editor.wrapInline({
      type: 'link',
      data: { href: this.state.href },
    });
    this.props.updateValue(this.props.editor.value);
    this.props.handleClose();
  }

  render() {
    return (
      <>
        <Modal show={this.props.show} animation={false}>
          <Modal.Header closeButton>
            <Modal.Title>Insert Link</Modal.Title>
          </Modal.Header>
          <Modal.Body>
          { this.props.value.selection.isExpanded || (
          <div>
            <span>Link Text</span>
            <input
              type="text"
              value={ this.state.linkText }
              onChange={ event => this.setState({linkText: event.target.value}) }
            />
          </div>
          ) }
          <div>
            <span>Target URL</span>
            <input
              type="text"
              value={ this.state.href }
              onChange={ event => this.setState({href: event.target.value}) }
            />
          </div>

          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={ this.props.handleClose }>
              Cancel
            </Button>
            <Button variant="primary" onClick={ () => { this.handleSave(); this.props.handleClose() } }>
              Save Changes
            </Button>
          </Modal.Footer>
        </Modal>
      </>
    )
  }
}

export default ItemModal
