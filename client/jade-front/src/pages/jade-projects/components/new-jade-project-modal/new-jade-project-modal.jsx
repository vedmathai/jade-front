import React, { useState, useEffect } from 'react'
import FormInput from '../../../../common/form-item/form-item';
import getNewJadeProjectAPI from '../../../../apis/jade-projects/getNewJadeProjectAPI';
import postJadeProjectAPI from '../../../../apis/jade-projects/postJadeProjectAPI';
import './new-jade-project-modal.css'


export default function NewJadeProjectModal(props) {

    var [jadeProject, setJadeProject] = useState({});


    const getNewJadeProjectFn = async () => {
        const newJadeProject = await getNewJadeProjectAPI(jadeProject);
        setJadeProject(newJadeProject)
    }

    const postJadeProjectFn = async () => {
        await postJadeProjectAPI(jadeProject);
        onClickCancelNewJadeProjectModalButton();
    }

    useEffect(() => {
        getNewJadeProjectFn();
    }, []);

    const onClickSubmitNewJadeProjectFormButton = async () => {
        await postJadeProjectFn();
        await props.refreshJadeProjectsTableFn();
    }

    const onClickCancelNewJadeProjectModalButton = () => {
        props.onClickCancelNewJadeProjectModalButton();
    }

    const onChangeFormInputFn = (e, key) => {
        var tempJadeProject = {...jadeProject};
        tempJadeProject[key] = e.target.value;
        setJadeProject(tempJadeProject);
    }
    const submitNewJadeProjectFormButton = <button
            onClick={() => onClickSubmitNewJadeProjectFormButton()}
        >
            Create
        </button>

    const CancelNewJadeProjectModalButton = <button
            onClick={() => onClickCancelNewJadeProjectModalButton()}
        >
            Cancel
        </button>

    const display_modal = props.showNewJadeProjectModal? '' : 'undisplay-modal';

    return (
        <>
            <div className={"modal ".concat(display_modal)}>
                <div>
                    <h2 class="modal-heading">New Jade Project</h2>
                </div>
                <div className='modal-row'>
                    <FormInput
                        formInputLabel='Project Name'
                        formInputKey='name'
                        onChangeFormInputFn={onChangeFormInputFn}
                    />
                </div>
                <div className='modal-row'>
                    {submitNewJadeProjectFormButton}
                    {CancelNewJadeProjectModalButton}
                </div>
            </div>
        </>
    )
}
