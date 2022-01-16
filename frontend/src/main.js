import { createApp } from "vue";
import App from "@/App.vue";
import router from "@/router";
import store from "@/store";
import vueDebounce from 'vue-debounce'
import "@/axios";

/* import the fontawesome core */
import { library } from "@fortawesome/fontawesome-svg-core";

/* import specific icons */
import { faUser } from "@fortawesome/free-solid-svg-icons";

/* import font awesome icon component */
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

/* add icons to the library */
library.add(faUser);

createApp(App)
  .component("font-awesome-icon", FontAwesomeIcon)
  .use(store)
  .use(router)
  .use(vueDebounce, {
    listenTo: ['input', 'keyup']
  })
  .mount("#app");
