import axios from 'axios';

const url = 'http://localhost:5000'


export default async function getJadeRequestTemplateAPI(template_id) {
    const request_template = await axios
    .get(url + "/v1/request-templates/1234")
    .then(response => {
        const request = response.data;
        return request
    })
    .catch((err) => console.log(err))
    return request_template
}
