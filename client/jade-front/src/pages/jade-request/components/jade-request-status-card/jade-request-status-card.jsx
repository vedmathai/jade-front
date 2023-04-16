import React, { useState, useEffect } from 'react'

import EditableDisplay from '../../../../common/editable-display/editable-display';

import './jade-request-status-card.css'

export default function JadeRequestStatusCard(props) {
    const requestStatus = props.jadeRequestStatus;

    return (
        <>
            <div className="page-card jade-run-page-card">
                <div className="page-card-heading">
                    Jade Request Status
                </div>
                <EditableDisplay
                    textLabel='Current Epoch'
                    textKey='current_epoch_i'
                    object={requestStatus}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Total Epochs'
                    textKey='total_epochs'
                    object={requestStatus}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Train Precision'
                    textKey='train_precision'
                    object={requestStatus}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Train Recall'
                    textKey='train_recall'
                    object={requestStatus}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Train F1'
                    textKey='train_f1'
                    object={requestStatus}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Train Exact Match'
                    textKey='train_exact_match'
                    object={requestStatus}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Evaluate Precision'
                    textKey='evaluate_precision'
                    object={requestStatus}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Evaluate Recall'
                    textKey='evaluate_recall'
                    object={requestStatus}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Evaluate F1'
                    textKey='evaluate_f1'
                    object={requestStatus}
                    editingMode={false}
                />
                <EditableDisplay
                    textLabel='Evaluate Exact Match'
                    textKey='evaluate_exact_match'
                    object={requestStatus}
                    editingMode={false}
                />
            </div>
        </>
    )
}
