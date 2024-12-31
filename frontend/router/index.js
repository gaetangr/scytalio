import { createRouter, createWebHistory } from 'vue-router';
import Layout from '@/components/Layout.vue';
import EncryptPage from '@/components/EncryptPage.vue';
import DecryptMessage from '@/components/DecryptMessage.vue';
import AboutPage from '@/components/AboutPage.vue';

const routes = [
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: '',
        redirect: '/encrypt', 
      },
      {
        path: 'encrypt',
        name: 'Encrypt',
        component: EncryptPage,
      },
      {
        path: 'decrypt/:id',
        name: 'decrypt',
        component: DecryptMessage,
        props: route => ({
          key: route.query.key,
          messageId: route.params.id,
        }),
      },
      {
        path: 'about',
        name: 'About',
        component: AboutPage,
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;