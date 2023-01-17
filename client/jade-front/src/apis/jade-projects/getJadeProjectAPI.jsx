import axios from 'axios';

const url = 'http://localhost:5000'


export default async function getJadeProjectAPI(project_id) {
    const project = await axios
    .get(url + "/v1/jade-projects/" + project_id)
    .then(response => {
        const project = response.data;
        return project
    })
    .catch((err) => console.log(err))
    return project
}
