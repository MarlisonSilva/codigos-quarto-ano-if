var pass = document.querySelector('#password')
function verifyPass(){     
    if (pass.value.length >= 8 && pass.value.length <= 14) {
        var exp1 = /^[a-z]/i;
        
        alert(exp1.test(pass.value))
        
    } else {

    }
}


function isAlpha(ch){
    return typeof ch === "string" && (ch >= "a" && ch <= "z" || ch >= "A" && ch <= "Z");
}