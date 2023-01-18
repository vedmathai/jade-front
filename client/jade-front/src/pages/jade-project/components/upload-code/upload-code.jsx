import './upload-code.css'

import uploadCodeAPI from '../../../../apis/jade-projects/uploadCodeAPI';


export default function UploadCode(props) {

    const handleUploadCodeFileReader = (event) => {
      let reader = new FileReader()
      reader.readAsDataURL(event.target.files[0]);
      reader.onload = (e) => {
        uploadCodeAPI(props.jadeProject.id, e.target.result);
      }
      
    }
  
    return(
        <div className="upload-code">
            <div className="bulk-upload-properties-heading">Upload Code</div>
            <input
                className="bulk-upload-file-select"
                onChange={handleUploadCodeFileReader}                
                type="file"
                accept=".zip"
            />
        </div>     
    )
}
