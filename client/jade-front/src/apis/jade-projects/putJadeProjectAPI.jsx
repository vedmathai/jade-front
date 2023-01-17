import axios from 'axios';


const url = 'http://localhost:5000'

export default async function putJadeProjectAPI(jade_project) {
    const response = await axios
        .post(url + '/v1/jade-projects', jade_project, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            const project = response.data;
            return project
        })
        .catch((err) => console.log(err))
    return response
}
