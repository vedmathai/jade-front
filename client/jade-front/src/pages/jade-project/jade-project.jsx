import React, { useState, useEffect } from 'react'
import { useSearchParams } from "react-router-dom";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faEdit } from '@fortawesome/free-solid-svg-icons'

import UploadCode from './components/upload-code/upload-code';
import UploadData from './components/upload-data/upload-data';
import JadeRequestsTable from '../jade-requests/components/jade-requests-table/jade-requests-table';
import EditableDisplay from '../../common/editable-display/editable-display';
import NewJadeRequestModal from './components/new-jade-request-modal/new-jade-request-modal';
import getJadeProjectAPI from '../../apis/jade-projects/getJadeProjectAPI';
import putJadeProjectAPI from '../../apis/jade-projects/putJadeProjectAPI';
import './jade-project.css'
import TopBar from '../../common/top-bar/top-bar';
import SideBar from '../../common/side-bar/side-bar';


export default function JadeProject(props) {

    var [jadeProject, setJadeProject] = useState({});
    var [showNewJadeRequestModal, setShowNewJadeRequestModal] = useState(false);
    var [editingMode, setEditingMode] = useState(false);

    const [searchParams, setSearchParams] = useSearchParams();


    const getJadeProjectFn = async (project_id) => {
        const jadeProject = await getJadeProjectAPI(project_id);
        setJadeProject(jadeProject)
    }

    const putJadeProjectFn = async () => {
        await putJadeProjectAPI(jadeProject);
    }

    useEffect(() => {
        const jade_project_id = searchParams.get("jade-project-id")
        getJadeProjectFn(jade_project_id);
    }, []);

    const onChangeEditableDisplayFn = async (e, key) => {
        var tempJadeProject = {...jadeProject};
        tempJadeProject[key] = e.target.value;
        setJadeProject(tempJadeProject);
    }

    const onClickSaveJadeProjectFormButton = async () => {
        await putJadeProjectFn();
    }

    const onClickEditProjectButton = () => {
        if (editingMode === true) {
            putJadeProjectFn();
        }
        setEditingMode(!editingMode);
    }

    const onClickNewJadeRequestButton = () => {
        setShowNewJadeRequestModal(true);
    }

    const onClickCancelNewJadeRequestModal = () => {
        setShowNewJadeRequestModal(false);
    }

    const edit_toggle_class = editingMode? "edit-toggle-on" : "edit-toggle-off";

    return (
        <>
            <div className="page">
                <SideBar />
                <TopBar />
                <div className="page-content">
                    <div className="page-row">
                        <h2 class="page-heading">Jade Project</h2>
                    </div>
                    <div className="page-row">
                        <div className="page-card">
                            <div className="page-class-heading-row">
                                <span className="page-card-heading">
                                    Project Details
                                </span>
                                <span className="edit-toggle-container">
                                    <span
                                        className={"edit-toggle " + edit_toggle_class}
                                        onClick={() => onClickEditProjectButton()}
                                    ><FontAwesomeIcon icon={faEdit} />
                                    </span>
                                </span>
                            </div>
                            <EditableDisplay
                                textLabel='Project Name'
                                textKey='name'
                                object={jadeProject}
                                onChangeEditableDisplayFn={onChangeEditableDisplayFn}
                                editingMode={editingMode}
                            />
                            <div>
                                <button
                                    className="page-button alert-button delete-project-button"
                                >
                                    Delete this project
                                </button>
                            </div>
                        </div>
                    </div>
                    <div className="page-row">
                        <span className="page-card">
                            <div className="page-card-heading-row">
                                <div className="page-card-heading">
                                    Upload Code
                                </div>
                            </div>
                            <UploadCode 
                                jadeProject={jadeProject}
                            />
                        </span>
                        <span className="page-card">
                            <div className="page-card-heading-row">
                                <div className="page-card-heading">
                                    Upload Data
                                </div>
                            </div>
                            <UploadData
                                jadeProject={jadeProject} 
                            />
                        </span>
                    </div>
                    <div className="page-row">
                        <span className="page-card">
                            <div className="page-card-row">
                                <div className="page-card-heading">
                                    Jade Requests
                                </div>
                            </div>
                            <div className="page-card-row">
                                <button
                                    className="page-button new-request-button"
                                    onClick={() => onClickNewJadeRequestButton()}
                                >New Request</button>
                            </div>
                            <div className="jade-requests-table-container">
                                <JadeRequestsTable 
                                    jadeProjectId={JadeProject.id}
                                />
                            </div>
                        </span>
                    </div>
                    <NewJadeRequestModal
                        showNewJadeRequestModal={showNewJadeRequestModal}
                        onClickCancelNewJadeRequestModal={onClickCancelNewJadeRequestModal}
                        jadeProject={jadeProject}
                    />
                </div>
            </div>
        </>
    )
}
