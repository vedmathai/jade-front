import './editable-display.css'


export default function EditableDisplay(props) {
    const editing = <span className="form-input">
        <span className="form-input-label">
            {props.textLabel}:
        </span>
        <span className='form-input-element'>
            <input
                value={props.object[props.textKey]}
                onChange={(e) => props.onChangeEditableDisplayFn(e, props.textKey)}
            />
        </span>
    </span>

    const non_editing = <span className="form-input">
        <span className="form-input-label">
            {props.textLabel}:
        </span>
        <span className='form-input-element'>
            {props.object[props.textKey]}
        </span>
    </span>

    const display = props.editingMode? editing : non_editing;

    return (
        <>
            {display}
        </>
    )
}
