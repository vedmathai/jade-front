import axios from 'axios';


const url = 'http://localhost:5000'


export default async function postJadeRequestAPI(jade_project_id, jade_request) {
    const request = await axios
        .post(url + "/v1/jade_projects/" + jade_project_id + "/jade_requests", jade_request, {
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
