import axios from "axios";
import store from "@/store"

// axios.defaults.baseURL = 'https://stag.mifarmacia.app/api/v1/';
axios.defaults.baseURL = "http://localhost/api/v1/";
axios.defaults.headers.common["Authorization"] =
  "Bearer " + store.state.token;
axios.defaults.headers.common["Access-Control-Allow-Origin"] =
  "http:/localhost:8080";
