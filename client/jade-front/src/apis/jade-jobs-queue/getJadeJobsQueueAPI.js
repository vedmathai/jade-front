import axios from 'axios';

const url = 'http://localhost:5000'


export default async function getJadeJobsQueue() {
    const jobs = await axios
    .get(url + "/v1/jobs")
    .then(response => {
        const jobs = response.data;
        return jobs
    })
    .catch((err) => console.log(err))
    return jobs
}