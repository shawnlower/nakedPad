// Rendering plugin
//

import React from 'react';

export function RenderPlugin() {
  return {
    renderBlock (props, editor, next) {
      // console.log('renderBlock called for', props.node.type);
      switch (props.node.type) {
        case 'code':
          return (
            <pre {...props.attributes}>
            <code>{props.children}</code>
            </pre>
          )
        case 'paragraph':
            return (
              <p {...props.attributes} className={props.node.data.get('className')}>
              {props.children}
              </p>
            )
        case 'quote':
            return <blockquote {...props.attributes}>{props.children}</blockquote>
        default:
            return next()
      }
    },

    // Add a `renderMark` method to render marks.
    renderMark(props, editor, next) {
      // console.log('renderMark called for', props.mark.type);
      const { mark, attributes } = props
        switch (mark.type) {
          case 'bold':
            return <strong {...attributes}>{props.children}</strong>
          case 'italic':
            return <em {...attributes}>{props.children}</em>
          case 'underline':
            return <u {...attributes}>{props.children}</u>
          default:
            return next()
        }
    },

    renderInline(props, editor, next) {
      const { attributes, children, node } = props

      switch (node.type) {
        case 'link': {
          const { data } = node
          const href = data.get('href')
          return (
            <a {...attributes} href={href}>
              {children}
            </a>
          )
        }

        default: {
          return next()
        }
      }
    }
  }
}

export default RenderPlugin
