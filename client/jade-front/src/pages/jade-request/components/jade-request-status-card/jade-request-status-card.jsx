import React, { useState, useEffect } from 'react'

import EditableDisplay from '../../../../common/editable-display/editable-display';

import './jade-request-status-card.css'

export default function JadeRequestStatusCard(props) {
    const requestStatus = props.requestStatus;

    return (
        <>
            <div className="page-card jade-run-page-card">
                <div className="page-card-heading">
                    Jade Request Status
                </div>
                {JSON.stringify(props.jadeRequestStatus)}
            </div>
        </>
    )
}
