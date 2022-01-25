import { createRouter, createWebHistory } from "vue-router";
import store from "@/store";
import { Role } from '@/_helpers/Role';

// route level code-splitting
// this generates a separate chunk (about.[hash].js) for this route
// which is lazy-loaded when the route is visited.
const Welcome = () =>
  import(/* webpackChunkName: "welcome" */ "../views/customer/Welcome.vue");
const Login = () =>
  import(/* webpackChunkName: "login" */ "../views/auth/Login.vue");
const CustomerProfile = () =>
  import(/* webpackChunkName: "customer-profile" */ "../views/customer/CustomerProfile.vue");
const PasswordRecovery = () =>
  import(
    /* webpackChunkName: "password-recovery" */ "../views/auth/PasswordRecovery.vue"
  );
const ResetPassword = () =>
  import(
    /* webpackChunkName: "reset-password" */ "../views/auth/ResetPassword.vue"
  );
const Register = () =>
  import(/* webpackChunkName: "register" */ "../views/auth/Register.vue");
const RegisterPro = () =>
  import(/* webpackChunkName: "register-pro" */ "../views/pro/Register.vue");
const DashboardCustomer = () =>
  import(
    /* webpackChunkName: "dashboard-customer" */ "../views/customer/Dashboard.vue"
  );
const DashboardPro = () =>
  import(/* webpackChunkName: "dashboard-pro" */ "../views/pro/Dashboard.vue");
const DashboardAdmin = () =>
  import(
    /* webpackChunkName: "dashboard-admin" */ "../views/admin/Dashboard.vue"
  );
const Catalog = () =>
  import(/* webpackChunkName: "catalog" */ "../views/customer/Catalog.vue");
const Cart = () =>
  import(/* webpackChunkName: "cart" */ "../views/customer/Cart.vue");
const PharmaPicker = () =>
  import(
    /* webpackChunkName: "pharma-picker" */ "../views/customer/PharmaPicker.vue"
  );
const WelcomePro = () =>
  import(/* webpackChunkName: "welcome-pro" */ "../views/pro/Welcome.vue");
const Drug = () =>
  import(/* webpackChunkName: "drug" */ "../views/customer/Drug.vue");
const CreatePharma = () =>
  import(
    /* webpackChunkName: "create-pharma" */ "../views/pro/CreatePharma.vue"
  );

const routes = [
  {
    path: "/",
    alias: "/welcome",
    name: "Welcome",
    meta: {
      pharmaRequired: false,
    },
    component: Welcome,
  },
  {
    path: "/login",
    name: "Login",
    meta: {
      pharmaRequired: false,
    },

    component: Login,
  },
  {
    path: "/customer/profile",
    name: "CustomerProfile",
    

    component: CustomerProfile,
  },
  {
    path: "/password-recovery",
    name: "PasswordRecovery",
    meta: {
      pharmaRequired: false,
    },

    component: PasswordRecovery,
  },
  {
    path: "/reset-password",
    name: "ResetPassword",
    meta: {
      pharmaRequired: false,
    },

    component: ResetPassword,
  },
  {
    path: "/register",
    name: "Register",
    meta: {
      pharmaRequired: false,
    },

    component: Register,
  },
  {
    path: "/customer/dashboard",
    name: "DashboardCustomer",
    meta: {
      authorize: [Role.Customer, Role.Admin],
      pharmaRequired: true,
    },

    component: DashboardCustomer,
  },
  {
    path: "/pro/dashboard",
    name: "DashboardPro",
    meta: {
      authorize: [Role.Owner, Role.Employee, Role.Admin],
      pharmaRequired: false,
    },

    component: DashboardPro,
  },
  {
    path: "/admin/dashboard",
    name: "DashboardAdmin",
    meta: {
      authorize: [Role.Admin],
      pharmaRequired: false,
    },

    component: DashboardAdmin,
  },
  {
    path: "/customer/catalog",
    name: "Catalog",
    meta: {
      authorize: [Role.Customer, Role.Admin],
      pharmaRequired: true,
    },

    component: Catalog,
  },
  {
    path: "/pro/register",
    name: "RegisterPro",
    meta: {
      pharmaRequired: false,
    },

    component: RegisterPro,
  },
  {
    path: "/customer/cart",
    name: "Cart",
    meta: {
      authorize: [Role.Customer],
      pharmaRequired: true,
    },

    component: Cart,
  },
  {
    path: "/customer/pharma-picker",
    name: "PharmaPicker",
    meta: {
      authorize: [Role.Customer],
      pharmaRequired: false,
    },

    component: PharmaPicker,
  },
  {
    path: "/customer/Drug",
    name: "Drug",
    meta: {
      authorize: [Role.Customer, Role.Admin],
      pharmaRequired: true,
    },

    component: Drug,
  },
  {
    path: "/pro/welcome",
    name: "WelcomePro",
    meta: {
      pharmaRequired: false,
    },
    component: WelcomePro,
  },
  {
    path: "/create-pharma",
    name: "CreatePharma",
    meta: {
      authorize: [Role.Owner, Role.Admin],
      pharmaRequired: false
    },

    component: CreatePharma,
  },
  // otherwise redirect to home
  { path: "/:pathMatch(.*)*", redirect: "/" },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const { authorize, pharmaRequired } = to.meta;
  const currentUser = store.state.currentUser;

  if (authorize) {
    if (!currentUser) {
      // not logged in so redirect to login page with the return url
      return next({ path: "/login", query: { returnUrl: to.path } });
    }

    // check if route is restricted by role
    if (authorize.length && !authorize.includes(currentUser.role.name)) {
      // role not authorised so redirect to home page
      return next({ path: "/" });
    }

    // check if the vue is restricted to the users with a selected pharmacy
    if (pharmaRequired && !currentUser.pharmacy_id) {
      if (currentUser.role.name === Role.Customer) {
        return next({ path: "/customer/pharma-picker" });
      } else if (currentUser.role.name === Role.Owner) {
        return next({ path: "/create-pharma" });
      } else {
        return next({ path: "/" });
      }
    }
  }


  next();
});
