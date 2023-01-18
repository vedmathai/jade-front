import React, { useState, useEffect } from 'react'
import { useSearchParams } from "react-router-dom";
import UploadCode from './components/upload-code/upload-code';
import UploadData from './components/upload-data/upload-data';
import JadeRequestsTable from '../jade-requests/components/jade-requests-table/jade-requests-table';
import EditableDisplay from '../../common/editable-display/editable-display';
import NewJadeRequestModal from './components/new-jade-request-modal/new-jade-request-modal';
import getJadeProjectAPI from '../../apis/jade-projects/getJadeProjectAPI';
import putJadeProjectAPI from '../../apis/jade-projects/putJadeProjectAPI';
import './jade-project.css'


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

    return (
        <>
            <div className="page">
                <div className="page-row">
                    <h2 class="page-heading">Jade Project</h2>
                    <button>Delete</button>
                    <button
                        onClick={() => onClickEditProjectButton()}
                    >Edit</button>
                </div>
                <div className="page-row">
                    <div className="page-card">
                        <EditableDisplay
                            textLabel='Project Name'
                            textKey='name'
                            object={jadeProject}
                            onChangeEditableDisplayFn={onChangeEditableDisplayFn}
                            editingMode={editingMode}
                        />
                    </div>
                </div>
                <div className="page-row">
                    <span className="page-card">
                        <UploadCode 
                            jadeProject={jadeProject}
                        />
                    </span>
                    <span className="page-card">
                        <UploadData />
                    </span>
                </div>
                <div className="page-row">
                    <span className="page-card">
                        <button
                            className="new-request-button"
                            onClick={() => onClickNewJadeRequestButton()}
                        >New Request</button>
                        <JadeRequestsTable 
                            jadeProjectId={JadeProject.id}
                        />
                    </span>
                </div>
                <NewJadeRequestModal
                    showNewJadeRequestModal={showNewJadeRequestModal}
                    onClickCancelNewJadeRequestModal={onClickCancelNewJadeRequestModal}
                    jadeProject={jadeProject}
                />

            </div>
        </>
    )
}
