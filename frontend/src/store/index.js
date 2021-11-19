import { createStore } from "vuex";
import axios from "axios";
import createPersistedState from "vuex-persistedstate";

const initialState = () => {
  return {
    currentUser: null,
    token: null,
    pharmacy: null,
    employees: [],
    customers: [],
    catalog: [],
    cart: [], 
    orders: [], 
    activePharmacies: [],
    inactivePharmacies: [],
    unverifiedOwners: [],
  }
}

export default createStore({
  state: initialState,
  mutations: {
    resetAll(state) {
      Object.assign(state, initialState())
    },
    updateCurrentUser(state, user) {
      state.currentUser = user;
    },
    updateCatalog(state, catalog) {
      state.catalog = catalog;
    },
    updateCart(state, cart) {
      state.cart = cart;
    },
    updateOrders(state, orders) {
      state.orders = orders;
    },
    updateToken(state, token) {
      state.token = token
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
      const response = await axios.get("/users/me/");
      commit("updateCurrentUser", response.data);
    },
    async updateCatalog({ commit }) {
      const response = await axios.get("/shop/catalog");
      commit("updateCatalog", response.data);
    },
    async updateCart({ commit }) {
      const response = await axios.get("/shop/get-cart");
      commit("updateCart", response.data);
    },
    async updateOrders({ commit }) {
      const response = await axios.get("/shop/order/history");
      commit("updateOrders", response.data);
    },
    async updatePharmacy({ commit }) {
      const response = await axios.get("/pharmacies/me/");
      commit("updatePharmacy", response.data);
    },
    async createPharmacy({ commit, dispatch }, payload) {
      try {
        const response = await axios.post("/pharmacies/", {
          name: payload.name,
          address: payload.address,
          address2: payload.address2,
          country: payload.country,
          city: payload.city,
          schedule: payload.schedule,
        });
        commit('updatePharmacy', response.data);
        dispatch('updateCurrentUser')
      } catch (error) {
        console.log(error)
        throw new Error('Unable to create a pharmacy')
      }


    },
    async updateEmployees({ commit }) {
      const response = await axios.get("/pharmacies/employees/");
      commit("updateEmployees", response.data);
    },
    async updateCustomers({ commit }) {
      try {
        const response = await axios.get("/pharmacies/customers/");
        commit("updateCustomers", response.data);
      } catch (err) {
        console.log(err)
        throw new Error('Unable to get a token.')
      }
    },
    async updateActivePharmacies({ commit }) {
      try {
        const response = await axios.get("/pharmacies/active/");
        commit('updateActivePharmacies', response.data);
      } catch (err) {
        console.log(err)
      }
    },
    async updateInactivePharmacies({ commit }) {
      try {
        const response = await axios.get("/admin/pharmacies/inactive/");
        commit('updateInactivePharmacies', response.data);
      } catch (err) {
        console.log(err)
      }
    },
    async updatePharmacies({ dispatch }) {
      dispatch('updateActivePharmacies');
      dispatch('updateInactivePharmacies');
    },
    async login({ commit, dispatch }, payload) {
      commit("resetAll");
      const params = new URLSearchParams();
      params.append("username", payload.username);
      params.append("password", payload.password);
      const response = await axios.post("/login/access-token/", params);
      commit("updateToken", response.data.access_token)
      commit("updateCurrentUser", response.data.user);
      dispatch("updatePharmacy")
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
      await dispatch("login", {
        username: payload.email,
        password: payload.password,
      });
    },
    async registerOwner({ dispatch }, payload) {
      await axios.post("/users/owner", {
        first_name: payload.first_name,
        last_name: payload.last_name,
        pharmacist_number: payload.pharmacist_number,
        email: payload.email,
        password: payload.password,
      });
      await dispatch("login", {
        username: payload.email,
        password: payload.password,
      });
    },
    async updateUnverifiedOwners({ commit }) {
      const response = await axios.get('/admin/owners/unverified/');
      commit("updateUnverifiedOwners", response.data);
    },
    async verifyOwner({ dispatch }, ownerId) {
      await axios.put(`/admin/verify-owner/${ownerId}`);
      dispatch('updateUnverifiedOwners');
    },
    async pickPharmacy({ commit }, pharmacy_id) {
      try {
        const response = await axios.post('/pharmacies/selection/', { pharmacy_id: pharmacy_id });
        commit("updatePharmacy", response.data);
        await this.dispatch('updateCurrentUser')
      } catch (error) {
        console.error(error);
      }
    }
  },
  getters: {
    getInactivePharmacyById: (state) => (id) => {
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
