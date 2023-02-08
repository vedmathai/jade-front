import React, { useState, useEffect } from 'react'
import getJadeJobsQueue from '../../apis/jade-jobs-queue/getJadeJobsQueueAPI';
import SideBar from '../../common/side-bar/side-bar';
import TopBar from '../../common/top-bar/top-bar';
import QueueTable from './components/queue-table/queue-table';
import './jobs-queue.css'


export default function JadeJobsQueue() {
    var [jobsQueue, setJobsQueue] = useState([]);

    const getJobsQueueFn = async () => {
        var jobsQueue = await getJadeJobsQueue();
        setJobsQueue(jobsQueue);
    }

    useEffect(() => {
        getJobsQueueFn();
    }, []);

    const onClickRefreshJobsQueue = async () => {
        await getJobsQueueFn();

    }

    return (
        <div className='page'>
            <SideBar />
            <TopBar />
            <div class="page-content">
                <div>
                    <h2 class="page-heading">Jobs Queue</h2>
                </div>
                <button
                    className="refresh-queue-button page-button"
                    onClick={() => onClickRefreshJobsQueue()}
                > Refresh </button>
                <div className='table-container'>
                    <QueueTable jobsQueue={jobsQueue}/>
                </div>
            </div>
        </div>
    )
}
