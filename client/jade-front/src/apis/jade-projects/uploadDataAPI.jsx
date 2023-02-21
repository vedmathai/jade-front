import axios from 'axios';


const url = 'http://localhost:5000'


export default async function uploadDataAPI(project_id, data) {
    var formData = new FormData();
    formData.append('file', data);
    const response = await axios
    .post(url + '/v1/jade-projects/' + project_id + '/data', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
    })
    .then(response => {
        const property = response.data;
        return property
    })
    .catch((err) => console.log(err))
    return response
}
