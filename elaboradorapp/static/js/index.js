const disciplina = document.getElementById('disciplina');
const bimestre = document.getElementById('bimestre');
const tipo_prova = document.getElementById('tipo_prova');

document.getElementById('topo').value = 'Avaliação ' + tipo_prova.value + ' de ' + disciplina.value + ' - ' + bimestre.value;

disciplina.addEventListener('change', function () {
    document.getElementById('topo').value = 'Avaliação ' + tipo_prova.value + ' de ' + disciplina.value + ' - ' + bimestre.value;
});

bimestre.addEventListener('change', function () {
    document.getElementById('topo').value = 'Avaliação ' + tipo_prova.value + ' de ' + disciplina.value + ' - ' + bimestre.value;
});

tipo_prova.addEventListener('change', function () {
    document.getElementById('topo').value = 'Avaliação ' + tipo_prova.value + ' de ' + disciplina.value + ' - ' + bimestre.value;
});

const serie = document.getElementById('serie');

serie.addEventListener('change', function () {
    if (serie.value == 'Indefinido') {
        document.getElementById('turma').value = '1º Ano';
    } else {
        document.getElementById('turma').value = serie.value + 'º Ano';
    }
});