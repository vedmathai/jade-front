import axios from 'axios';


const url = 'http://localhost:5000'


export default async function getJadeRequestStatusAPI(jade_project_id, jade_request_id) {
    console.log(jade_project_id, jade_request_id);
    const api = url + '/v1/jade-projects/' + jade_project_id + '/jade-requests/' + jade_request_id + '/jade-request-status';
    const status = await axios
        .get(api, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            const status = response.data;
            return status
        })
        .catch((err) => console.log(err))
    return status
}
