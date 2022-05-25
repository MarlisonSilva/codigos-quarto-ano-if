var elementosCores = document.getElementsByClassName('cor');
var opc = null;
var pontos = 0;

function novoJogo() {
    let red = Math.floor(Math.random() * 256);
    let green = Math.floor(Math.random() * 256);
    let blue = Math.floor(Math.random() * 256);
    opc = Math.floor(Math.random() * 3);
    document.getElementById('cor-gerada').innerHTML = 'RGB('+red+', '+green+', '+blue+')';
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
    if (opc != null){
        if (corClicada == opc) {
            alert('PARABÉNS! VOCÊ ACERTOU A COR!')
            pontos++;
            document.querySelector('#pontos').innerHTML = pontos;
            novoJogo();
        } else {
            alert('QUE PENA! VOCÊ ERROU A COR! A cor correta era '+(opc+1)+'ª da esquerda para a direita')
            novoJogo();
        }
    }
}