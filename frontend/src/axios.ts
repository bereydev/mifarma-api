import axios from 'axios'

axios.defaults.baseURL = 'https://stag.mifarmacia.app/api/v1/';
axios.defaults.headers.common['Authorization'] = 'Bearer ' + localStorage.getItem('token');