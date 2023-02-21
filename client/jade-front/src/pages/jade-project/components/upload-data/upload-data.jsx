import './upload-data.css'

import uploadDataAPI from '../../../../apis/jade-projects/uploadDataAPI';


export default function UploadData(props) {

    const handleUploadDataFileReader = (event) => {
      let reader = new FileReader()
      reader.readAsDataURL(event.target.files[0]);
      reader.onload = (e) => {
        uploadDataAPI(props.jadeProject.id, e.target.result);
      }
    }
  
    return(
        <div className="upload-data">
            <input
                className="bulk-upload-file-select"
                onChange={handleUploadDataFileReader}                
                type="file"
                accept=".zip"
            />
        </div>     
    )
}
