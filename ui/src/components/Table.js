import React from 'react';

const Table = ({ attributes, children, element }) => {
    console.log('Creating table from element', element)
    switch(element.type) {
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
            return (
                <p {...attributes}>{children}</p> 
            )
    }
}

export default Table