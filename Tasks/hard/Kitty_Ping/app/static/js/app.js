var app=new Vue({
    el:"#app",
    data:{
        result:"",
        address:"",
    },
    methods:{
        fetch_data(){
            fetch("/ping",{
                method:'post',
                body:document.getElementsByName("address")[0].value
            }).then(response=>response.json()).then(response=>this.result=response.result)
        },
    }
})
