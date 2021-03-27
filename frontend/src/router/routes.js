
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: '/login', component: () => import('pages/login.vue') },
      { path: '/register', component: () => import('pages/register.vue') },
    ]
  },
  { // 404 page
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
