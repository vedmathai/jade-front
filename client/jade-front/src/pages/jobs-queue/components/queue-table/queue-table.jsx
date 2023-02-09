import React, { useState, useEffect } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faFilter } from '@fortawesome/free-solid-svg-icons'

import './queue-table.css'
import '../../../../common/css/table.css';

function QueueTableCell(props){
    var item = props.item;
    return (
        <>
            <td className="table-cell queue-table-cell">
                {item}
            </td>
        </>
    )
}

function QueueTableRow(props){
    const row = props.row;
    const rowi = props.rowi;
    const row_vals = [rowi].concat(Object.values(row));
    const row_div = row_vals.map((row_val, row_val_i) => (
        <QueueTableCell item={row_val}/>
    ))
    return (
        <tr className='table-row queue-table-row'>
            {row_div}
        </tr>
    )
        
}

function QueueTableHeader() {
    var headers = ['Sr. No.', 'Job Id', 'Partition', 'Name',
                   'User', 'Status', 'Time', 'Nodes',
                   'Nodelist(reason)']
    headers = headers.map((header) => {
        return <th className='table-header'>{header}</th>
    })
    return (
        <tr>
            {headers}
        </tr>
    )
}

function PaginationFunctions(props) {

    return (
        <>
            <button
                className="pagination-button"
                onClick={() => props.onClickPreviousPageButton()}
            >&lt;-- Previous
            </button>
            <span className="pagination-page-numbers">
                Page {props.currentPage} / {props.totalPages}
            </span>
            <button
                className="pagination-button"
                onClick={() => props.onClickNextPageButton()}
            >Next --&gt;</button>
        </>
    )
}

function SearchBar(props) {
    return (
        <span>
            <span
                className="table-search-label"
            >
                <FontAwesomeIcon icon={faFilter} />:
            </span>
            <input 
                placeholder='Filter Jade Jobs'
                className="table-search"
                onChange={(e) => props.onChangeSearch(e.target.value)}
            />
        </span>
    )
}

export default function QueueTable(props) {
    var [pageStarti, setPageStarti] = useState(1);
    var [searchTerm, setSearchTerm] = useState('');
    var current_page = 0;
    var total_pages = 0

    var queue = props.jobsQueue;
    var rows = [];
    const page_size = 10;

    var onClickNextPageButton = () => {
        if (current_page !== total_pages) {
            setPageStarti(pageStarti + page_size);
        }
    }

    var onClickPreviousPageButton = () => {
        if (current_page !== 1) {
            setPageStarti(pageStarti - page_size);
        }
    }

    var onChangeSearch = (value) => {
        setSearchTerm(value);
        setPageStarti(0);
    }

    if (queue.job_queue) {

        var page_rows = queue.job_queue.filter((row_item) => {
            if (searchTerm.length == 0) { return true }
            let values = Object.values(row_item);
            for (let i in values) {
                if (values[i].includes(searchTerm)) {
                    return true;
                }
            }
            return false;
        })
        current_page = Math.ceil((pageStarti + 1) / page_size)
        total_pages = Math.ceil(page_rows.length / page_size)
        var rows = page_rows.slice(pageStarti, pageStarti + page_size);
        rows = rows.map((row, rowi) => (
                <QueueTableRow row={row} rowi={rowi + pageStarti} />
        ));
    }
    return (
        <>
            <div className="table-search-container">
                <SearchBar
                    onChangeSearch={onChangeSearch}
                />
            </div>
            <table className='table'>
                <QueueTableHeader/>
                {rows}
            </table>
            <div className="pagination-functions-container">
                <PaginationFunctions
                    onClickNextPageButton={onClickNextPageButton}
                    onClickPreviousPageButton={onClickPreviousPageButton}
                    currentPage={current_page}
                    totalPages={total_pages}
                />
            </div>
        </>
    )
}
