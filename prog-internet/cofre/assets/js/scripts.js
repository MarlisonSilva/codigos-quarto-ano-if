var pass = document.querySelector('#password')
function verifyPass(){     
    if (pass.value.length >= 8 && pass.value.length <= 14) {
       alert(pass.value.substr(0, 1))
    } else {

    }
}