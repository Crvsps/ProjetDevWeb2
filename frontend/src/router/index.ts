import { createRouter, createWebHistory } from 'vue-router'
import CreateAccount from '../components/CreateAccount.vue'
import HomePage from '../components/HomePage.vue'
import LoginPage from '../components/LoginPage.vue'
import ProfilPage from '../components/ProfilPage.vue'
import Dashboard from '../components/Dashboard.vue'
import DashboardAdmin from '../components/DashboardAdmin.vue'
import UserAdmin from '../components/UserAdmin.vue'
import RechercheObj from '../components/RechercheObj.vue'
import DashboardAdvanced from '../components/DashboardAdvanced.vue'
import ObjectsAdvanced from '../components/ObjectsAdvanced.vue'
import DetailObjet from '../components/DetailObjet.vue'
import PageRecherche from '../components/PageRecherche.vue'
import GestionObjet from '@/components/GestionObjet.vue'
import AjouterObjet from '@/components/AjouterObjet.vue'
import AideSchool from '../components/AideSchool.vue'
import ActualitesSchool from '../components/Actualites.vue'


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
      name: 'profil',
      component: ProfilPage
    },
    {
      path: '/register',
      name: 'register',
      component: CreateAccount
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard
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
      path: '/ajouter-objet',
      name: 'ajouter-objet',
      component: AjouterObjet
    },
	{
      path: '/dashboard-advanced',
      name: 'dashboard-advanced',
      component: DashboardAdvanced
    },
    {
      path: '/:category_slug/:object_slug',
      name: 'detail',
      component: DetailObjet
    },
    {
      path: '/gestion/:category_slug/:object_slug',
      name: 'gestion',
      component: GestionObjet
    },
    {
      path: '/AideSchool',
      name: 'AideSchool',
      component: AideSchool
    },
    {
      path: '/actualites',
      name: 'actualites',
      component: ActualitesSchool
    }
  ]});

router.beforeEach((to, from, next) => {
  const publicPages = ['/', '/login', '/register','/AideSchool', '/actualites'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('token');

  if (authRequired && !loggedIn) {
    next('/login');
  } else {
    next();
  }
});


export default router