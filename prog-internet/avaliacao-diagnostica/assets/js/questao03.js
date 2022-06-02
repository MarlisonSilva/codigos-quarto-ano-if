// var cores = document.querySelector('cores');
const cores = document.querySelectorAll('.cor');
function carregarCores() {    
    for (let i = 0; i < cores.length; i++) {     
        let red = Math.floor(Math.random() * 256);
        let green = Math.floor(Math.random() * 256);
        let blue = Math.floor(Math.random() * 256);   
        cores[i].style.backgroundColor = 'rgb('+red+', '+green+', '+blue+')';        
    }
}

function clicou(corClicada) {
    document.body.style.backgroundColor = cores[corClicada].style.backgroundColor;
}