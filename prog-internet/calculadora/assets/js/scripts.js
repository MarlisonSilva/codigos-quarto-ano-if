var resultado = document.querySelector('#resultado');
var numAnterior = null;
function soma() {
    numAnterior = resultado.innerHTML;
}

function subtracao() {
    numAnterior = resultado.innerHTML;
}

function multiplicacao() {
    numAnterior = resultado.innerHTML;
}

function divisao() {
    numAnterior = resultado.innerHTML;
}

function addNum(num) {
    if (numAnterior != null) {
        resultado.innerHTML = 0;
    }

    if (resultado.innerHTML != "Resultado" && resultado.innerHTML != "0") {
        resultado.innerHTML += num;
    } else {
        resultado.innerHTML = num;
    }



}

function ponto() {
    if (resultado.innerHTML != "Resultado" && resultado.innerHTML != "0") {
        resultado.innerHTML += ".";
    } 
}

function igualdade() {

}

function limpar() {
    resultado.innerHTML = 0;
}