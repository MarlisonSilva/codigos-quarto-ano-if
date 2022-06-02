var meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
function converter() {
    let data = document.querySelector('#data');
    let data_extenso = document.querySelector('#data-extenso');
    let data_array = data.value.split('/');
    data_extenso.innerHTML = data_array[0]+ ' de '+meses[parseInt(data_array[1]) - 1]+' de '+data_array[2];
}