import axios from "axios";

// axios.defaults.baseURL = 'https://stag.mifarmacia.app/api/v1/';
axios.defaults.baseURL = "http://localhost/api/v1/";
axios.defaults.headers.common["Authorization"] =
  "Bearer " + localStorage.getItem("token");
axios.defaults.headers.common["Access-Control-Allow-Origin"] =
  "http:/localhost:8080";
