import { createStore } from "vuex";
import axios from 'axios';

export default createStore({
  state: {
    user: {},
    pharmacy: {},
    employees: [],
    customers: [],
  },
  mutations: {
    updateUser(state, user) {
      state.user = user;
    },
    updatePharmacy(state, pharmacy) {
      state.pharmacy = pharmacy;
    },
    updateEmployees(state, employees) {
      state.employees = employees;
    },
    updateCustomers(state, customers) {
      state.customers = customers;
    },
  },
  actions: {
    async updateUser({ commit }) {
      const response = await axios.get('/users/me');
      commit('updateUser', response.data);
    },
    async updatePharmacy({ commit }) {
      const response = await axios.get('/pharmacies/me');
      commit('updatePharmacy', response.data);
    },
    async updateEmployees({ commit }) {
      const response = await axios.get('/pharmacies/employees');
      commit('updateEmployees', response.data);
    },
    async updateCustomers({ commit }) {
      const response = await axios.get('/pharmacies/customers');
      commit('updateCustomers', response.data);
    },
  },
  modules: {},
});
