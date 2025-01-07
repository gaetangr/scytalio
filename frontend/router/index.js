import { createRouter, createWebHistory } from 'vue-router';
import Layout from '@/components/Layout.vue';
import EncryptPage from '@/components/EncryptPage.vue';
import DecryptMessage from '@/components/DecryptMessage.vue';
import AboutPage from '@/components/AboutPage.vue';
import TermsOfUsePage from '@/components/TermsOfUsePage.vue';
import PrivacyPolicyPage from '@/components/PrivacyPolicyPage.vue';


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
   
      {
        path: 'terms-of-use',
        name: 'TermsOfUse',
        component: TermsOfUsePage,
      },
      {
        path: 'privacy-policy',
        name: 'PrivacyPolicy',
        component: PrivacyPolicyPage,
      },
      {
        path: 'mit-license',
        name: 'MITLicense',
        beforeEnter() {
          window.location.href = 'https://github.com/gaetangr/scytalio/blob/main/LICENSE';
        },
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;