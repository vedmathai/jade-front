import axios from 'axios';


const url = 'http://localhost:5000'


export default async function getJadeMetaLogAPI(jade_project_id, jade_request_id) {
    console.log(jade_project_id, jade_request_id);
    const api = url + '/v1/jade-projects/' + jade_project_id + '/jade-requests/' + jade_request_id + '/jade-log-metadata';
    const metalog = await axios
        .get(api, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            const metalog = response.data;
            return metalog
        })
        .catch((err) => console.log(err))
    return metalog
}
