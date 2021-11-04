import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

// route level code-splitting
// this generates a separate chunk (about.[hash].js) for this route
// which is lazy-loaded when the route is visited.
const Dashboard = () => import(/* webpackChunkName: "dashboard" */ "../views/Dashboard.vue");
const Login = () => import(/* webpackChunkName: "login" */ "../views/Login.vue");
const Profile = () => import(/* webpackChunkName: "profile" */ "../views/Profile.vue");
const PasswordRecovery = () => import(/* webpackChunkName: "password-recovery" */ "../views/PasswordRecovery.vue");
const ResetPassword = () => import(/* webpackChunkName: "reset-password" */ "../views/ResetPassword.vue");
const Register = () => import(/* webpackChunkName: "register" */ "../views/customer/Register.vue");
const RegisterPro = () => import(/* webpackChunkName: "register-pro" */ "../views/pro/Register.vue");
const HomeCustomer = () => import(/* webpackChunkName: "customerHome" */ "../views/customer/Home.vue");
const Catalog = () => import(/* webpackChunkName: "Catalog" */ "../views/customer/Catalog.vue");

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Dashboard",
    component: Dashboard,
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
    path: "/customer/home",
    name: "HomeCustomer",

    component: HomeCustomer,
  },
  {
    path: "/customer/Catalog",
    name: "Catalog",
    component: Catalog,
  },
  {
    path: "/pro/register",
    name: "RegisterPro",
    component: RegisterPro,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
