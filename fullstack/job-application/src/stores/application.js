import {defineStore} from 'pinia'
export const useApplicationStore = defineStore('application',{
    state:()=>({
        personal:{
            name:'',
            email:'',
            phone:'',
            dob:''
        },
        education:{
            degree:'',
            instituiton:'',
            year:''
        },
        experience:[]
    })
})