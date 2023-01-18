import './upload-data.css'

import uploadDataAPI from '../../../../apis/jade-projects/uploadDataAPI';


export default function UploadData(props) {

    const handleUploadDataFileReader = (event) => {
      let reader = new FileReader()
      reader.readAsDataURL(event.target.files[0]);
      reader.onload = (e) => {
        uploadDataAPI(e.target.result);
      }
    }
  
    return(
        <div className="upload-data">
            <div className="bulk-upload-properties-heading">Upload Data</div>
            <input
                className="bulk-upload-file-select"
                onChange={handleUploadDataFileReader}                
                type="file"
                accept=".zip"
            />
        </div>     
    )
}
