import React, { useState, useEffect } from 'react'
import getJadeProjectsListAPI from '../../apis/jade-projects/getJadeProjectsListAPI';
import JadeProjectsTable from './components/jade-projects-table/jade-projects-table';
import NewJadeProjectModal from './components/new-jade-project-modal/new-jade-project-modal';
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
        onClick={() => onClickNewJadeProjectButton()}
    >
        New Project
    </button>

    return (
        <>
            <div class="page-content">
                <NewJadeProjectModal 
                    showNewJadeProjectModal={showNewJadeProjectModal}
                    onClickCancelNewJadeProjectModalButton={onClickCancelNewJadeProjectModalButton}
                    refreshJadeProjectsTableFn={refreshJadeProjectsTableFn}
                />
                <div>
                    <h2 class="page-heading">Jade Projects</h2>
                </div>
                <div className='table-container'>
                    {new_jade_project_button}
                    <JadeProjectsTable
                        jadeProjectsList={jadeProjectsList}
                    ></JadeProjectsTable>
                </div>
            </div>
        </>
    )
}
