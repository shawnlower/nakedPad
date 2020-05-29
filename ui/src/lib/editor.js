import React from 'react';

import { createEditor } from 'slate';
import { Slate, withReact, Editable } from 'slate-react';

// import Table from '../components/Table';

const initialState = {
    value: [
        {
            type: 'paragraph',
            children: [
                { text: 'Enter some text' },
                {
                    type: 'link',
                    url: 'http://www.mozilla.org/',
                    children: [
                        { text: 'Enter some text' },
                    ],
                },
            ]
        },
        {
            type: 'table',
            children: [
                {
                    type: 'table-row',
                    children: [
                        { type: 'table-cell', children: [{ text: "Column 1" }] },
                        { type: 'table-cell', children: [{ text: "Column 2" }] },
                        { type: 'table-cell', children: [{ text: "Column 3" }] },
                    ]
                },
                {
                    type: 'table-row',
                    children: [
                        { type: 'table-cell', children: [{ text: "R2 Column 1" }] },
                        { type: 'table-cell', children: [{ text: "R2 Column 2" }] },
                        { type: 'table-cell', children: [{ text: "R2 Column 3" }] },
                    ]
                },
            ]
        }
    ],
}

export class NPEditor extends React.Component {

    // editor = useMemo(() => withReact(createEditor()), [])

    constructor(props) {
        super(props);
        this.state = initialState;
        this.editor = withReact(createEditor());
    }

    // const[value, setValue] = useState(initialValue);
    updateEditor(value) {
        console.log('updateEditor VALUE', value)
        console.log('updateEditor STATE', this.state)
        this.setState({ value })
    }

    // renderElement = useCallback(({ attributes, children, element }) => {
    renderElement = ({ attributes, children, element }) => {
        switch (element.type) {
            case 'quote':
                return <blockquote {...attributes}>{children}</blockquote>
            case 'link':
                return (
                    <a {...attributes} href={element.url}>
                        {children}
                    </a>
                )
            case 'table':
                return (
                    <table>
                        <tbody {...attributes}>{children}</tbody>
                    </table>
                )
            case 'table-row':
                return (
                    <tr {...attributes}>{children}</tr>
                )
            case 'table-cell':
                return (
                    <td {...attributes}>{children}</td>
                )

            default:
                return <p {...attributes}>{children}</p>
        }
    }


    render() {
        return (
            <Slate
                editor={this.editor}
                value={this.state.value}
                onChange={value => this.updateEditor(value)}
            >
                <Editable renderElement={this.renderElement} />
            </Slate>
        )
    }
}