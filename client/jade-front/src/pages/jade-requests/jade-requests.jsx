import React, { useState, useEffect } from 'react'
import getJadeRequestsListAPI from '../../apis/jade-requests/getJadeRequestsListAPI';
import JadeRequestsTable from './components/jade-requests-table/jade-requests-table';
import './jade-requests.css'


export default function JadeRequestsList() {
    var [jadeRequestsList, setJadeRequestsList] = useState([]);

    const getJadeRequestsFn = async () => {
        var jadeRequestsList = await getJadeRequestsListAPI();
        setJadeRequestsList(jadeRequestsList);
    }
    <JadeRequestsTable jadeRequestsList={jadeRequestsList}/>
    useEffect(async () => {
        await getJadeRequestsFn();
    }, []);


    return (
        <>
            <div class="page-content">
                <div>
                    <h2 class="page-heading">Jade Requests</h2>
                </div>
                <div className='table-container'>
                    <JadeRequestsTable
                        jadeRequestsList={jadeRequestsList}
                    ></JadeRequestsTable>
                </div>
            </div>
        </>
    )
}
