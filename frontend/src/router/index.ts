import { createRouter, createWebHistory } from 'vue-router'
import CreateAccount from '../components/CreateAccount.vue'
import Home from '../components/Home.vue'
import Login from '../components/Login.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/create-account',
      name: 'CreateAccount',
      component: CreateAccount
    },
	
	{
	  path: '/login',
	  name: 'Login',
	  component: Login
	}
	
  ]
})

export default router
