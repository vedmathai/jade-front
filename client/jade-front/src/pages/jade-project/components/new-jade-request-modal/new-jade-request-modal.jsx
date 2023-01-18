import React, { useState, useEffect } from 'react'
import FormInput from '../../../../common/form-item/form-item';
import getNewJadeRequestAPI from '../../../../apis/jade-requests/getNewJadeRequestAPI';
import postJadeRequestAPI from '../../../../apis/jade-requests/postJadeRequestAPI';
import './new-jade-request-modal.css'


export default function NewJadeRequestModal(props) {

    var [jadeRequest, setJadeRequest] = useState({});


    const getNewJadeRequestFn = async () => {
        const newJadeRequest = await getNewJadeRequestAPI(jadeRequest);
        console.log(JSON.stringify(props.jadeProject));
        newJadeRequest['jade_project'] = props.jadeProject['id'];
        setJadeRequest(newJadeRequest)
    }

    const postJadeRequestFn = async () => {
        await postJadeRequestAPI(jadeRequest);
        onClickCancelNewJadeRequestModal();
    }

    useEffect(() => {
        getNewJadeRequestFn();
    }, [props.showNewJadeRequestModal]);

    const onClickSubmitNewJadeRequestFormButton = async () => {
        await postJadeRequestFn();
        await props.refreshJadeRequestTableFn();
    }

    const onClickCancelNewJadeRequestModal = () => {
        props.onClickCancelNewJadeRequestModal();
    }

    const onChangeFormInputFn = (e, key) => {
        console.log(JSON.stringify(jadeRequest));
        var tempJadeRequest = {...jadeRequest};
        tempJadeRequest[key] = e.target.value;
        setJadeRequest(tempJadeRequest);
    }
    const submitNewJadeRequestFormButton = <button
            onClick={() => onClickSubmitNewJadeRequestFormButton()}
        >
            Submit
        </button>

    const cancelNewJadeRequestModalButton = <button
            onClick={() => onClickCancelNewJadeRequestModal()}
        >
            Cancel
        </button>

    const display_modal = props.showNewJadeRequestModal? '' : 'undisplay-modal';

    return (
        <>
            <div className={"modal ".concat(display_modal)}>
                <div>
                    <h2 class="modal-heading">New Jade Request</h2>
                </div>
                <div className='modal-row'>
                    <FormInput
                        formInputLabel='Request Name'
                        formInputKey='name'
                        onChangeFormInputFn={onChangeFormInputFn}
                    />
                </div>
                <div className='modal-row'>
                    <FormInput
                        formInputLabel='Number of Nodes'
                        formInputKey='nodes'
                        onChangeFormInputFn={onChangeFormInputFn}
                    />
                </div>
                <div className='modal-row'>
                    <FormInput
                        formInputLabel='Wall Clock Time'
                        formInputKey='wallclock_time'
                        onChangeFormInputFn={onChangeFormInputFn}
                    />
                </div>
                <div className='modal-row'>
                    <FormInput
                        formInputLabel='Number of GPUs'
                        formInputKey='number_gpus'
                        onChangeFormInputFn={onChangeFormInputFn}
                    />
                </div>
                <div className='modal-row'>
                    <FormInput
                        formInputLabel='Mail Type'
                        formInputKey='mail_type'
                        onChangeFormInputFn={onChangeFormInputFn}
                    />
                </div>
                <div className='modal-row'>
                    <FormInput
                        formInputLabel='Mail User'
                        formInputKey='mail_user'
                        onChangeFormInputFn={onChangeFormInputFn}
                    />
                </div>
                <div className='modal-row'>
                    <FormInput
                        formInputLabel='Partition'
                        formInputKey='partition'
                        onChangeFormInputFn={onChangeFormInputFn}
                    />
                </div>
                <div className='modal-row'>
                    <FormInput
                        formInputLabel='Code Invocation Command'
                        formInputKey='code_invocation'
                        onChangeFormInputFn={onChangeFormInputFn}
                    />
                </div>
                <div className='modal-row'>
                    {submitNewJadeRequestFormButton}
                    {cancelNewJadeRequestModalButton}
                </div>
            </div>
        </>
    )
}