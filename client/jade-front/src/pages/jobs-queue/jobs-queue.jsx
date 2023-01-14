import React, { useState, useEffect } from 'react'
import getJadeJobsQueue from '../../apis/jade-jobs-queue/getJadeJobsQueueAPI';
import QueueTable from './components/queue-table/queue-table';
import './jobs-queue.css'


export default function JadeJobsQueue() {
    var [jobsQueue, setJobsQueue] = useState([]);

    const getJobsQueueFn = async () => {
        var jobsQueue = await getJadeJobsQueue();
        setJobsQueue(jobsQueue);
    }

    useEffect(async () => {
        await getJobsQueueFn();
    }, []);

    const onClickRefreshJobsQueue = async () => {
        await getJobsQueueFn();

    }

    return (
        <>
            <div class="page-content">
                <div>
                    <h2 class="page-heading">Jobs Queue</h2>
                </div>
                <button
                    className="refresh-queue-button"
                    onClick={() => onClickRefreshJobsQueue()}
                > Refresh </button>
                <div className='table-container'>
                    <QueueTable jobsQueue={jobsQueue}/>
                </div>
            </div>
        </>
    )
}
