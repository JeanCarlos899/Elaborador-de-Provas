
// Obter o botão
var botaoNegrito = document.querySelector(".bold");

// Adicionar event listener
botaoNegrito.addEventListener("click", function () {
    // Obter a seleção de texto
    let selecao = window.getSelection();

    // Verificar se há texto selecionado
    if (selecao.toString().length > 0) {
        moments.saveMoment();
        // Criar um novo elemento span
        try {
            let novoElemento = document.createElement("span");
            novoElemento.style.fontWeight = "bold";
            // Obter o range da seleção
            let range = selecao.getRangeAt(0);
            // Inserir o novo elemento no range
            range.surroundContents(novoElemento);
        } catch (error) {
            // ignore
        }
    }
});

// Obter o botão
var botaoItalico = document.querySelector(".italic");

// Adicionar event listener
botaoItalico.addEventListener("click", function () {
    // Obter a seleção de texto
    let selecao = window.getSelection();

    // Verificar se há texto selecionado
    if (selecao.toString().length > 0) {
        moments.saveMoment();
        // Criar um novo elemento span
        try {
            let novoElemento = document.createElement("span");
            novoElemento.style.fontStyle = "italic";
            // Obter o range da seleção
            let range = selecao.getRangeAt(0);
            // Inserir o novo elemento no range
            range.surroundContents(novoElemento);
        } catch (error) {
            // ignore
        }
    }
});

// Obter o botão
var botaoSublinhado = document.querySelector(".underline");

// Adicionar event listener
botaoSublinhado.addEventListener("click", function () {
    // Obter a seleção de texto
    let selecao = window.getSelection();

    // Verificar se há texto selecionado
    if (selecao.toString().length > 0) {
        moments.saveMoment();
        // Criar um novo elemento span
        try {
            let novoElemento = document.createElement("span");
            novoElemento.style.textDecoration = "underline";
            // Obter o range da seleção
            let range = selecao.getRangeAt(0);
            // Inserir o novo elemento no range
            range.surroundContents(novoElemento);
        } catch (error) {
            // ignore
        }
    }
});


// Obter o botão
var fontCase = document.querySelector(".font-case");

// Adicionar event listener
fontCase.addEventListener("click", function () {
    let selecao = window.getSelection();

    // Verificar se há texto selecionado
    if (selecao.toString().length > 0) {
        moments.saveMoment();
        // Obter o range da seleção
        try {
            let range = selecao.getRangeAt(0);
            // Criar um novo texto com o conteúdo em maiúsculas
            let novoTexto = document.createTextNode(selecao.toString().toUpperCase());
            // Remover o conteúdo antigo
            range.deleteContents();
            // Inserir o novo texto no range
            range.insertNode(novoTexto);
        } catch (e) {
            // ignorar
        }
    }
});

// Obter o botão
var fontColor = document.querySelector(".color");
var estadoBotaoColor = false;

// Adicionar event listener
fontColor.addEventListener("click", function () {
    estadoBotaoColor = !estadoBotaoColor;
    if (estadoBotaoColor) {
        // Ativar formatação de negrito
        fontColor.style.color = "#1a73e8";
        fontColor.style.backgroundColor = "#e0e0e0";
        fontColor.style.borderRadius = "5px";
        document.addEventListener("mouseup", formataFontColor);
    } else {
        // Desativar formatação de negrito
        fontColor.style.color = "";
        fontColor.style.backgroundColor = "";
        fontColor.style.borderRadius = "";
        document.removeEventListener("mouseup", formataFontColor);
    }
});

function formataFontColor() {
    let selecao = window.getSelection();
    if (selecao.toString().length > 0) {
        moments.saveMoment();
        try {
            let color = document.querySelector(".color-picker-input").value;
            let novoElemento = document.createElement("span");
            novoElemento.style.color = color;
            let range = selecao.getRangeAt(0);
            range.surroundContents(novoElemento);
        } catch (error) {
            // ignore
        }
    }
}

function reorganizarNumeracao() {
    // obter todos os elementos com a classe "questao"
    let questoes = document.querySelectorAll("#questao");

    // obter todos os elementos com a classe "questão-{{ forloop.counter }} div-questoes"
    let divQuestoes = document.querySelectorAll(".div-questoes");

    // atualizar a numeração de cada elemento
    for (let i = 0; i < questoes.length; i++) {
        // encontrar o elemento "strong" dentro da questão
        let strong = questoes[i].querySelector("strong");

        // atualizar o número da questão
        let numQuestao = i + 1;
        strong.innerHTML = numQuestao + ". ";

        // atualizar a classe da div-questoes com a nova numeração
        let classeAtual = divQuestoes[i].className;
        let novaClasse = classeAtual.replace(
            /questao-\d+/,
            `questao-${numQuestao}`
        );
        divQuestoes[i].className = novaClasse;

        // atualizar a numeração recursivamente em todas as sub-questões
        reorganizarSubNumeracao(questoes[i], numQuestao);
    }

    // selecionar todas as linhas da tabela de gabarito
    let linhasGabarito = document.querySelectorAll('.tr-questao-gabarito');

    // iterar sobre as linhas e atualizar as classes
    for (let i = 0; i < linhasGabarito.length; i++) {
        // obter o número da questão
        let numQuestao = i + 1;

        // atualizar a classe da linha com a nova numeração
        let classeAtual = linhasGabarito[i].className;
        let novaClasse = classeAtual.replace(
            /tr-questao-\d+/,
            `tr-questao-${numQuestao}`
        );
        linhasGabarito[i].className = novaClasse;
    }


    // atualizar a numeração das questões do gabarito
    let trQuestoes = document.querySelectorAll(".tr-questao-gabarito");
    for (let i = 0; i < trQuestoes.length; i++) {
        let numeroDaQuestao = trQuestoes[i].querySelector(".numero-da-questao");
        numeroDaQuestao.innerHTML = i + 1;
    }
}

function reorganizarSubNumeracao(parentElement, index) {
    // obter todos os elementos com a classe "questao"
    let subQuestoes = parentElement.querySelectorAll("#questao");

    // atualizar a numeração de cada sub-questão
    for (let i = 0; i < subQuestoes.length; i++) {
        // encontrar o elemento "strong" dentro da sub-questão
        let strong = subQuestoes[i].querySelector("strong");

        // atualizar o número da sub-questão
        strong.innerHTML = index + "." + (i + 1);

        // atualizar o número da sub-questão no gabarito
        let gabaritoNum = document.querySelector(
            `.tr-questao-${parentElement.dataset.id} .gabarito-num-${i + 1}`
        );
        gabaritoNum.innerHTML = index + "." + (i + 1);

        // atualizar a numeração recursivamente em todas as sub-questões
        reorganizarSubNumeracao(subQuestoes[i], index + "." + (i + 1));
    }
}

var trashButton = document.querySelector(".trash");

trashButton.addEventListener("click", function () {
    let numberQuestionDelete = document.querySelector(".number-question-delete").value;
    let question = document.querySelector(`.questao-${numberQuestionDelete}`);
    let trQuestion = document.querySelector(`.tr-questao-${numberQuestionDelete}`);
    // pedir uma confirmação
    let confirmacao = confirm("Tem certeza que deseja excluir esta questão?");
    if (confirmacao && question) {
        question.remove();
        trQuestion.remove();
        reorganizarNumeracao();
    }
});