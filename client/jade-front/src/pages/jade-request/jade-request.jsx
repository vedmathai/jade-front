import React, { useState, useEffect } from 'react'
import { useSearchParams } from "react-router-dom";

import './jade-request.css'
import TopBar from '../../common/top-bar/top-bar';
import SideBar from '../../common/side-bar/side-bar';
import getJadeRequestAPI from '../../apis/jade-requests/getJadeRequest';
import getJadeMetaLogAPI from '../../apis/jade-logs/getJadeMetaLogAPI';


export default function JadeRequest(props) {

    const [searchParams, setSearchParams] = useSearchParams();
    const [jadeMetaLog, setJadeMetaLog] = useState();
    const [jadeRequest, setJadeRequest] = useState();

    const jadeProjectId = searchParams.get("jade-project-id");
    const jadeRequestId = searchParams.get("jade-request-id");

    const getJadeMetaLog = async () => {
        const jadeMetaLogResponse = await getJadeMetaLogAPI(jadeProjectId, jadeRequestId);
        const jadeRequestResponse = await getJadeRequestAPI(jadeProjectId, jadeRequestId);
        setJadeMetaLog(jadeMetaLogResponse);
        setJadeRequest(jadeRequestResponse);
    } 

    useEffect(() => {
        getJadeMetaLog();
    }, []);

    return (
        <>
            <div className="page">
                <SideBar />
                <TopBar />
                <div className="page-content">
                    <div className="page-row">
                        <h2 class="page-heading">Jade Request</h2>
                    </div>
                    <div className="page-row">
                        <div className="page-card extra">
                            {jadeRequestId}
                            {JSON.stringify(jadeRequest)}
                            {JSON.stringify(jadeMetaLog)}
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}
