var valorTabuada = document.querySelector('#valorTabuada');
var inicioTabuada = document.querySelector('#inicioTabuada');
var fimTabuada = document.querySelector('#fimTabuada');
var tabelaTabuada = document.querySelector('#tabuada');
var vTabelaTabuada = "";
function calcular() {
    for (let i = inicioTabuada.value; i <= fimTabuada.value; i++) {        
        let res = valorTabuada.value * i;
        vTabelaTabuada += "<tr> <td>"+valorTabuada.value+"</td> <td>"+i+"</td> <td>"+res+"</td> </tr>";
    }
    tabelaTabuada.innerHTML = "<table> "+vTabelaTabuada+"</table>";
}