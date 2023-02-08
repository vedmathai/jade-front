import React, { useState, useEffect } from 'react'
import { useNavigate } from "react-router-dom";
import './jade-projects-table.css'
import '../../../../common/css/table.css';


function JadeProjectsTableCell(props){
    var item = props.item;
    return (
        <td className="table-cell jade-projects-table-cell">
            {item}
        </td>
    )
}

function JadeProjectsTableRow(props){
    const row = props.row;
    const rowi = props.rowi;
    const keys = ['name']
    const navigate = useNavigate();
    const vals = keys.map((key) => {
        return row[key]
    })
    const row_vals = [rowi].concat(vals);
    const row_div = row_vals.map((row_val, row_val_i) => (
        <JadeProjectsTableCell item={row_val}/>
    ))

    const onClickJadeProjectsTableRow = (id) => {
        navigate("/jade-project?jade-project-id=" +id)
    }
    
    return (
        <tr className="table-row jade-projects-table-row"
            onClick={() => onClickJadeProjectsTableRow(row['id'])}
        >
            {row_div}
        </tr>
    )
        
}

function JadeProjectsHeader() {
    var headers = ['Sr. No.', 'Name']
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
            >&lt;- Previous
            </button>
            Page {props.currentPage} / {props.totalPages}
            <button
                className="pagination-button"
                onClick={() => props.onClickNextPageButton()}
            >Next -&gt;</button>
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

export default function JadeProjectsTable(props) {
    var [pageStarti, setPageStarti] = useState(0);
    var [searchTerm, setSearchTerm] = useState('');
    var current_page = 0;
    var total_pages = 0

    var projects_list = props.jadeProjectsList;
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
    }

    var empty_state = <div>
        There are no projects to display. Click the 'New Project' button above to create a new project.
    </div>

    if (projects_list.jade_project_list) {
        var page_rows = projects_list.jade_project_list.filter((row_item) => {
            if (searchTerm.length == 0) { return true }
            let values = Object.values(row_item);
            for (let i in values) {
                if ((values[i] !== null) && (values[i].includes(searchTerm))) {
                    return true;
                }
            }
            return false;
        })
        current_page = Math.ceil((pageStarti + 1) / page_size)
        total_pages = Math.ceil(page_rows.length / page_size)
        var rows = page_rows.slice(pageStarti, pageStarti + page_size);
        rows = rows.map((row, rowi) => (
            <JadeProjectsTableRow row={row} rowi={rowi + pageStarti + 1} />
        ));
        empty_state = page_rows.length > 0? '' : empty_state;
    }
    return (
        <>
            {empty_state}
            <SearchBar
                onChangeSearch={onChangeSearch}
            />
            <table className='table'>
                <JadeProjectsHeader/>
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
