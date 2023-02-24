import axios from 'axios';

const url = 'http://localhost:5000'


export default async function getNewJadeRequestAPI(jade_project_id) {
    const request = await axios
    .get(url + "/v1/jade_projects/" + jade_project_id + "/jade_requests/new")
    .then(response => {
        const request = response.data;
        return request
    })
    .catch((err) => console.log(err))
    return request
}
