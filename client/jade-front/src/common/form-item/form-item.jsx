import './form-item.css'


export default function FormInput(props) {
    return (
        <span className="form-input">
            <span className="form-input-label">
                {props.formInputLabel}:
            </span>
            <span className='form-input-element'>
                <input
                    onChange={(e) => props.onChangeFormInputFn(e, props.formInputKey)}
                />
            </span>
        </span>
    )
}
