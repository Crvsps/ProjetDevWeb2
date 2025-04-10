import { createRouter, createWebHistory } from 'vue-router'
import CreateAccount from '../components/CreateAccount.vue'
import HomePage from '../components/HomePage.vue'
import LoginPage from '../components/LoginPage.vue'
import ProfilPage from '../components/ProfilPage.vue'
import DashboardPage from '../components/Dashboard.vue'
import DashboardAdmin from '../components/DashboardAdmin.vue'
import UserAdmin from '../components/UserAdmin.vue'
import RechercheObj from '../components/RechercheObj.vue'
import DashboardAdvanced from '../components/DashboardAdvanced.vue'
import ObjectsAdvanced from '../components/ObjectsAdvanced.vue'
import DetailObjet from '../components/DetailObjet.vue'
import PageRecherche from '../components/PageRecherche.vue'


const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/search',
      name: 'search',
      component: PageRecherche
    },
    {
      path: '/login',
      name: 'login',
      component: LoginPage
    },
    {
      path: '/profil',
      name: 'profil-page',
      component: ProfilPage
    },
    {
      path: '/create-account',
      name: 'create-account',
      component: CreateAccount
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardPage
    },
    {
      path: '/dashboardAdmin',
      name: 'dashboardAdmin',
      component: DashboardAdmin
    },
	{
      path: '/user-admin',
      name: 'user-admin',
      component: UserAdmin
    },
  {
      path: '/recherche-objet',
      name: 'recherche-objet',
      component: RechercheObj
    },
	{
      path: '/dashboard-advanced',
      name: 'dashboard-advanced',
      component: DashboardAdvanced
    },
	{
      path: '/objects-advanced',
      name: 'objects-advanced',
      component: ObjectsAdvanced
    },
    {
      path: '/:category_slug/:object_slug',
      name: 'detail',
      component: DetailObjet
    },
  ]
})

export default router