import React, { useState, useEffect } from 'react'

import EditableDisplay from '../../../../common/editable-display/editable-display';

import './jade-request-info-card.css'

export default function JadeRequestInfoCard(props) {
    const jadeRequest = props.jadeRequest;

    return (
        <>
            <div className="page-card jade-request-page-card">
                <div className="page-card-heading">
                    Jade Request Parameters
                </div>
                <EditableDisplay
                    textLabel='Name'
                    textKey='name'
                    object={jadeRequest}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Job ID'
                    textKey='job_id'
                    object={jadeRequest}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Nodes'
                    textKey='nodes'
                    object={jadeRequest}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Wall Clock Time'
                    textKey='wallclock_time'
                    object={jadeRequest}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Number of GPUs'
                    textKey='number_gpus'
                    object={jadeRequest}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Mail Type'
                    textKey='mail_type'
                    object={jadeRequest}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Mail User'
                    textKey='mail_user'
                    object={jadeRequest}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Partition'
                    textKey='partition'
                    object={jadeRequest}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Code Invocation'
                    textKey='code_invocation'
                    object={jadeRequest}
                    editingMode={false}
                />
            </div>
        </>
    )
}
