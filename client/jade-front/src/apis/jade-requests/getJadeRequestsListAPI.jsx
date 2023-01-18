import axios from 'axios';

const url = 'http://localhost:5000'


export default async function getJadeRequestsListAPI() {
    const requests_list = await axios
    .get(url + "/v1/jade_requests")
    .then(response => {
        const requests_list = response.data;
        return requests_list
    })
    .catch((err) => console.log(err))
    return requests_list
}