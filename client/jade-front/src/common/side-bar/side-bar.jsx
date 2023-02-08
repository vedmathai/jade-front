import { useNavigate } from "react-router-dom";


import './side-bar.css'


function SideBarRow(props) {
    const navigate = useNavigate();
    const onClickSideBarRow = () => {
        navigate(props.url);
    }
    return (
        <div className="side-bar-row"
            onClick={() => onClickSideBarRow()}
        >
            {props.label}
        </div>
    )
}

export default function SideBar(props) {
    const side_bar_rows_dict = [
        {
            'label': 'Projects',
            'url': '/jade-projects',
        },
        {
            'label': 'Jobs',
            'url': '/jade-jobs-queue',
        },
    ]
    const side_bar_rows = side_bar_rows_dict.map((row_dict) => {
        return <SideBarRow 
            label={row_dict.label}
            url={row_dict.url}
        />
    })
        
    return (
        <div className="side-bar">
            {side_bar_rows}
        </div>
    )
}
