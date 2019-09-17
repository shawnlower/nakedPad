import React from 'react';

import { Button } from 'react-bootstrap'
import { Modal } from 'react-bootstrap'


class ItemModal extends React.Component {
  componentDidMount() {
    console.log("I've been mounted");
  }

  componentDidUnmount() {
    console.log("I've been Unmmounted");
  }

  render() {
    return (
      <>
        <Modal show={this.props.show} onHide={this.props.handleClose} animation={false}>
          <Modal.Header closeButton>
            <Modal.Title>Modal heading</Modal.Title>
          </Modal.Header>
          <Modal.Body>
          Received: {this.props.item}

          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={this.props.handleClose}>
              Close
            </Button>
            <Button variant="primary" onClick={this.props.handleClose}>
              Save Changes
            </Button>
          </Modal.Footer>
        </Modal>
      </>
    )
  }
}

export default ItemModal
