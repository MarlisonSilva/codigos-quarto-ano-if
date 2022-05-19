var corGeradaReal = null;
var corGeradaFalsa1 = null;
var corGeradaFalsa2 = null;
var elmCorGeradaReal = document.getElementById('cor-gerada');
var elmCor1 = document.getElementById('cor1');
var elmCor2 = document.getElementById('cor2');
var elmCor3 = document.getElementById('cor3');
var elementosCores = [elmCor1, elmCor2, elmCor3];
var opc = null;
var pontos = 0;

function novoJogo() {
    let red = Math.floor(Math.random() * 256);
    let green = Math.floor(Math.random() * 256);
    let blue = Math.floor(Math.random() * 256);
    console.log(red)
    console.log(green)
    console.log(blue)
    elmCorGeradaReal.innerHTML = 'RGB('+red+', '+green+', '+blue+')';
    opc = Math.floor(Math.random() * 3);
    console.log(opc)
    elementosCores[opc].style.backgroundColor = 'RGB('+red+', '+green+', '+blue+')';
    
    for (let i = 0; i < elementosCores.length; i++) {
        let red = Math.floor(Math.random() * 256);
        let green = Math.floor(Math.random() * 256);
        let blue = Math.floor(Math.random() * 256);
        if (i != opc)
            elementosCores[i].style.backgroundColor = 'RGB('+red+', '+green+', '+blue+')';

    }
}

function verificar(corClicada) {
    if (corClicada == opc) {
        alert('PARABÉNS! VOCÊ ACERTOU A COR!')
        pontos++;
        document.querySelector('#pontos').innerHTML = pontos;
        novoJogo();
    } else {
        alert('QUE PENA! VOCÊ ERROU A COR!')
        novoJogo();
        
    }
}