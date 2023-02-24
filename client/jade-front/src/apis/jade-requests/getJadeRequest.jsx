import axios from 'axios';


const url = 'http://localhost:5000'


export default async function getJadeRequestAPI(jade_project_id, jade_request_id) {
    const request = await axios
        .get(url + "/v1/jade_projects/" + jade_project_id + "/jade_requests/" + jade_request_id, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            const request = response.data;
            return request
        })
        .catch((err) => console.log(err))
    return request
}
