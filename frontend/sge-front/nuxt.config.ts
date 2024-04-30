// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  typescript: {
    typeCheck: true
  },
  modules: [
    'nuxt-primevue',
    '@sidebase/nuxt-auth'
  ],
  primevue: {
    components: {
      include: ['Button']
    }
  },
  css: [
    'primeicons/primeicons.css', //css dos ícones do primevue
    'primevue/resources/themes/aura-light-green/theme.css', // css tema dos componentes primevue
    '~/assets/style/global-variables.scss',  //variáveis css global customizado para toda a aplicação
    '~/assets/style/global-project.scss',  //css global customizado para toda a aplicação
  ],
  auth: {
    baseURL: 'http://localhost:8000',//process.env.BACKEND_URL,//'http://localhost:8000',//endereço do backend
    provider: {
      type: 'local',//biblioteca sidebase no modo local (webToken)
      endpoints: {
        signIn: { path: '/token/login', method: 'post' },//endereço do djoser
        signOut: { path: '/token/logout', method: 'post' },//endereço do djoser
        //signUp: false,//criar usuário novo (desativado temporáriamente)
        getSession: { path: '/users', method: 'get' },//endereço p/ confirmar token
      },
      token: { signInResponseTokenPointer: '/auth_token', type: 'Token' },
      pages: { login: '/' }//endereço da página de login do front
    }
  }
})
