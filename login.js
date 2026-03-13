async function loginUser(){

let username=document.getElementById("username").value
let password=document.getElementById("password").value

let form=new FormData()

form.append("username",username)
form.append("password",password)

let res=await fetch("http://127.0.0.1:5000/login",{

method:"POST",
body:form

})

let data=await res.json()

alert(data.message)

if(data.status==="success"){

localStorage.setItem("user",username)

window.location.href="index.html"

}

}