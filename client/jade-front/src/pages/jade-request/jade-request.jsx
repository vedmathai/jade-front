import React, { useState, useEffect } from 'react'
import { useSearchParams } from "react-router-dom";

import './jade-request.css'
import TopBar from '../../common/top-bar/top-bar';
import SideBar from '../../common/side-bar/side-bar';
import JadeRequestInfoCard from './components/jade-request-info-card/jade-request-info-card';
import JadeRequestStatusCard from './components/jade-request-status-card/jade-request-status-card';
import getJadeRequestStatusAPI from '../../apis/jade-logs/getJadeRequestStatusAPI';
import getJadeRequestAPI from '../../apis/jade-requests/getJadeRequest';


export default function JadeRequest(props) {

    const [searchParams, setSearchParams] = useSearchParams();
    const [jadeRequestStatus, setJadeRequestStatus] = useState({});
    const [jadeRequest, setJadeRequest] = useState({});

    const jadeProjectId = searchParams.get("jade-project-id");
    const jadeRequestId = searchParams.get("jade-request-id");

    const getJadeRequestStatus = async () => {
        const jadeRequestStatus = await getJadeRequestStatusAPI(jadeProjectId, jadeRequestId);
        setJadeRequestStatus(jadeRequestStatus);
    }

    const getJadeRequestResponse = async () => {
        const jadeRequestResponse = await getJadeRequestAPI(jadeProjectId, jadeRequestId);
        setJadeRequest(jadeRequestResponse);
    }

    useEffect(() => {
        getJadeRequestResponse();
        getJadeRequestStatus();
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
                        <JadeRequestInfoCard
                            jadeRequest={jadeRequest}
                        />
                        <JadeRequestStatusCard
                            jadeRequestStatus={jadeRequestStatus}
                        />
                    </div>
                </div>
            </div>
        </>
    )
}
