import axios from 'axios';

const url = 'http://localhost:5000'


export default async function getNewJadeRequestAPI() {
    const request = await axios
    .get(url + "/v1/jade_requests/new")
    .then(response => {
        const request = response.data;
        return request
    })
    .catch((err) => console.log(err))
    return request
}
