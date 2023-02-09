import React, { useState, useEffect } from 'react'
import getJadeProjectsListAPI from '../../apis/jade-projects/getJadeProjectsListAPI';
import SideBar from '../../common/side-bar/side-bar';
import TopBar from '../../common/top-bar/top-bar';
import JadeProjectsTable from './components/jade-projects-table/jade-projects-table';
import NewJadeProjectModal from './components/new-jade-project-modal/new-jade-project-modal';
import '../pages.css'
import './jade-projects.css'


export default function JadeProjectsList() {
    var [jadeProjectsList, setJadeProjectsList] = useState({});
    var [showNewJadeProjectModal, setShowNewJadeProjectModal] = useState(false);


    const getJadeProjectsFn = async () => {
        var jadeProjectsList = await getJadeProjectsListAPI();
        setJadeProjectsList(jadeProjectsList);
    }
    
    useEffect(() => {
        getJadeProjectsFn();
    }, []);

    const onClickNewJadeProjectButton = () => {
        setShowNewJadeProjectModal(true);
    }

    const onClickCancelNewJadeProjectModalButton = async () => {
        setShowNewJadeProjectModal(false);
        await getJadeProjectsFn();
    }

    const refreshJadeProjectsTableFn = async () => {
        await getJadeProjectsFn();
    }

    const new_jade_project_button = <button
        className='page-button new-jade-project-button'
        onClick={() => onClickNewJadeProjectButton()}
    >
        New Project
    </button>

    return (
        <div className="page">
            <SideBar />
            <TopBar />
            <div className="page-content">
                <div>
                    <h2 class="page-heading">Jade Projects</h2>
                </div>
                <div className='table-container'>
                    <div className="new-jade-project-button-container">
                        {new_jade_project_button}
                    </div>
                    <JadeProjectsTable
                        jadeProjectsList={jadeProjectsList}
                    ></JadeProjectsTable>
                </div>
            </div>
            <NewJadeProjectModal 
                showNewJadeProjectModal={showNewJadeProjectModal}
                onClickCancelNewJadeProjectModalButton={onClickCancelNewJadeProjectModalButton}
                refreshJadeProjectsTableFn={refreshJadeProjectsTableFn}
            />
        </div>
    )
}
