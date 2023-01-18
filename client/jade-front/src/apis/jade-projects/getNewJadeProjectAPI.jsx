import axios from 'axios';

const url = 'http://localhost:5000'


export default async function getNewJadeProjectAPI() {
    const project = await axios
    .get(url + "/v1/jade-projects/new")
    .then(response => {
        const project = response.data;
        return project
    })
    .catch((err) => console.log(err))
    return project
}
