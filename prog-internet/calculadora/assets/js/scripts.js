var resultado = document.querySelector('#resultado');
var numAnterior = null;
var funcaoClicada = null;
var resetNum = false;
var elementoSoma = document.querySelector('#soma');
var elementoSubtracao = document.querySelector('#subtracao');
var elementoMultiplicacao = document.querySelector('#multiplicacao');
var elementoDivisao = document.querySelector('#divisao');
var ultElementoClicado = null;
function soma() {
    numAnterior = resultado.innerHTML;
    funcaoClicada = "+";
    if (ultElementoClicado != null) {
        ultElementoClicado.classList.remove("button-calc-clicado");        
    }
    elementoSoma.classList.add("button-calc-clicado");

    resetNum = true;
    ultElementoClicado = elementoSoma;
}

function subtracao() {
    numAnterior = resultado.innerHTML;
    funcaoClicada = "-";
    if (ultElementoClicado != null) {
        ultElementoClicado.classList.remove("button-calc-clicado");        
    }
    elementoSubtracao.classList.add("button-calc-clicado");

    resetNum = true;
    ultElementoClicado = elementoSubtracao;

}

function multiplicacao() {
    numAnterior = resultado.innerHTML;
    funcaoClicada = "*";
    if (ultElementoClicado != null) {
        ultElementoClicado.classList.remove("button-calc-clicado");        
    }
    elementoMultiplicacao.classList.add("button-calc-clicado");

    
    resetNum = true;
    ultElementoClicado = elementoMultiplicacao;
}

function divisao() {
    numAnterior = resultado.innerHTML;
    funcaoClicada = "/";
    if (ultElementoClicado != null) {
        ultElementoClicado.classList.remove("button-calc-clicado");        
    }
    elementoDivisao.classList.add("button-calc-clicado");    

    resetNum = true;
    ultElementoClicado = elementoDivisao;
}

function addNum(num) {
    if (resetNum) {
        resultado.innerHTML = 0;
        resetNum = false;
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
    if (ultElementoClicado != null) {
        ultElementoClicado.classList.remove("button-calc-clicado");        
    }
    resultado.innerHTML = eval(numAnterior + funcaoClicada + resultado.innerHTML);
}

function limpar() {
    if (ultElementoClicado != null) {
        ultElementoClicado.classList.remove("button-calc-clicado");        
    }
    numAnterior = 0;
    resultado.innerHTML = 0;
}
