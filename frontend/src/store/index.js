import { createStore } from "vuex";
import axios from "axios";
import createPersistedState from "vuex-persistedstate";

export default createStore({
  state: {
    currentUser: null,
    pharmacy: null,
    employees: [],
    customers: [],
    activePharmacies: [],
    unverifiedOwners: [],
  },
  mutations: {
    updateCurrentUser(state, user) {
      state.currentUser = user;
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
    updateUnverifiedOwners(state, unverifiedOwners) {
      state.unverifiedOwners = unverifiedOwners
    }
  },
  actions: {
    async updateCurrentUser({ commit }) {
      const response = await axios.get("/users/me");
      commit("updateCurrentUser", response.data);
    },
    async updatePharmacy({ commit }) {
      const response = await axios.get("/pharmacies/me");
      commit("updatePharmacy", response.data);
    },
    async updateEmployees({ commit }) {
      const response = await axios.get("/pharmacies/employees");
      commit("updateEmployees", response.data);
    },
    async updateCustomers({ commit }) {
      const response = await axios.get("/pharmacies/customers");
      commit("updateCustomers", response.data);
    },
    async login({ commit }, payload) {
      const params = new URLSearchParams();
      params.append("username", payload.username);
      params.append("password", payload.password);
      const response = await axios.post("/login/access-token/", params);
      localStorage.setItem("token", response.data.access_token);
      commit("updateCurrentUser", response.data.currentUser);
    },
    async registerCustomer({ dispatch }, payload) {
      await axios.post("/users/customer", {
        first_name: payload.first_name,
        last_name: payload.last_name,
        email: payload.email,
        address: payload.address,
        postcode: payload.postcode,
        city: payload.city,
        password: payload.password,
      });
      dispatch("login", {
        username: payload.email,
        password: payload.password,
      });
    },
    async updateUnverifiedOwners({ commit }) {
      const response = await axios.get('/admin/unverified/owners');
      commit("updateUnverifiedOwners", response.data);
    },
    async verifyOwner({ dispatch, state }, pharmacyId) {
      dispatch('updatePharmacyOwner', pharmacyId);
      const pharmacy = state.pharmacies.find(obj => obj.id == pharmacyId);
      await axios.put(`/admin/verify-owner/${pharmacy.owner.id}`);
    }
  },
  modules: {},
  plugins: [createPersistedState()],
});
