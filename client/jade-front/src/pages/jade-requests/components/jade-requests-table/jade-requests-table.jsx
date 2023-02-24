import React, { useState, useEffect } from 'react'
import { useNavigate } from "react-router-dom";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faFilter } from '@fortawesome/free-solid-svg-icons'
import './jade-requests-table.css'
import '../../../../common/css/table.css';



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
    const rowi = props.rowi;
    const navigate = useNavigate();
    const keys = ['job_id', 'name', 'partition']
    const vals = keys.map((key) => {
        return row[key]
    })
    const row_vals = [rowi].concat(vals);
    const row_div = row_vals.map((row_val, row_val_i) => (
        <JadeRequestsTableCell item={row_val}/>
    ))
    const onClickJadeRequestsTableRow = (jade_project_id, jade_request_id) => {
        navigate("/jade-request?jade-project-id=" + jade_project_id + "&jade-request-id=" + jade_request_id)
    }
    return (
        <tr className="table-row jade-requests-table-row"
            onClick={() => onClickJadeRequestsTableRow(props.jadeProjectId, row['id'])}
        >
            {row_div}
        </tr>
    )
        
}

function JadeRequestsHeader() {
    var headers = ['Sr. No.', 'Job Id', 'Name', 'Partition']
    headers = headers.map((header) => {
        return <th className="table-header">{header}</th>
    })
    return (
        <tr className='table-row jade-request-table-row'>
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
            > &lt;- Previous
            </button>
            <span className="pagination-page-numbers">
                Page {props.currentPage} / {props.totalPages}
            </span>
            <button
                className="pagination-button"
                onClick={() => props.onClickNextPageButton()}
            >Next -&gt;</button>
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
                placeholder='Filter Jade Requests'
                className="table-search"
                onChange={(e) => props.onChangeSearch(e.target.value)}
            />
        </span>
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

    var empty_state = <div
        className="empty-state-message"
    >
        There are no requests to display. Click the 'New Request' button above to create a new request.
    </div>

    var table_display = empty_state;

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
        rows = rows.map((row, rowi) => (
                <JadeRequestsTableRow row={row} rowi={rowi + pageStarti + 1} jadeProjectId={props.jadeProjectId} />
        ));
        var table = <div>
            <div className="table-search-container jade-requests-table-search-container">
                <SearchBar
                    onChangeSearch={onChangeSearch}
                />
            </div>
            <table className="table">
                <JadeRequestsHeader/>
                {rows}
            </table>
            <div className="pagination-functions-container jade-requests-pagination-functions-container">
                <PaginationFunctions
                    onClickNextPageButton={onClickNextPageButton}
                    onClickPreviousPageButton={onClickPreviousPageButton}
                    currentPage={current_page}
                    totalPages={total_pages}
                />
            </div>
        </div>
        table_display = page_rows.length > 0? table : empty_state;

    }
    return (
        <>
            {table_display}
        </>
    )
}
