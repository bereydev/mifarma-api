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
    inactivePharmacies: [],
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
    },
    updateActivePharmacies(state, activePharmacies) {
      state.activePharmacies = activePharmacies
    },
    updateInactivePharmacies(state, inactivePharmacies) {
      state.inactivePharmacies = inactivePharmacies
    },
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
      try {
        const response = await axios.get("/pharmacies/customers");
        commit("updateCustomers", response.data);
      } catch (err) {
        console.log(err)
        throw new Error('Unable to get a token.')
      }
    },
    async updateActivePharmacies({ commit }) {
      try {
        const response = await axios.get("/pharmacies/active");
        commit('updateActivePharmacies', response.data);
      } catch (err) {
        console.log(err)
      }
    },
    async updateInactivePharmacies({ commit }) {
      try {
        const response = await axios.get("/admin/pharmacies/inactive");
        commit('updateInactivePharmacies', response.data);
      } catch (err) {
        console.log(err)
      }
    },
    async updatePharmacies({ dispatch }) {
      dispatch('updateActivePharmacies');
      dispatch('updateInactivePharmacies');
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
      const response = await axios.get('/admin/owners/unverified');
      commit("updateUnverifiedOwners", response.data);
    },
    async verifyOwner({ dispatch }, ownerId) {
      await axios.put(`/admin/verify-owner/${ownerId}`);
      dispatch('updateUnverifiedOwners');
    },
  },
  getters: {
    getInactivePharmacyById: (state) => (id) => {
      console.log(state.inactivePharmacies.find(pharma => pharma.id === id))
      return state.inactivePharmacies.find(pharma => pharma.id === id)
    },
    activePharmaciesCount: state => {
      return state.activePharmacies.length
    },
    inactivePharmaciesCount: state => {
      return state.inactivePharmacies.length
    },
  },
  modules: {},
  plugins: [createPersistedState()],
});
