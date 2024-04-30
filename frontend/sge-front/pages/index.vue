<script setup lang="ts">
    import { ref, computed, reactive } from 'vue'
    const { signIn } = useAuth() //importando a função de login da sidebase
    
    //JÉSSICA NÃO TRANQUE O CURSO:
    //const username = ref('')
    //const password = ref('')

    const credentials = reactive({
        email: '',
        password: ''
    });

    //para lidar com promises, podemos usar o try/catch com o async/await    
    /*const submitLogin = async()=>{
        console.log("trying to login with credentials below:", credentials);
        try{
            await signIn(credentials, {redirect: false});
            navigateTo('/home');
        } catch(error){
            console.log("Error when trying to login: ", error);
        }
    }*/
    
    //também podemos lidar com Promises usando o then/catch
    const submitLogin = ()=>{
        console.log("trying to login with credentials below:", credentials);        
        signIn(credentials, {redirect: false})
        .then(()=>{
            console.log("successfully logged!!");
            navigateTo('/home');
        })
        .catch((error)=>{
            console.log("Error when trying to login: ", error);
        });
    }
    


    /*
    exemplos para explicar typescript
    const teste = 'ok'
    const value1 = ref(0)
    const value2 = ref(0)   
    const makeMul = (n1:number,n2:number):number => n1 * n2

    const result = computed(()=> makeMul(value1.value,value2.value))*/
</script>

<template>
    <!--
    <div>
        <h1>My HomePage!!!</h1>
        <p>{{ teste }}</p>
        <input type="text" v-model="value1">
        <input type="text" v-model="value2">
        <p>Result: {{ result }}</p>
    </div>-->
    <main class="flex_center login_main"> 
        <!-- content of logo image -->
        <section class="logo_panel flex_center">
            <img src="/sge.jpeg" alt="sge logo">
            <h1>Sistema de Gestão de Ensino</h1>
            <p>&reg; Senai Roberto Mange</p>
            <div class="stars1"></div>
            <div class="stars2"></div>
            <div class="stars3"></div>
        </section>

         <!-- content of login form -->
         <section class="login_panel">
            <div class="login_content flex_center">
                <h1>LOGIN</h1>
                <form class="login_form" v-on:submit.prevent="submitLogin">
                    <div class="input_container">
                        <CustomInput type="email" label="LOGIN" inputId="user_login"
                            v-model="credentials.email"
                        />
                    </div>
                    <div class="input_container">
                        <CustomInput label="SENHA" type="password" inputId="pass_login" 
                            v-model="credentials.password"
                        />
                    </div>
                    <button type="submit" class="customButton">ENTRAR</button>
                </form>
            </div>
        </section>
    </main>
</template>

<style scoped lang="scss">

    .flex_center{
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
    }

    .login_main{
        width: 100vw;
        height: 100vh;       
        background-color: var(--dark-background-color);

        .logo_panel{
            display: none;
            width: 50vw;
            height: 100vh;   
            flex-direction: column;  
            color: var(--light-background-color);       
            img{              
                margin: 0px 0px 25px 0px;
                align-items: center;
                width: 65%;
                height: 45%;
            }
        }

        .login_panel{
            width: 100vw;
            height: 100vh;  
            background-color: var(--light-background-color);

            .login_content{
                flex-direction: column;
                width: 100%;
                height: 80%;

                h1{
                    width: 120px;
                    padding-top: 10px;
                    padding-bottom: 50px;
                    font-size: 36px;
                }
                .login_form{
                    width: 60%;
                    .input_container{
                        margin-top: 30px;
                    }
                    .customButton{
                        margin-top: 50px;
                    }
                }
            }
        }
    }

    @media screen and (min-width: 550px){
        .login_main{
            .login_panel{
                width: 50vw;
            }
            .logo_panel{
                display: flex;
            }
        }
    }

        

</style>