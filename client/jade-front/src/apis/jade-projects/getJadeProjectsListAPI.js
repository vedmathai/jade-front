import axios from 'axios';

const url = 'http://localhost:5000'


export default async function getJadeProjectsListAPI() {
    const projects_list = await axios
    .get(url + "/v1/jade-projects")
    .then(response => {
        const projects_list = response.data;
        return projects_list
    })
    .catch((err) => console.log(err))
    return projects_list
}