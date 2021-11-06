import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

// route level code-splitting
// this generates a separate chunk (about.[hash].js) for this route
// which is lazy-loaded when the route is visited.
const Welcome = () => import(/* webpackChunkName: "welcome" */ "../views/customer/Welcome.vue");
const Login = () => import(/* webpackChunkName: "login" */ "../views/auth/Login.vue");
const Profile = () => import(/* webpackChunkName: "profile" */ "../views/auth/Profile.vue");
const PasswordRecovery = () => import(/* webpackChunkName: "password-recovery" */ "../views/auth/PasswordRecovery.vue");
const ResetPassword = () => import(/* webpackChunkName: "reset-password" */ "../views/auth/ResetPassword.vue");
const Register = () => import(/* webpackChunkName: "register" */ "../views/customer/Register.vue");
const RegisterPro = () => import(/* webpackChunkName: "register-pro" */ "../views/pro/Register.vue");
const DashboardCustomer = () => import(/* webpackChunkName: "dashboard-customer" */ "../views/customer/Dashboard.vue");
const Catalog = () => import(/* webpackChunkName: "catalog" */ "../views/customer/Catalog.vue");
const Cart = () => import(/* webpackChunkName: "cart" */ "../views/customer/Cart.vue");
const PharmaPicker = () => import(/* webpackChunkName: "pharma-picker" */ "../views/customer/PharmaPicker.vue");
const WelcomePro = () => import(/* webpackChunkName: "welcome-pro" */ "../views/pro/Welcome.vue");
const Drug = () => import(/* webpackChunkName: "drug" */ "../views/customer/Drug.vue");

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    alias: "/welcome",
    name: "Welcome",
    component: Welcome,
  },
  {
    path: "/login",
    name: "Login",

    component: Login,
  },
  {
    path: "/profile",
    name: "Profile",

    component: Profile,
  },
  {
    path: "/password-recovery",
    name: "PasswordRecovery",

    component: PasswordRecovery,
  },
  {
    path: "/reset-password",
    name: "ResetPassword",

    component: ResetPassword,
  },
  {
    path: "/register",
    name: "Register",

    component: Register,
  },
  {
    path: "/customer/dashboard",
    name: "DashboardCustomer",

    component: DashboardCustomer,
  },
  {
    path: "/customer/catalog",
    name: "Catalog",
    component: Catalog,
  },
  {
    path: "/pro/register",
    name: "RegisterPro",
    component: RegisterPro,
  },
  {
    path: "/customer/cart",
    name: "Cart",
    component: Cart,
  },
  {
    path: "/customer/pharma-picker",
    name: "PharmaPicker",

    component: PharmaPicker,
  },
  {
    path: "/customer/Drug",
    name: "Drug",

    component: Drug
  },
  {
    path: "/pro/welcome",
    name: "WelcomePro",

    component: WelcomePro,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
