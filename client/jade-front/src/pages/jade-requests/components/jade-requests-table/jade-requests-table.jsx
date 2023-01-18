import React, { useState, useEffect } from 'react'
import './jade-requests-table.css'

function JadeRequestsTableCell(props){
    var item = props.item;
    return (
        <>
            <td className="jade-requests-table-cell">
                {item}
            </td>
        </>
    )
}

function JadeRequestsTableRow(props){
    const row = props.row;
    console.log(row);
    const rowi = props.rowi;
    const keys = ['job_id', 'name', 'partition']
    const vals = keys.map((key) => {
        return row[key]
    })
    const row_vals = [rowi].concat(vals);
    const row_div = row_vals.map((row_val, row_val_i) => (
        <JadeRequestsTableCell item={row_val}/>
    ))
    return (
        <tr>
            {row_div}
        </tr>
    )
        
}

function JadeRequestsHeader() {
    var headers = ['Sr. No.', 'Job Id', 'Name', 'Partition']
    headers = headers.map((header) => {
        return <th>{header}</th>
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
                onClick={() => props.onClickPreviousPageButton()}
            >Previous
            </button>
            Page {props.currentPage} / {props.totalPages}
            <button
                onClick={() => props.onClickNextPageButton()}
            >Next</button>
        </>
    )
}

function SearchBar(props) {
    return (
        <input
            onChange={(e) => props.onChangeSearch(e.target.value)}
        />
    )
}

export default function JadeRequestsTable(props) {
    var [pageStarti, setPageStarti] = useState(0);
    var [searchTerm, setSearchTerm] = useState('');
    var current_page = 0;
    var total_pages = 0

    var requests_list = props.jadeRequestsList;
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

    if (requests_list) {

        var page_rows = requests_list.filter((row_item) => {
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
        console.log(rows);
        rows = rows.map((row, rowi) => (
                <JadeRequestsTableRow row={row} rowi={rowi + pageStarti + 1} />
        ));
    }
    return (
        <>
            <SearchBar
                onChangeSearch={onChangeSearch}
            />
            <table>
                <JadeRequestsHeader/>
                {rows}
            </table>
            <PaginationFunctions
                onClickNextPageButton={onClickNextPageButton}
                onClickPreviousPageButton={onClickPreviousPageButton}
                currentPage={current_page}
                totalPages={total_pages}
            />
        </>
    )
}
