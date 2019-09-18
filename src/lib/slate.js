import React from 'react';

export const BLOCK_TAGS = {
  blockquote: 'quote',
  p: 'paragraph',
  pre: 'code',
}

// Add a dictionary of mark tags.
export const MARK_TAGS = {
  em: 'italic',
  strong: 'bold',
  u: 'underline',
}

// eslint-disable-next-line
// export const rules = [ { serialize() { return <p>'hi'</p>}}];

export const rules = [
  { serialize(obj, children) { console.log('init: ', obj.object, obj.type); } },
  {
    serialize(obj, children) {
      if (obj.object === 'inline') {
        switch (obj.type) {
          case 'link':
            const href = obj.data.get('href');
            return <a href={href}>{children}</a>
          default:
            return <p>{children}</p>
        }
      }
    },
  },
  {
    deserialize(el, next) {
      const type = BLOCK_TAGS[el.tagName.toLowerCase()]
      if (type) {
        return {
          object: 'block',
          type: type,
          data: {
            className: el.getAttribute('class'),
          },
          nodes: next(el.childNodes),
        }
      }
    },
    serialize(obj, children) {
      if (obj.object === 'block') {
        switch (obj.type) {
          case 'code':
            return (
              <pre>
                <code>{children}</code>
              </pre>
            )
          case 'paragraph':
            return <p className={obj.data.get('className')}>{children}</p>
          case 'quote':
            return <blockquote>{children}</blockquote>
          default:
            return <p>{children}</p>
        }
      }
    },
  },
    // Add a new rule that handles marks...
  {
    deserialize(el, next) {
      const type = MARK_TAGS[el.tagName.toLowerCase()]
      if (type) {
        return {
          object: 'mark',
          type: type,
          nodes: next(el.childNodes),
        }
      }
    },
    serialize(obj, children) {
      console.log("In serialize", obj.object, children)
      if (obj.object === 'mark') {
        switch (obj.type) {
          case 'bold':
            return <strong>{children}</strong>
          case 'italic':
            return <em>{children}</em>
          case 'underline':
            return <u>{children}</u>
          default:
            console.warn('Unknown mark type: ', obj);
            return {children}
        }
      }
    },
  },
]
